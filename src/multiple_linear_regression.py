import numpy as np

class MultipleLinearRegression:
    def __init__(self, default_intercept:float = 0, default_slope:float= 0):
        self._intercept = default_intercept
        self._slope = default_slope

    def train(self,X, y):
        Xmean = np.mean(X, axis=0)
        Ymean = np.mean(y)

        # using closed-form solution 
        p = 
        n = 

        self._slopes = np.linalg.inv(X.T @ X) @ X.T @ y
        self._intercept = Ymean - np.sum(Xmean * self.slopes)

        #account for intercept (add row of 1's)
        X_matrix_with_ones = np.column_stack((np.ones(X.shape[0]), X))

        self.w = np.linalg.inv(X_matrix_with_ones.T @ X_matrix_with_ones) @ X_matrix_with_ones.T @ y

    def predict(self, X):
        predictions = X_matrix_with_ones @ self.w
        return predictions



   


if __name__ == "__main__":
