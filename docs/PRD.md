# Product Requirements Document (PRD)  
**Project:** locale‑flow  
**Team:** Localization Automation (Product/Engineering)  
**Owner:** Senior Product Lead – [Your Name]  
**Date:** 2026‑06‑18  
**Version:** 1.0  

---  

## 1. Problem Statement  

Development teams spend excessive manual effort coordinating translation of UI strings, documentation, and configuration files across multiple locales. Current workflows involve:  

| Pain Point | Impact |
|------------|--------|
| **Fragmented tooling** – developers use separate scripts, spreadsheets, and third‑party services. | Increases context‑switching and onboarding time. |
| **Inconsistent releases** – translations lag behind code, causing feature roll‑outs to be delayed or shipped with missing/localized text. | Customer dissatisfaction & higher support cost. |
| **Lack of traceability** – no single source of truth linking code changes to translation status. | Hard to audit compliance and quality. |
| **High cost of re‑work** – missed strings, duplicated translations, and manual QA lead to re‑translation cycles. | Increases time‑to‑market and translation spend. |

**Result:** Teams cannot reliably ship localized features at the same cadence as core product releases, limiting market penetration and revenue growth.

---

## 2. Target Users  

| Persona | Role | Primary Needs |
|---------|------|----------------|
| **Frontend Engineer** | Writes UI code & string resources | One‑click extraction, sync, and validation of strings. |
| **Product Manager** | Prioritizes feature releases across regions | Visibility into translation progress and risk. |
| **Localization Manager** | Oversees translation vendors & in‑house linguists | Centralized task assignment, quality gates, and reporting. |
| **DevOps / Release Engineer** | Automates CI/CD pipelines | Seamless integration of translation steps into CI pipelines. |

---

## 3. Goals & Success Metrics  

| Goal | Success Metric (quantitative) | Target (12 mo) |
|------|------------------------------|----------------|
| **Accelerate localization cycle** | Avg. time from code commit to localized build | ≤ 24 h (down from 72 h) |
| **Reduce manual effort** | Engineer hours spent on translation tasks per sprint | ≤ 2 h (down from 8 h) |
| **Improve release reliability** | % of releases with 0 missing/placeholder strings | ≥ 98 % |
| **Increase translation spend efficiency** | Cost per localized string | ↓ 15 % vs baseline |
| **Adoption** | Number of active repositories using locale‑flow | ≥ 20 internal repos + 5 external partners |

---

## 4. Key Features (Prioritized)  

| Priority | Feature | Description | Acceptance Criteria |
|----------|---------|-------------|----------------------|
| **P1** | **CLI Extraction & Sync** | `locale-flow extract` parses source files (JS/TS, JSON, YAML, PO, etc.) and generates a canonical `messages.pot`. `locale-flow sync` pushes updates to a translation hub (e.g., Crowdin, Lokalise) and pulls completed translations. | • Supports all Axentx‑standard i18n formats.<br>• Idempotent – repeated runs produce no duplicate entries.<br>• Exit code 0 on success, non‑zero on failure. |
| **P1** | **CI/CD Integration Plugin** | A lightweight GitHub Action / GitLab CI job that runs extraction, validates translation completeness, and fails the pipeline if missing strings exceed a threshold. | • Configurable threshold (default 0).<br>• Generates a summary artifact (`locale-report.json`). |
| **P2** | **Translation Status Dashboard** | Web UI (React) that visualizes per‑locale progress, recent changes, and risk indicators (e.g., “stale strings > 7 days”). Auth via SSO. | • Shows real‑time status for all repos linked to locale‑flow.<br>• Exportable CSV report. |
| **P2** | **Quality Gate – Placeholder Detection** | Static analysis that flags common placeholder patterns (`{0}`, `%s`, `{{var}}`) mismatches between source and target strings. | • Fails CI if any placeholder mismatch detected.<br>• Provides line‑level diagnostics. |
| **P3** | **Vendor & In‑House Assignment Engine** | Rules‑based routing of strings to external vendors or internal linguists based on language, domain, or string tag. | • Configurable routing JSON.<br>• Automatic task creation in selected translation platform. |
| **P3** | **Rollback & Versioning** | Store each translation snapshot in Git LFS; allow `locale-flow rollback --version <hash>` to revert to prior state. | • Full audit trail of changes.<br>• No data loss on rollback. |
| **P4** | **Analytics & Cost Reporting** | Aggregate translation spend, word counts, and time‑to‑completion per locale; expose via Grafana dashboards. | • Data refreshed nightly.<br>• Exportable PDF summary. |

