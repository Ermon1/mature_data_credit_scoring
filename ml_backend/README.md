# ML Backend

Credit scoring ML pipeline and serving API.

## Folders

- `src/component/` — Individual pipeline steps (ingestion, transformation, training, evaluation)
- `src/pipeline/` — Orchestrates components into full workflows
- `src/utility/` — Shared helpers (logging, config loading)
- `app/` — FastAPI application for model serving
- `config/` — YAML configuration files
- `data/` — Raw and processed datasets (not tracked in Git)
- `models/` — Saved model artifacts (not tracked in Git)
- `notebook/` — Jupyter notebooks for EDA
- `tests/` — Unit and integration tests
