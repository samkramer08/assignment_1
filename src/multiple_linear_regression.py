import numpy as np
from sklearn.linear_model import LinearRegression

class MultipleLinearRegression:
    def __init__(self, default_intercept: float = 0, default_slope: float = 0):
        self._intercept = default_intercept
        self._slopes = default_slope

    def train(self, X, y):
        Xmean = np.mean(X, axis=0)
        Ymean = np.mean(y)

        self._slopes = np.linalg.inv(X.T @ X) @ X.T @ y
        self._intercept = Ymean - np.sum(Xmean * self._slopes)

    def predict(self, X):
        X_matrix_with_ones = np.column_stack((np.ones(X.shape[0]), X))
        predictions = X_matrix_with_ones @ np.insert(self._slopes, 0, self._intercept)
        return predictions

if __name__ == "__main__":
    np.random.seed(42)
    X_train = np.random.rand(100, 3)
    y_train = 2 * X_train[:, 0] + 3 * X_train[:, 1] - 5 * X_train[:, 2] + np.random.randn(100)


    our_model = MultipleLinearRegression()
    our_model.train(X_train, y_train)

    sklearn_model = LinearRegression()
    sklearn_model.fit(X_train, y_train)

    X_test = np.random.rand(10, 3)
    
    our_model_predictions = our_model.predict(X_test)


    sklearn_predictions = sklearn_model.predict(X_test)

    print("Our Model Predictions:", our_model_predictions)
    print("Scikit-learn Model Predictions:", sklearn_predictions)

    assert np.allclose(our_model_predictions, sklearn_predictions), "Predictions do not match!"