---

## 5. Scope  

### In‑Scope  
- Core CLI tool (extraction, sync, validation).  
- CI/CD plugin for GitHub Actions (initially).  
- Basic web dashboard (status view only).  
- Placeholder quality gate.  
- Integration with Crowdin API (as primary translation hub).  
- Documentation, onboarding guides, and sample repo templates.  

### Out‑of‑Scope (Phase 1)  
- Full multi‑vendor orchestration (support for Lokalise, Phrase, etc.).  
- Machine‑translation pre‑fill workflow.  
- Mobile‑specific resource formats (e.g., Android XML, iOS .strings) – deferred to Phase 2.  
- Advanced analytics (predictive spend, AI‑driven quality scoring).  

---

## 6. Assumptions & Dependencies  

| Assumption | Rationale |
|------------|-----------|
| Development teams already use a supported i18n library (e.g., `react-intl`, `i18next`). | Extraction relies on standard patterns. |
| Translation hub (Crowdin) API keys are centrally managed via Axentx secret vault. | Enables secure automation. |
| CI pipelines have network access to the translation hub. | Required for sync step. |
| Existing Axentx BRAIN vector store can host the translation metadata for dashboard queries. | Leverages existing infrastructure. |

**Dependencies**  
- Access to Crowdin Enterprise API (team to provision).  
- GitHub Actions runner environment with Node 20+.  
- Axentx UI component library for dashboard UI.  

---

## 7. Milestones & Timeline  

| Milestone | Deliverable | Owner | Target Date |
|-----------|-------------|-------|-------------|
| **M1 – Foundations** | Repo scaffold, CLI skeleton, unit test framework | Lead Engineer | 2026‑07‑15 |
| **M2 – Extraction & Sync** | Full CLI with support for JS/TS & JSON, Crowdin sync | Engineer + QA | 2026‑08‑31 |
| **M3 – CI/CD Plugin** | GitHub Action, documentation, sample workflow | DevOps Lead | 2026‑09‑15 |
| **M4 – Dashboard MVP** | Status page, auth, basic charts | Frontend Lead | 2026‑10‑15 |
| **M5 – Quality Gate** | Placeholder detection, CI fail integration | QA Lead | 2026‑11‑01 |
| **M6 – Beta Release** | Internal beta to 5 product teams, feedback loop | PM | 2026‑11‑30 |
| **M7 – GA Launch** | Public release, docs site, support hand‑off | PM/Support | 2026‑12‑31 |

---

## 8. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **API rate limits** on Crowdin could block large syncs. | Delayed pipelines. | Implement exponential back‑off & batch processing. |
| **Incorrect placeholder detection** causing false positives. | Unnecessary CI failures. | Provide configurable ignore list; extensive unit tests with real strings. |
| **Team adoption resistance** due to learning curve. | Low usage, missed ROI. | Offer interactive tutorials, embed CLI in existing scripts, champion from early‑adopter teams. |
| **Security of translation assets** (source strings may contain secrets). | Data leakage. | Enforce secret‑masking rules, store only non‑sensitive strings, audit logs. |

---

## 9. Acceptance Criteria (Definition of Done)

- All P1 features implemented, tested (unit + integration), and passing CI on main branch.  
- Documentation covers installation, configuration, CI integration, and troubleshooting.  
- Dashboard deployed to Axentx staging environment, accessible via SSO.  
- Beta feedback collected from ≥ 5 internal teams; ≥ 80 % satisfaction score.  
- Success metrics baseline established and monitoring dashboards configured.  

---  

*Prepared by the Localization Automation team, Axentx.*
