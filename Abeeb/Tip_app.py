#Build a tip calculator that add 3% to what ever the user buys and determines if it a joint or single payment
print("Good day, hope you enjoyed your meal? ")
print("a. Yes")
print("b. No")
response = str(input(""))
if response == "a" or response == "Yes" :
    print("We are clad you did")
else:
    print("Apologies, we hope to serve you well next time")
purchase_cost = float(input("how much is your meal? $"))
tip = 0.3 * purchase_cost
print(f"Our restuarant charges 3% for total purchase, which is {tip} ")
total_cost = tip + purchase_cost
print("Are you making a single or joint Payment?")
print ("a. Single payment")
print ("b. joint payment")
payment_type = str(input(""))
if payment_type == "a" or payment_type == "single":
    print(f"Your total cost is ${total_cost}")
elif payment_type == "b" or payment_type == "joint payment":
    print("how many of you are paying? ")
    numb_of_people = int(input(""))
    each_pay = total_cost / numb_of_people
    print(f"You are welcome as you pay ${each_pay} each")
else:
    print("invalid request")
print("Thanks for patronising us")




