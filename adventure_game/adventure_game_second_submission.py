import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("Welcome player!")
    print_pause("You are in a strange land full of adventure!")
    print_pause("Well, not really, since it's my first python adventure game,")
    print_pause("But I hope you will enjoy!")
    print_pause("You wake up, still feeling disoriented."
                "You look around and you find"
                " 2 magical creatures in front of you.")


def adventure():
    print_pause("With your chosen companion,"
                "you roam through the land,")
    print_pause("in search of quests to prove your worth.")
    print_pause("Suddenly, you feel warmth in the air."
                "At first it was pleasant,")
    print_pause("But, it grows hotter, and hotter, and hotter,")
    print_pause("you hear a deep drawl behind you...")


def first_stage(items):
    items.append("cat")
    print_pause("You have chosen a cat.")
    adventure()
    boss_fight(items)


def second_stage(items):
    items.append("dog")
    print_pause("You have chosen a dog.")
    adventure()
    boss_fight(items)


def change_stage(items):
    print_pause("Please enter the number for the "
                "animal you want to take on your journey:")
    animal = input("1. Cat\n"
                   "2. Dog\n")
    if animal == '1':
        first_stage(items)
    elif animal == '2':
        second_stage(items)
    else:
        change_stage(items)


def boss_fight(items):
    coin = ["Heads", "Tails", "Middle"]
    hit_count = 0
    hp = 3

    def skill_check():
        print(attack)
        print(accuracy)
        print(hit_count)
        print(hp)

    print_pause("There's a dragon attacking you!")
    print_pause("You have to fight now!")
    print_pause("You attack the dragon!")
    if "cat" in items:
        while hit_count < 4 and hp > 0:
            attack = random.randrange(2, 6)
            accuracy = "Heads"
            skill_check()
            if attack >= 4 or accuracy == "Heads":
                print_pause("You have hit the dragon!")
                print_pause("The dragon attacks back,"
                            "but you gallantly parry the attack!")
                hit_count += 1
            elif hp == 0:
                print_pause("With all your might, you launched"
                            " a blinding fast attack from downwards...")
                print_pause("But the dragon saw it,"
                            "and blasted you with its fire...")
                print_pause("You have lost.")
                game_over = input("Do you want to play the game again?\n"
                                  "Type yes if you want to play,"
                                  "anything else to exit.").lower()
                if "yes" == game_over:
                    play_game()
            else:
                print_pause("You tried to strike, but the dragon...")
                print_pause("Parried your attack"
                            "and slammed you to the ground!")
                print_pause("You have been hit!")
                hp -= 1
                if hp == 0:
                    print_pause("With all your might, you launched"
                                "a blinding fast attack from downwards...")
                    print_pause("But the dragon saw it,"
                                "and blasted you with its fire...")
                    print_pause("You have lost.")
                    game_over = input("Do you want to play the game again?\n"
                                      "Type yes if you want to play,"
                                      "anything else to exit.").lower()
                    if "yes" == game_over:
                        play_game()
        if hit_count == 4:
            print_pause("With all your might, you launched"
                        " a blinding fast attack from upwards...")
            print_pause("and you sliced off the dragon's wings!")
            print_pause("As he writhed in pain, you took advantage"
                        " and lunge straight at his head...")
            print_pause("You have slayed the dragon!")
            game_over = input("Do you want to play the game again?\n"
                              "Type yes if you want to play,"
                              "anything else to exit.").lower()
            if "yes" == game_over:
                play_game()
    elif "dog" in items:
        while hit_count < 4 and hp > 0:
            attack = random.randrange(4, 6)
            accuracy = random.choice(coin)
            skill_check()
            if attack >= 4 or accuracy == "Heads":
                print_pause("You have hit the dragon!")
                print_pause("The dragon attacks back,"
                            "but you gallantly parry the attack!")
                hit_count += 1
            elif hp == 0:
                print_pause("With all your might, you launched"
                            " a blinding fast attack from downwards...")
                print_pause("But the dragon saw it,"
                            "and blasted you with its fire...")
                print_pause("You have lost.")
                game_over = input("Do you want to play the game again?\n"
                                  "Type yes if you want to play,"
                                  "anything else to exit.").lower()
                if "yes" == game_over:
                    play_game()
            else:
                print_pause("You tried to strike, but the dragon...")
                print_pause("Parried your attack"
                            "and slammed you to the ground!")
                print_pause("You have been hit!")
                hp -= 1
                if hp == 0:
                    print_pause("With all your might,"
                                "you launched a blinding"
                                " fast attack from downwards...")
                    print_pause("But the dragon saw it,"
                                "and blasted you with its fire...")
                    print_pause("You have lost.")
                    game_over = input("Do you want to play the game again?\n"
                                      "Type yes if you want to play,"
                                      "anything else to exit.").lower()
                    if "yes" == game_over:
                        play_game()
            if hit_count == 4:
                print_pause("With all your might,"
                            "you launched a blinding"
                            "fast attack from upwards...")
                print_pause("and you sliced off the dragon's wings!")
                print_pause("As he writhed in pain, you took advantage"
                            " and lunge straight at his head...")
                print_pause("You have slayed the dragon!")
                game_over = input("Do you want to play the game again?\n"
                                  "Type yes if you want to play,"
                                  "anything else to exit.").lower()
                if "yes" == game_over:
                    play_game()


def play_game():
    items = []
    intro()
    change_stage(items)


play_game()
