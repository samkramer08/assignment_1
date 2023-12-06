from multiple_linear_regressions import MultipleLinearRegression
from model_saver import ModelSaver
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from reg_plotter import RegressionPlotter
from sklearn.metrics import mean_squared_error

if __name__ == "__main__":
    model = MultipleLinearRegression()
    ms = ModelSaver(format_type='csv')
    ms.save_params(model, 'diabetes_dataset.csv')
    ms.load_params(model, 'diabetes_dataset.csv')

    data = load_diabetes(return_X_y=True)
    x, y = data

    # split data into training and testing data
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # train model
    model.train(x_train, y_train)

    # make prediction
    y_pred = model.predict(x_test)

    # mean squared error to compare predictions to ground truth
    meanSqError = mean_squared_error(y_test, y_pred)

    plotter = RegressionPlotter(data={'feature': x_test[:, 0], 'target': y_test})  # Using the first feature for simplicity
    plotter.plotter(target='target', features=['feature'])

    
