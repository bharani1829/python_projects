import random
import string

    
def generate_password(length,numbers,special):
        letters = string.ascii_letters
        nums = string.digits
        spl_char = string.punctuation
        characters = letters
        if numbers == 'y':
            characters += nums
        if special == 'y':
            characters += spl_char
        
        
        pwd=""
        
        for i in range(length):
            pwd = pwd + random.choice(characters)
        
        print(pwd)
        
length = int(input("Enter the Length of the password : "))
numbers = input("do you want number also (y or n):").lower()
special = input("do you want Special characters Also (y or n):").lower()

generate_password(length,numbers,special)