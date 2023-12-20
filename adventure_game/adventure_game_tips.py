Default delay

Here you can add a default delay, for example:

def print_pause(message, delay=0):
    print(message)
    time.sleep(delay)


print_pause("Quick message")
print_pause("Delayed message", 5)

Typing simulator

How about making your text simulate typing? :wink:

import string

def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print('')


def print_pause(message, delay=1):
    typewriter_simulator(message)
    time.sleep(delay)

TIP
Text color

How about making your text colorful? :wink:

import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
         orange = '\033[33m'
         yellow = '\033[93m'
    bold = '\033[1m'
    underline = '\033[4m'
    black = '\033[0m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)

Note: It doesn't work well in Windows, though.
For Windows Operating System, use the Colorama package:
https://pypi.org/project/colorama/

Random methods (choice or randint) triggered on every round :white_check_mark:

You are using the random function to select random things. Very fine!

Another excellent place to call the random function for the next round is inside the play again function.

Example:

things = ["a", "b", "c"]
# initial random thing <------------
thing = random.choice(things)


def play_again():
    choice = valid_input("Play again?" ['y', 'n'])
    if choice == "y":
        # next round random thing <------------
        global thing
        thing = random.choice(things)

Read more about the Python random module and global variables:
https://www.w3schools.com/python/ref_random_choices.asp
https://www.w3schools.com/python/python_variables_global.asp

def play_game():

    # Infinite loop
    while True:
        # go to map X
        # break if the case

        # go to map Y
        # break if pertinent

        # go to map Z
        # break if applicable


def play_again():
    choice = valid_input("Play again? [y|n]", ['y', 'n'])
    if choice == 'n':
        print('Thanks for playing! Goodbye!')
        exit(0)


def game():

    # Infinite loop.
    while True:

        # All logic to play.
        play_game()

        # The stop condition.
        play_again()


if __name__ == '__main__':
    game()