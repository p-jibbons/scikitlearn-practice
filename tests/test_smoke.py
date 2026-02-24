from sklearn.metrics import r2_score

from scikitlearn_practice import fit_linear_regression


def test_linear_regression_smoke() -> None:
    x = [[1.0], [2.0], [3.0], [4.0]]
    y = [2.0, 4.0, 6.0, 8.0]

    model = fit_linear_regression(x, y)
    predictions = model.predict(x)

    assert r2_score(y, predictions) > 0.99
