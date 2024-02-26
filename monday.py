# Nexted loop

# for x in range(7):
# 	for y in range(6):
# 		for z in range(8):
#                     print(f"{x}, {y}, {z}")
  
# exercise
# number = [5, 2, 5, False, 2]

# for x in number:
#     print(x * x)
    
#While Loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
    
    
# example
# Guessing game
# secret_number = 9
# guess_count = 0
# guess_limit = 2
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You win!!!")
#         break
# else:
#     print("You lost!!!!")
     
# # CAR GAME
command = ""
 
# while command.lower() != "quit":
#     command = input("> ")
#     print("Thanks for playing")
#     if command.lower() == "start":
#         print("Car started..")
#     elif command.lower() == "stop":
#         print("Car stopped")
#     elif command.lower() == "help":
#         print("start - to start the car\nstop - to stop the car\nquit - to quit")
#     else:
#         ("Invalid game request")
# print("Good game!!")

# List
app = ['John', "Apple", 200, True, 249.0]
# print(app[-1]) # Negative from the left
# print(app[0]) # Positive from the right
print(app[2:5])
# print(app[:]) # print all

# # Find the largest number in a list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# max = numbers[0]
# for number in numbers:
#     if number  >max:
#         max = number
# print(max)

# # List method upnext