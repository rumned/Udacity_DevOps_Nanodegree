# #!/usr/bin/env python3

# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

# """The Player class is the parent class for all of the Players
# in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

def learn(self,my_move,their_move):
    pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def beaten(one, two):
    return ((one == 'scissors' and two == 'rock') or
            (one == 'rock' and two == 'paper') or
            (one == 'paper' and two == 'scissors'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def keep_score(self):
        if beats == True and beaten == False:
            print("Player 1 won!")
        elif beats == False and beaten == True:
            print("Player 2 won!")
        else:
            print("Tie")

    def play_game(self):
        print("Game start!")
        for round in range(10):
            print(f"Round {round}:")
            self.play_round()
            self.keep_score()
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
