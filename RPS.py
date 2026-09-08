# #ask user to enter choice
# check choice correctness
# generate computer choice 
# check both
# print output

import random

choices = ("r", "p", "s")
emojis = {"r": "🪨", "p": "📄", "s": "✂️"}


def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, Scissors (r, p, or s)? ").lower()

        if user_choice in choices:
            return user_choice

        print("Invalid choice!")


def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You won!")
    else:
        print("You lose! Try again.")


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        ask_continue = input("Do you want to continue (y or n)? ").lower()

        if ask_continue == "n":
            break


play_game()




