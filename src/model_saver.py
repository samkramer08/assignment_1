import pickle
import json

class ModelSaver:
    def __init__(self, format_type='pickle'): # default format (pickle)
        self.format_type = format_type

    def save(self, model, filename): # dont know what the filename is supposed to be 
        if self.format_type == 'pickle':
            with open(filename, 'wb') as file:
                pickle.dump(model.get_params(), file)
        elif self.format_type == 'json':
            with open(filename, 'w') as file:
                json.dump(model.get_params(), file)
        else:
            pass

    def load(self, model, filename):
        if self.format_type == 'pickle':
            with open(filename, 'rb') as file:
                parameters = pickle.load(file)
        elif self.format_type == 'json':
            with open(filename, 'r') as file:
                parameters = json.load(file)
        else:
            pass




