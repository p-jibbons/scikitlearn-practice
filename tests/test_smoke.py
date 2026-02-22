from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def test_linear_regression_smoke() -> None:
    x = [[1], [2], [3], [4]]
    y = [2, 4, 6, 8]

    model = LinearRegression()
    model.fit(x, y)
    predictions = model.predict(x)

    assert r2_score(y, predictions) > 0.99
