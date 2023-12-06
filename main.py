from src.multiple_linear_regression import MultipleLinearRegression
from src.model_saver import ModelSaver
from sklearn.datasets import load_diabetes
from src.regressrion_plotter import regressrion_plotter

if __name__ == "__main__":
	model = MultipleLinearRegression()
	ms = model_saver(format_type='csv')
	ms.save_params(model, 'diabetet_dataset.csv')
	ms.load_params(model, 'diabetes_dataset.csv')

	data = sklearn.datasets.load_diabetes(return_X_y=True)
	x, y = data

	#split data into training and testing data
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

	# train model
	model.fit(x_train, y_train)

	#make prediction
	y_pred = model.predict(x_test)

	# mean squared error to compare predictions to grownd truth
	meanSqError = mean_squared_error(y_test, y_pred)

  # using regression plotter to visualyze results
	plotter = RegressionPlotter()
	plotter.set_data({'feature': x_test[:, 0], 'target': y_test}) 
	plotter.plot(model, features=['feature'])


