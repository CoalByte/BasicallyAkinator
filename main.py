import json


data = json.loads(open("dataset.txt", "r").read())

most_frequent = lambda List: max(set(List), key=List.count)

while data.__len__() != 1:
    options = [s for value in data.values() for s in value.keys()]

    possible_options = [data[key][most_frequent(options)] for key in data.keys() if data[key][most_frequent(options)]]

    print("Answer options:", ', '.join(possible_options))
    data1 = input(f"What/where is/are your character('s) {most_frequent(options)}? ")

    for key in [key for key in data.keys() if data[key][most_frequent(options)] != data1]:
        del data[key]


print("You guessed", list(data.keys())[0])
