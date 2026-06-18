# ROADMAP.md – locale‑flow

## Vision
**locale‑flow** is a developer‑centric translation pipeline that automates extraction, translation, review, and integration of localized strings. It enables product teams to ship multilingual features with minimal manual effort, consistent quality, and full CI/CD integration.

---

## Milestones Overview

| Milestone | Target Release | Core Theme | MVP‑Critical Items |
|-----------|----------------|------------|--------------------|
| **MVP**   | **2026‑09‑30** | End‑to‑End Automation for a Single Repo | ✅ Extraction + Sync + Machine‑Translate + PR generation |
| **v1.0**  | 2026‑12‑15 | Team Collaboration & Quality Gates | ✅ Review UI, Glossary, CI integration, Metrics |
| **v2.0**  | 2027‑03‑31 | Enterprise Scale & Extensibility | ✅ Multi‑repo orchestration, Custom MT engines, SaaS dashboard |

---

## MVP – Minimum Viable Product (Launch)

**Goal:** Deliver a fully automated, single‑repository localization flow that can be run from the command line or CI pipeline and produces a ready‑to‑merge PR with translated resources.

| Feature | Description | Acceptance Criteria |
|---------|-------------|----------------------|
| **1️⃣ Extraction Engine** | Parse source code (JS/TS, Python, Java, Go) and extract i18n keys into a canonical `messages.pot` file. | - Supports at least 3 language‑specific extraction plugins.<br>- Handles plural forms and context tags.<br>- Generates deterministic output (stable hashes). |
| **2️⃣ Translation Sync** | Upload `messages.pot` to a configurable MT provider (e.g., OpenAI GPT‑4o, DeepL) and pull translations into locale‑specific `.po`/`.json` files. | - Configurable provider API keys.<br>- Fallback to cached translations.<br>- Rate‑limit handling and retry logic. |
| **3️⃣ PR Generation** | Create a GitHub (or GitLab) Pull Request that adds/updates the locale files in the target repo. | - PR includes a concise diff and auto‑generated description.<br>- Optional “apply‑only” mode for non‑Git environments. |
| **4️⃣ CLI / CI Wrapper** | `locale-flow run --repo <path> --target <branch>` command usable locally or as a CI step. | - Zero‑config mode works on a fresh checkout.<br>- Exit codes reflect success, partial‑failure, or fatal error. |
| **5️⃣ Configuration Schema** | `locale-flow.yml` supporting source paths, exclusion patterns, MT provider, target branch, and PR options. | - Validation with clear error messages.<br>- Example file included in repo. |
| **6️⃣ Logging & Telemetry** | Structured JSON logs + optional opt‑in usage metrics (sent to Axentx BRAIN). | - Logs written to stdout/stderr.<br>- Metrics respect privacy flags. |

### MVP Success Metrics
- **Time to PR** ≤ 5 minutes for a repo of ≤ 10 k strings.
- **Translation coverage** ≥ 95 % for supported languages.
- **Zero manual steps** after initial config (except optional review).

---

## v1.0 – Collaboration & Quality

**Theme:** Empower teams to review, refine, and monitor translations while keeping the pipeline fully automated.

| Feature | Description | MVP‑Critical? |
|---------|-------------|---------------|
| **Interactive Review UI** | Web UI (React) showing extracted keys, machine translations, and edit controls. | ✅ |
| **Glossary & Terminology Management** | Central glossary that MT engine consults; UI for term overrides. | ✅ |
| **Quality Gates** | Configurable checks (e.g., length delta, placeholder integrity, profanity filter). PR fails if gates not met. | ✅ |
| **CI/CD Integration Plugins** | Official GitHub Actions, GitLab CI, Azure Pipelines, and generic Docker entrypoint. | ✅ |
| **Metrics Dashboard** | Per‑repo dashboard: strings processed, translation latency, review turnaround, coverage trends. | – |
| **Export Formats** | Support for additional i18n formats (`.arb`, `XLIFF`, `Android XML`). | – |
| **User Permissions** | Role‑based access (maintainer, reviewer, viewer) for the Review UI. | – |

### v1.0 Success Metrics
- **Review turnaround** ≤ 2 hours for a batch of ≤ 5 k strings.
- **Glossary adoption** ≥ 80 % of high‑frequency terms overridden.
- **Quality gate pass rate** ≥ 98 % on merged PRs.

---

## v2.0 – Enterprise Scale & Extensibility

**Theme:** Scale to multi‑repo, multi‑team environments and allow plug‑in of custom translation engines.

| Feature | Description | v2.0‑Only |
|---------|-------------|-----------|
| **Orchestrator Service** | Central service that tracks dozens of repos, schedules extraction runs, and aggregates results. | ✅ |
| **Custom MT Engine Plug‑in SDK** | SDK for teams to integrate proprietary NMT models (e.g., on‑prem LLMs via vLLM). | ✅ |
| **SaaS Dashboard & Billing** | Multi‑tenant UI with usage analytics, quota management, and Axentx billing integration. | ✅ |
| **Delta‑Sync & Incremental Updates** | Detect changed keys only; avoid re‑translating unchanged strings. | ✅ |
| **Localization Testing Harness** | Automated UI snapshot testing with localized strings to catch layout breaks. | – |
| **Compliance & Auditing** | Exportable audit logs, GDPR/CCPA data‑subject request handling. | – |
| **Marketplace of Language Packs** | Community‑contributed language packs (e.g., domain‑specific terminology). | – |

### v2.0 Success Metrics
- **Supported repos** ≥ 50 simultaneously with < 10 min average cycle time.
- **Custom MT adoption** ≥ 30 % of enterprise customers.
- **SLA** 99.9 % pipeline availability.

---

## Release Cadence & Governance

| Release | Frequency | Process |
|---------|-----------|---------|
| **MVP** | Fixed date (2026‑09‑30) | Internal QA → Security review → Beta‑tester sign‑off |
| **v1.x** | Quarterly (Q4 2026, Q1 2027) | Feature freeze → Public beta → GA |
| **v2.x** | Bi‑annual (mid‑2027, end‑2027) | Enterprise pilot → Feedback loop → Full launch |

All releases will be versioned following **Semantic Versioning** (`MAJOR.MINOR.PATCH`). Critical security patches are released as needed.

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **MT provider downtime** | Pipeline stalls | Built‑in fallback cache & multi‑provider fallback. |
| **Schema drift in extracted files** | Broken PRs | Schema validation step; automated rollback on failure. |
| **Privacy / data leakage** | Compliance breach | Opt‑in telemetry only; data‑at‑rest encryption; contracts with MT providers. |
| **Scaling orchestration** | Performance bottlenecks | Horizontal‑scalable microservice design; use of Axentx BRAIN for queueing. |

---

## Appendices

- **Repo Structure** – `src/`, `cli/`, `ui/`, `config/`, `tests/`
- **Tech Stack** – Python 3.11, FastAPI (orchestrator), React + Vite (UI), PostgreSQL, Redis, Docker, GitHub Actions.
- **Dependencies** – `vLLM` for custom MT, `SGLang` for structured generation, `poetry` for packaging.  

--- 

*Prepared by the Locale‑Flow Product & Engineering Lead, Axentx*  
*Last updated: 2026‑06‑18*
