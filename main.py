import json


data = json.loads(open("dataset.txt", "r").read()) # Open and load dataset as a dictionary

most_frequent = lambda data: max(set(data), key=data.count) # Define a function to get the most common value out of a list

while data[:-1]: # Loop (equivallent to while data.__len__() != 1)
    options = [s for value in data.values() for s in value.keys()] # Get all characteristics
    possible_options = [data[key][most_frequent(options)] for key in data.keys() if data[key][most_frequent(options)]] # Get all different values for the characteristic with most instances in "options"

    print("Answer options:", ', '.join(possible_options)) # Print the possible options
    data1 = input(f"What/where is/are your character('s) {most_frequent(options)}? ") # Get data for the option we are asking about

    for key in [key for key in data.keys() if data[key][most_frequent(options)] != data1]: # Get every option with a value that doesn't match the value we have been given
        del data[key] # Remove that option


print("You guessed", list(data.keys())[0]) # Print the remaining option
