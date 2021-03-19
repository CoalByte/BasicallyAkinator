# BasicallyAkinator
![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Basically Akinator, written in Python.

This is a program based on [Akinator](https://en.akinator.com/), which basically guesses who/what you are thinking about based on some key characteristics.

Every line has a comment explaining what it does If you don't really get how the code works.

## **Examples:**
![image](https://user-images.githubusercontent.com/62639622/111640674-50a9b000-87f4-11eb-9006-424e6e021795.png)


## **BasicallyAkinator Library:**

If you want to use a more flexible version of this program, I included a file named `lib.py` with a class that does the same thing as the `main.py` file, without the external loop. This can be useful if you're trying to use it with a third party software or just adding it into a section of your code effortlesly.

```python
import lib

guess = lib.BasicallyAkinator()

while guess.is_done() is False: 
  guess.next()

print(guess.guessed)
```

#### Functions:
`lib.BasicallyAkinator().is_done()`: returns a boolean if it has guessed the item.

`lib.BasicallyAkinator().next(input_function=input, print_options=True)`: goes to the next question and does all the processing for that one.

- **input_function:** Function that will be executed to fetch the input, has to have 1 argument for the prompt and has to return data inputed as a string.

- **print_options:** Boolean argument, print the answer options you have or not

`lib.BasicallyAkinator().guessed`: the item It has guessed, if it hasn't been guessed it's equal to None




## **Contributions:**

Feel free to contribute to this project as It's pretty new, open a request and I'Il merge it if It looks good.
