# Credit Scoring ML Project

End-to-end ML/MLOps pipeline for predicting credit default risk using mature historical data.

## Overview

This project builds a production-grade credit scoring model that:
- Ingests and validates raw credit data
- Engineers features for default prediction
- Trains and evaluates ML models (XGBoost, Logistic Regression)
- Serves predictions via a REST API
- Tracks experiments with MLflow
- Monitors for data and concept drift (future)

## Project Structure

- `.github/workflows/` — CI/CD pipelines
- `docker-compose.yml` — Service orchestration
- `ml_backend/` — ML service (training, serving, data)

## Setup

1. `cd ml_backend`
2. `python -m venv .venv`
3. `.venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `pip install -e .`
