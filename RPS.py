# #ask user to enter choice
# check choice correctness
# generate computer choice 
# check both
# print output

import random

choices = ('r','p','s')
emojis = {'r':'🪨','p':'📄','s':'✂️'}
while True:
    user_choice = input("Rock,Paper,Scissors(r or p or s)..? ").lower()

    if user_choice not in choices:
        print("Invalid Choice !")
        continue
    computer_choice = random.choice(choices)
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer Choose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print("Its a tie !")
    elif(
        user_choice ==  'r' and computer_choice == 's' or 
        user_choice ==  'p' and computer_choice == 'r' or 
        user_choice ==  's' and computer_choice == 'p'):
        print("You Won !")
    else:
        print("You Loose !-----Try Again")
    ask_continue = input("Do you want to continue(y or n)..?").lower()
    if ask_continue == 'n':
        print("Thank You")
        break




