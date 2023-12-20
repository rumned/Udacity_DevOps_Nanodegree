# #!/usr/bin/env python3

# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""

import random
import time


def typewriter_simulator(message):
    for char in message:
        print(char, end='')
        time.sleep(.03)
    print('')


def print_pause(message):
    typewriter_simulator(message)
    time.sleep(0.5)


moves = ['rock', 'paper', 'scissors']

# while rounds >= 0:
#     rounds = int(input("How many rounds do you want to play?"))
#     if rounds < 0:
#         rounds = 3

# """The Player class is the parent class for all of the Players
# in this game"""

p1_score = 0
p2_score = 0
round_count = 0
reflect_my_move = []

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass

class ReflectPlayer(Player):
    def move(self):
       if reflect_my_move == []:
           return random.choice(moves)
       else:
           return reflect_my_move[0]

# trying to make this function return the move, 
# and make move function above to access the value
    def learn(self, my_move, their_move):
        if reflect_my_move == []:
            reflect_my_move.append(their_move)
        else:
            reflect_my_move[0] = their_move
    
class CyclePlayer(Player):
    def move(self):
        if round_count == 0:
            return moves[0]
        elif round_count == 1:
            return moves[1]
        elif round_count == 2:
            return moves[2]
        elif round_count % 3 == 0:
            return moves[0]
        elif round_count % 3 == 1:
            return moves[1]
        elif round_count % 3 == 2:
            return moves[2]
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        human_moves = ['rock', 'paper', 'scissors']
        while True:
            try:
                human_move = int(input("Rock, Paper, or Scissors?\n"
                                       "Type 1 for Rock, 2 for Paper,"
                                       "3 for Scissors.\n"))
            except ValueError:
                print_pause("Please only type the numbers.")
                continue

            if human_move == 1:
                return human_moves[0]
            elif human_move == 2:
                return human_moves[1]
            elif human_move == 3:
                return human_moves[2]


# def beats(one, two):
#     return ((one == 'rock' and two == 'scissors') or
#             (one == 'scissors' and two == 'paper') or
#             (one == 'paper' and two == 'rock'))
# # p1_score += 1

# def beaten(one, two):
#     return ((one == 'scissors' and two == 'rock') or
#             (one == 'rock' and two == 'paper') or
#             (one == 'paper' and two == 'scissors'))
# p2_score += 1

class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)  # line does nothing bcs human always p1
        self.p2.learn(move2, move1)
        if (move1 == "rock" and move2 == "scissors"
                or move1 == "scissors" and move2 == "paper"
                or move1 == "paper" and move2 == "rock"):
            print("Player 1 wins!")
            global p1_score
            p1_score += 1
        elif (move1 == "rock" and move2 == "paper"
              or move1 == "paper" and move2 == "scissors"
              or move1 == "scissors" and move2 == "rock"):
            print("Player 2 wins!")
            global p2_score
            p2_score += 1
        elif move1 == move2:
            print("Tie!")
        else:
            print("Not valid...")
        print(f"Player 1 score:{p1_score}")
        print(f"Player 2 score:{p2_score}")
        # if beats == True and beaten == False:
        #     print("Player 1 won!")
        # elif beats == False and beaten == True:
        #     print("Player 2 won!")
        # else:
        #     print("Tie")

    def play_game(self):
        print_pause("Game start!")
        how_many_rounds = 1 # default round so code doesnt crash
        try:
            how_many_rounds = int(input("How many rounds do you want to play?\n"))
        except ValueError:
            print_pause("Please only type numbers.")
        for round in range(how_many_rounds):  # add user input to set rounds
            print_pause(f"Round {round+1}:")
            self.play_round()
            global round_count
            round_count += 1
        print("Game over!")
        if p1_score > p2_score:
            print("Player 1 wins!")
        elif p2_score > p1_score:
            print("Player 2 wins!")
        elif p1_score == p2_score:
            print("It is a tie!")
        else:
            print("Thanks for playing!")
        print("The final score is...\n")
        print(f"Player 1 score:{p1_score}")
        print(f"Player 2 score:{p2_score}")
        print("\n")
        print_pause("Thanks for playing!\n")


if __name__ == '__main__':
    # game = Game(Player(), RandomPlayer())
    # game.play_game()
    # p1_score = 0
    # p2_score = 0
    # round_count = 0
    # game = Game(HumanPlayer(), RandomPlayer())
    # game.play_game()
    # p1_score = 0
    # p2_score = 0
    # round_count = 0
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
    # p1_score = 0
    # p2_score = 0
    # round_count = 0
    # game = Game(HumanPlayer(), CyclePlayer())
    # game.play_game()
