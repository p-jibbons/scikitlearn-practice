"""Reusable model helpers for learning workflows."""

from __future__ import annotations

from sklearn.linear_model import LinearRegression


def fit_linear_regression(features: list[list[float]], targets: list[float]) -> LinearRegression:
    """Train and return a simple linear regression model."""
    model = LinearRegression()
    model.fit(features, targets)
    return model
