# STORIES.md  

## Project: locale‑flow  
**Goal:** Build an end‑to‑end, automated translation pipeline that lets development teams ship localized software faster, with minimal manual effort and high quality assurance.

---

## Epics & Ordered MVP Backlog  

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Core Translation Pipeline** | Detect source changes, extract translatable strings, send to a translation provider, receive and merge translations. | ✅ |
| **E2 – CI/CD Integration** | Hook the pipeline into existing CI/CD workflows (GitHub Actions, GitLab CI, Jenkins). | ✅ |
| **E3 – Configuration & Project Management** | Define locales, providers, and rules via a declarative config file. | ✅ |
| **E4 – UI Dashboard** | Web UI for monitoring runs, reviewing translations, and managing overrides. | ⬜ |
| **E5 – Quality & Validation** | Automatic linting, placeholder checks, and post‑merge validation. | ⬜ |
| **E6 – Access Control & Auditing** | Role‑based permissions and audit logs for translation actions. | ⬜ |
| **E7 – Extensibility (Plugins)** | Plugin system for custom extractors, providers, and post‑processing steps. | ⬜ |
| **E8 – Documentation & Testing** | Comprehensive docs, example projects, and automated test suite. | ⬜ |

> **MVP** = all stories under **E1–E3** (the first three epics). Stories in later epics are planned for subsequent releases.

---

## User Stories  

### **Epic E1 – Core Translation Pipeline**

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E1‑01** | **As a developer, I want locale‑flow to automatically detect changed source files in a pull request, so that I only translate what actually changed.** | - Detects added/modified files matching `*.js`, `*.ts`, `*.py`, `*.json`, `*.yaml`.<br>- Generates a list of changed files within 30 seconds of PR creation.<br>- Emits a `locale-flow:changes` event with file paths. |
| **E1‑02** | **As a developer, I want locale‑flow to extract translatable strings from the changed files, so that I don’t have to manually maintain resource files.** | - Supports extraction for i18n libraries: `react‑i18next`, `gettext`, `formatjs`.<br>- Produces a `.pot`/`.json` file per locale target.<br>- Handles plural forms and ICU message syntax.<br>- Extraction runs deterministically (same input → same output). |
| **E1‑03** | **As a product manager, I want locale‑flow to send extracted strings to a configured translation provider (e.g., DeepL, Google Translate, or a custom TM), so that translations are generated automatically.** | - Provider credentials stored securely via env vars or secret manager.<br>- API call respects rate limits and retries on transient failures.<br>- Returns translations in the provider’s native format and maps them back to source keys. |
| **E1‑04** | **As a developer, I want locale‑flow to merge received translations back into the project’s locale files, so that the codebase stays up‑to‑date.** | - Merges translations preserving existing manual overrides.<br>- Creates a PR (or commit) with a clear title `locale‑flow: update <locale>`.<br>- Fails the pipeline if any key is missing after merge. |
| **E1‑05** | **As a QA engineer, I want locale‑flow to generate a diff report of added/updated translations, so that I can review changes before they go live.** | - Generates a markdown/HTML report listing added, updated, and unchanged keys per locale.<br>- Report attached as an artifact to the CI run and posted as a comment on the PR. |
| **E1‑06** | **As a DevOps engineer, I want locale‑flow to be runnable as a Docker container with a single command, so that it can be used in any environment.** | - Docker image published to `ghcr.io/arkashira/locale-flow`.<br>- `docker run --rm -v $(pwd):/repo -e CONFIG=/repo/locale-flow.yml locale-flow run` works out‑of‑the‑box.<br>- Image size < 300 MB and starts in < 5 seconds. |

### **Epic E2 – CI/CD Integration**

| # | Story | Acceptance Criteria |
|---|-------|----------------------|
| **E2‑01** | **As a developer, I want a ready‑made GitHub Action, so that I can add locale‑flow to my workflow with minimal configuration.** | - Action `arkashira/locale-flow@vX` accepts inputs: `config-path`, `provider-secret`.<br>- Action runs on `pull_request` and `push` events.<br>- Action fails the job if any pipeline step fails. |
| **E2‑02** | **As a DevOps engineer, I want locale‑flow to expose exit codes for success, partial‑success, and failure, so that CI pipelines can react appropriately.** | - Exit code `0` = all translations merged successfully.<br>- Exit code `1` = extraction or provider error.<br>- Exit code `2` = validation errors (e.g., missing placeholders). |
| **E2‑03** | **As a developer, I want locale‑flow to cache extracted strings between runs, so that unchanged strings are not re‑sent to the provider.** | - Cache stored in `.locale-flow/cache` and keyed by file hash.<br>- Cache is restored on subsequent runs within the same CI job.<br>- Cache invalidates correctly when source files change. |
| **E2‑04** | **As a release manager, I want locale‑flow to emit
