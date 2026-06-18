# TECH_SPEC.md – locale‑flow  
**Product:** AxentX – Translation Pipeline Automation Tool  
**Repository:** `locale-flow`  

---  

## 1. Overview  

`locale-flow` is a fully‑automated, end‑to‑end localization pipeline designed for modern development teams. It ingests source strings from a codebase, routes them through a configurable translation stack (machine translation, human review, glossaries, TM), and pushes the localized assets back into the repository or a CDN.  

Key goals:  

| Goal | Success Metric |
|------|----------------|
| **Speed** – Translate a new commit of ≤10 k strings in < 5 min (including model inference). |
| **Quality** – ≥ 95 % of machine‑translated strings pass automated QA (placeholder integrity, length limits). |
| **Reliability** – 99.9 % uptime of the API & worker services. |
| **Scalability** – Horizontal scaling to handle 100 M string pairs per week (aligned with AxentX growth). |
| **Security** – All data in‑transit encrypted, at‑rest encrypted, role‑based access control (RBAC). |

---  

## 2. Architecture  

```
+-------------------+        +-------------------+        +-------------------+
|   CI/CD System    |  ---> |   Locale‑Flow API |  --->  |   Task Queue (R)  |
| (GitHub Actions) |        |  (FastAPI)        |        |   Redis / Rabbit  |
+-------------------+        +-------------------+        +-------------------+
                                 |   ^   |
                                 |   |   |
                +----------------+   |   +----------------+
                |                    |                    |
        +-------v------+      +------v------+      +------v------+
        |   Worker #1  |      |   Worker #2 | …  |   Worker N  |
        | (Celery +   |      | (Celery +   |    | (Celery +   |
        |  vLLM/SG)    |      |  vLLM/SG)   |    |  vLLM/SG)   |
        +-------+------+      +------+------+    +------+------+
                |                     |                 |
                |                     |                 |
        +-------v------+      +-------v------+   +------v------+
        |   PostgreSQL |      |   Object Store|   |   Glossary   |
        |   (metadata) |      |   (S3/MinIO)  |   |   Service    |
        +--------------+      +---------------+   +-------------+

```

* **Locale‑Flow API** – Public REST/GraphQL entry point for CI pipelines, UI, and webhooks.  
* **Task Queue** – Redis (development) or RabbitMQ (production) used by Celery workers.  
* **Workers** – Stateless containers that execute translation jobs. They invoke:  
  * **vLLM** – High‑throughput inference engine for large language models (e.g., Llama‑3‑8B).  
  * **SGLang** – Structured generation for glossary‑aware, placeholder‑preserving output.  
* **PostgreSQL** – Stores project definitions, string catalogs, job metadata, audit logs.  
* **Object Store** – Stores large binary assets (XLIFF, JSON bundles, translation memories).  
* **Glossary Service** – Optional micro‑service exposing term‑lookup via gRPC.  

All components are containerised and orchestrated via Helm on a Kubernetes cluster.  

---  

## 3. Core Components  

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **API Gateway** | Auth, rate‑limit, request validation | FastAPI + OAuth2 (Auth0) |
| **Scheduler** | Convert PR events → translation jobs | Celery beat + PostgreSQL |
| **Worker** | Pull job, run MT, apply TM/glossary, post‑process, store results | Python 3.11, Celery, vLLM, SGLang |
| **Translation Memory (TM)** | Store previously approved translations, fuzzy‑match | PostgreSQL `tm` schema + pgvector index |
| **Glossary Service** | Term‑level overrides, case‑sensitive lookup | gRPC (Python `grpcio`) |
| **CLI** | Local dev/ops tool for ad‑hoc runs, inspection | Click + Rich |
| **UI (future)** | Dashboard for job monitoring, review | React + Vite (outside repo) |
| **Metrics & Logging** | Prometheus metrics, Loki logs, OpenTelemetry traces | Prometheus, Grafana, Loki, OTEL SDK |

---  

## 4. Data Model  

### 4.1 ER Diagram (simplified)

```
Project ──< Locale
   │           │
   │           └─< StringCatalog
   │                     │
   │                     └─< SourceString
   │                               │
   │                               └─< TranslationJob
   │                                         │
   │                                         └─< TranslationResult
   │
   └─< User (RBAC)
```

###
