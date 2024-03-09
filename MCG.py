

print(100)
"""For Loop"""
print(200)
#/bin/venv/manage.py/

print(201)

print(range(5))

simp = [5, 2, 2, 4, 2, 2]

for x in simp:
    print(x * "x")


for x in range(5):       
    print(x)
    
(0, 1, 2, 3, 4, 5)


"""Nested """

for x in range(1, 13):
    for y in range(1, 13):
        z = x * y
        print(f"{x} * {y} = {z}")

""""While Loops"""

import sys

guess_number = 9
guess_limit = 3

while True:
    guess_count = 0
    while guess_count < guess_limit:
        response = int(input("Guess the number on my mind\n>> "))
        if response == guess_number:
            print("Yes, you are correct!")
            break
        else:
            print("You're wrong. Try again.")
        guess_count += 1
        
    if guess_count == guess_limit:
        print(f"You've reached your limit, and your response {response} is still wrong")
        reply = int(input("Would you like to play again?\n1. Yes\n2. No\n>> "))
        if reply == 1:
            continue  # Restart the game
        else:
            print("Thank you for playing!")
            sys.exit()  # Exit the program
        
            


    
    
    
    

    
    

