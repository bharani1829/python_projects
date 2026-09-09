# #fist take choice
# if user wants roll dice
# else exit


import random

while True:
    choice = input("Do you want to roll the die (y Or n) : ").lower()
    if choice == "y":
        die = random.randint(1,6)
        print(f"({die})")
    elif choice=="n":
        print("Thank You For playing ! ")
        break
    else:
        print("Invalid Choice :")
