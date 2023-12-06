import pickle
import csv

class ModelSaver:
    def _init_(self, model=None, format_type='pickle'):
        self.__model = model
        self.format_type = format_type

    def save_params(self, model, filename): # saves parameters of a model to a file
        if self.format_type == 'pickle':
            with open(filename, 'wb') as file:
                pickle.dump(model.get_params(), file)
        elif self.format_type == 'csv':
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(model.get_params().items())
        else:
            raise ValueError(f"{self.format_type} not supported") # value error to account for other format types

    def load_params(self, model, filename): # loads parameters from a file
        if self.format_type == 'pickle':
            with open(filename, 'rb') as file:
                parameters = pickle.load(file)
        elif self.format_type == 'csv':
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                parameters = dict(reader)
        else:
            raise ValueError(f"{self.format_type} not supported") # value error to account for other format types

        model.set_params(parameters) # set parameters from file into model
