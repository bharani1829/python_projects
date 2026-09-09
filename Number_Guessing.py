# first generate random number 
# ask user to enter 
# check the number using if and else 
# if right print congratulations and Stop
#here i mentioned value error because if you enter rather than number like symbols and characters in int we get tha
import random
number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input("Guess A Number between 1 to 100 :  "))
        if guess>number_to_guess:
            print("Too High !")
        elif guess<number_to_guess:
            print("Too Low !")
        else:
            print(f"Congrats You Guessed it Right It is {number_to_guess}")
    except ValueError:
        print("Valid Number !")
    
