import pickle
import csv

class ModelSaver:
    def __init__(self, model=None, format_type='pickle'):
        self.__model = model
        self.format_type = format_type

    def save_params(self, filename):
        # open file in pickle format writer binary, get model params and write them on a file
        if self.format_type == 'pickle':
            with open(filename, 'wb') as file:
                pickle.dump(self.__model.get_params(), file) 
        # open file in csv format writer, convert to list get params, write a single row in the csv file
        elif self.format_type == 'csv':
            with open(filename, 'w', newline='') as file:
                csv_w = csv.writer(file)
                params_w = list(self.__model.get_params().items())
                csv_w.writerow(params_w) 

        else:
            raise ValueError(f"{self.format_type} not supported")

    def load_params(self, filename):
        if self.format_type == 'pickle':
            # Open  file in pickle binary read
            with open(filename, 'rb') as file:
                # Load the object from  file
                params_r = pickle.load(file)
        elif self.format_type == 'csv':
            # open file in csv read
            with open(filename, 'r') as file:
                # make reader
                csv_r = csv.reader(file)
                # store each row as a list in a list
                params_rows = [row for row in csv_r]
                # If you want each row as a NumPy array
                params_r = [np.array(row, dtype=float) for row in params_rows]
        else:
            raise ValueError(f"{self.format_type} not supported")

        # set the parameters of the model to the saved and loaded parameters
        self.__model.set_params(params_r)
