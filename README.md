# Scikit-Learn Practice

This repository has two goals:

1. Build practical scikit-learn proficiency through a structured, hands-on learning path.
2. Serve as a portfolio artifact that demonstrates technical depth, code quality, and clean repo management.

## Audience

- Primary: personal learning and skill development.
- Secondary: recruiters/hiring managers reviewing project quality and consistency.

## Project Style

This repo is a mix of:

- small focused notebooks for exploration and learning,
- scripts/modules for reusable code,
- tests and documentation to show production-minded engineering habits.

## Setup

Python version: `3.13.7` (pinned in `.python-version`).

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Daily Workflow

```powershell
.\.venv\Scripts\Activate.ps1
git pull
# do focused work for the day
git add .
git commit -m "Day XX: <topic>"
git push
```

## Repository Structure (Planned)

```text
scikitlearn-practice/
  README.md
  WORKLOG.md
  requirements.txt
  notebooks/
  src/
  tests/
  data/
```

## 6-Week Scikit-Learn Roadmap

The working plan is one focused commit per day, tracked in Git history.

### Week 1: Fundamentals and Workflow

- Day 1: scikit-learn API basics (`fit`, `transform`, `predict`)
- Day 2: train/test split and evaluation basics
- Day 3: preprocessing fundamentals
- Day 4: pipelines and reproducible workflows
- Day 5: cross-validation basics
- Day 6: metrics for regression and classification
- Day 7: weekly recap and cleanup commit

### Week 2: Core Supervised Models

- Day 8: linear regression and regularization
- Day 9: logistic regression
- Day 10: k-nearest neighbors
- Day 11: decision trees
- Day 12: random forests
- Day 13: support vector machines
- Day 14: weekly recap and model comparison summary

### Week 3: Model Tuning and Validation

- Day 15: grid search
- Day 16: randomized search
- Day 17: feature scaling strategy comparison
- Day 18: feature selection basics
- Day 19: class imbalance handling
- Day 20: error analysis patterns
- Day 21: weekly recap and reproducibility checks

### Week 4: Unsupervised Learning

- Day 22: k-means clustering
- Day 23: hierarchical clustering
- Day 24: DBSCAN
- Day 25: PCA dimensionality reduction
- Day 26: t-SNE/UMAP exploration notes
- Day 27: cluster validation techniques
- Day 28: weekly recap and visual summary

### Week 5: End-to-End Mini Projects

- Day 29: project 1 problem framing + dataset selection
- Day 30: project 1 baseline model
- Day 31: project 1 feature engineering + tuning
- Day 32: project 1 evaluation + write-up
- Day 33: project 2 problem framing + baseline
- Day 34: project 2 iteration and improvement
- Day 35: weekly recap and portfolio cleanup

### Week 6: Portfolio Polish and Engineering Quality

- Day 36: refactor notebook logic into reusable `src/` code
- Day 37: add/expand tests
- Day 38: improve documentation and examples
- Day 39: add lint/format/test automation
- Day 40: final model cards or experiment summaries
- Day 41: portfolio narrative and repo presentation pass
- Day 42: final retrospective and next-step roadmap

## Definition of Progress

Each day should leave at least one of the following:

- a meaningful code change,
- a reproducible notebook output,
- improved documentation/tests,
- a commit message that clearly explains what changed and why.

