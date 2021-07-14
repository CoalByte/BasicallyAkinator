import json


def most_frequent(data):
    return max(set(data), key=data.count)


class BasicallyAkinator:
    def __init__(self, dataset_path="dataset.json", on_guessed=None):
        self.data = json.loads(open(dataset_path, "r").read())
        self.guessed = None
        
        self._event = on_guessed

    def next(self, input_function=input, print_options=True):
        options = [s for value in self.data.values() for s in value.keys()]
        possible_options = [self.data[key][most_frequent(options)] for key in self.data.keys() if self.data[key][
            most_frequent(options)]]

        if print_options is True:
            print("Answer options:", ', '.join(possible_options))
        data1 = input_function(
            f"Is/Are/Can your character('s)/object('s) {most_frequent(options)}? ")

        for key in [key for key in self.data.keys() if self.data[key][most_frequent(
                options)] != data1]:
            del self.data[key]

        for key in [key for key in self.data.keys() if self.data[key][most_frequent(options)]]:
            self.data[key].pop(most_frequent(options))

        if self.is_done() is True:
            self.guessed = list(self.data.keys())[0]
            if str(type(self._event)).find("function") != -1:
                self._event(self.guessed)

    @property
    def is_done(self):
        return True if self.data.__len__() == 1 else False
