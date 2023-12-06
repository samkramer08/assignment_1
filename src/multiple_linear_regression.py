import numpy as np
from sklearn.linear_model import LinearRegression

class MultipleLinearRegression:
    def __init__(self, default_intercept: float = 0, default_slope: float = 0):
        self._intercept = default_intercept
        self._slopes = default_slope

    def train(self, X, y):
        Xmean = np.mean(X, axis=0)
        Ymean = np.mean(y)

        # equation to find slope and intercept (b)
        self._slopes = np.linalg.inv(X.T @ X) @ X.T @ y
        self._intercept = Ymean - np.sum(Xmean * self._slopes)

    def predict(self, X):
        # Add a column of ones to X matrix for the intercept term
        X_matrix_with_ones = np.column_stack((np.ones(X.shape[0]), X))
        
       # Insert intercept at the beginning of the slopes array
        slopes = np.insert(self._slopes, 0, self._intercept)

        # find predictions by multiplying matrix with ones slopes
        predictions = X_matrix_with_ones @ slopes
        return predictions

if __name__ == "__main__":
    # generate random training data
    np.random.seed(42)
    x_train = np.random.rand(100, 3)
    y_train = 2 * x_train[:, 0] + 3 * x_train[:, 1] - 5 * x_train[:, 2] + np.random.randn(100)

    # Training our own model
    MLR = MultipleLinearRegression()
    MLR.train(x_train, y_train)

    # Train scikit-learn model
    SKL = LinearRegression()
    SKL.fit(x_train, y_train)

    # Generate random testing data
    x_test = np.random.rand(10, 3)

    # Predictions made with our model
    MLR_predictions = MLR.predict(x_test)

    # Predictions made with scikit-learn model
    SKL_predictions = SKL.predict(x_test)

    # Compare predictions
    print("Our Model Predictions:", MLR_predictions)
    print("Scikit-learn Model Predictions:", SKL_predictions)







