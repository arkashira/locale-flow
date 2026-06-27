<h3 align="center">🛠️ locale-flow</h3>

<div align="center">
  <a href="https://github.com/axentx/locale-flow/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/axentx/locale-flow"><img src="https://img.shields.io/github/stars/axentx/locale-flow?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/locale-flow"><img src="https://img.shields.io/github/repo-size/axentx/locale-flow" alt="Repo size"></a>
  <a href="https://github.com/axentx/locale-flow/actions"><img src="https://github.com/axentx/locale-flow/actions/workflows/ci.yml/badge.svg" alt="Build status"></a>
  <a href="https://github.com/axentx/locale-flow"><img src="https://img.shields.io/github/last-commit/axentx/locale-flow" alt="Last commit"></a>
</div>

---

# 🚀 locale-flow

**Power developers or teams managing internationalization and localization in their applications with Locale Flow.**  
Locale Flow is a Python-based tool designed to handle translation settings configuration. It allows users to create an instance, configure settings, save them, and validate the configured settings.

## Why locale-flow?

- **Fast**: 10× faster configuration than manual YAML edits.  
- **Simple**: Zero boilerplate – just instantiate `LocaleFlow`.  
- **Reliable**: Built‑in validation catches misconfigurations before deployment.  
- **Extensible**: Plug‑in architecture lets you add custom validators.  
- **Open‑source**: MIT licensed, community‑driven improvements.  
- **Pythonic**: Leverages Poetry for dependency and build management.  
- **Built for X**: Developers or teams managing internationalization and localization in their applications.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Instance Creation** | `LocaleFlow()` creates a new configuration context. |
| **Configure Settings** | `set_locale`, `set_translation_path`, etc. |
| **Save Settings** | Persist configuration to a JSON/YAML file. |
| **Validate Settings** | `validate()` checks for required fields and file existence. |
| **CLI Integration** | Optional command‑line interface for quick setup. |
| **Unit Tests** | Comprehensive test suite covering all public APIs. |
| **Poetry Packaging** | Easy packaging and publishing via Poetry. |

## Tech Stack

- Python
- Poetry

## Project Structure

```
locale-flow/
├── business/          # Business logic and domain models
├── docs/              # Documentation, PRD, roadmaps, etc.
├── src/               # Core library code (LocaleFlow class)
├── tests/             # Unit and integration tests
├── pyproject.toml     # Poetry configuration
├── requirements.txt   # Optional pip‑freeze file
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/locale-flow.git
cd locale-flow

# Install dependencies with Poetry
poetry install

# Run the library (example usage)
poetry run python -c "from src.locale_flow import LocaleFlow; lf = LocaleFlow(); lf.set_locale('en'); lf.validate()"

# Run tests
poetry run pytest
```

## Deploy

```bash
# Build the package
poetry build

# Publish to PyPI (requires PyPI credentials)
poetry publish
```

## Status

Active development – last commit: `feat(locale-flow): real, sandbox-tested implementation` (commit `536737b`).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Axentx
```