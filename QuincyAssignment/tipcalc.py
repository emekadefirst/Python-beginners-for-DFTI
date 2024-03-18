"""
Build a tip calculator that adds 3% of whatever the user buys and determine if it's a joint payment or singular payment

Joint payment : divides by n number of people and display amount to pay each

Singular payment : Add tip to the payment 
"""
# Welcome Name and thanks for Patronizing us

# Joint or Singular payment

# You'd be paying

name = str(input("Hello, Welcome, What's your name ? ")).title()
print("Welcome",f"{name}")

Purchase_cost = float(input("What's the cost of your purchase ?"))

tip_amont = 0.03 * Purchase_cost

print("Our Eatery charges 3\"%\" of your purchase as tip, which is ", f"${tip_amont}")

total_cost = tip_amont + Purchase_cost

print(f"Your total cost is ${total_cost}")
print("Are you making a singular or joint payment")
print("a. single payment")
print("b. joint payment")

reply = str(input()).lower()
if reply == "a":
    print(f"Your total cost is ${total_cost}")
elif reply == "b":
    print("how many of you are paying?")
    no_of_ppl = int(input())
    each_py = total_cost / no_of_ppl
    print(f"You are to pay ${each_py}")
else:
    print("invalid request")
    print("Thanks for eating here")


# response = int(input("For Singular Payment type 1 and for Joint Payment type 2"))
# if payment == 1:
#     amount = 5 * 0.03 
#     print("You are to Pay" , f"{amount}")
# elif payment == 2:
#     name