import numpy as np
import matplotlib.pyplot as plt 

class regression_plotter:
    def __init__(self, data):
        self.data = None

    def set_data(self, data):
        self.data = data

    def one_feature_plot(self, data, feature, target):
        x = self.datap[feature]
        y = model.predict(self.data)

        plt.scatter(x, self.data[target], label='Data')
        plt.plot(x, y_pred, color='red', label='Regression')
        plt.xlabel = 'Feature'
        plt.ylabel = 'Target'
        plt.legend()
        plt.show()

    def two_feautres_plot(self, data, feature_one, feature_two, target):
        fig = plt.figure()
        ax = fig.add_subplot(111, projecten='3D')

        x = self.data[feature_one]
        y = self.data[feature_two]
        z = model.predict(self.data)

        ax.scatter(x, y, self.data[target], label='Data')
        ax.plot_trisurf(x, y, z, color='red', alpha=0.5, label='Regression')
        ax.set_xlabel(feature_one)
        ax.set_ylabel(feature_two)
        ax.set_zlabel(target)
        ax.legend()
        plt.show()

    def multiple_features_plot(self, data, target):
        features = list(self.data.columns)
        features.remove(target)

        num_features = len(features)

        fig, axes = plt.subplots(num_features, 1, figsize=(8, 4 * num_features), sharey=True)

        for i, feature in enumerate(features):
            x = self.data[feature]
            y = model.predict(self.data)

            axes[i].scatter(x, self.data[target], label='Actual data')
            axes[i].plot(x, y, color='red', label='Regression')
            axes[i].set_xlabel(feature)
            axes[i].set_ylabel(target)
            axes[i].legend()

        plt.tight_layout()
        plt.show()
