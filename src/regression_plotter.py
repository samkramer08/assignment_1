import numpy as np
import matplotlib.pyplot as plt

class RegressionPlotter:
    def __init__(self, data):
        self.data = data

    def plotter(self, target, features):
        features = list(self.data.columns)
        features.remove(target)
        num_features = len(features)

        if num_features == 1:
            x = self.data[features[0]]
            y = model.predict(self.data)

            plt.scatter(x, self.data[target], label='Data')
            plt.plot(x, y, color='red', label='Regression')
            plt.xlabel('Feature')
            plt.ylabel('Target')
            plt.legend()
            plt.show()
            
        elif num_features == 2:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            x = self.data[features[0]]
            y = self.data[features[1]]
            z = model.predict(self.data)

            ax.scatter(x, y, self.data[target], label='Data')
            ax.plot_trisurf(x, y, z, color='red', alpha=0.5, label='Regression')
            ax.set_xlabel(features[0])
            ax.set_ylabel(features[1])
            ax.set_zlabel(target)
            ax.legend()
            plt.show()

        else: 
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

if __name__ == "__main__":

    # Define model and features
    model = RegressionPlotter
    features = features...

    # Initialize and set data for the plotter
    plotter = RegressionPlotter(data=your_data)
    plotter.set_data(your_data)

    # Call the plotter method with target and features
    plotter.plotter(target='your_target', features=features)
