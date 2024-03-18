print("WELCOME OUR ESTEEMED CUSTOMER😊😊")
print("Did you enjoy your time with us?")
print("Yes or no")
response = (str(input(""))).title()
if response == "Yes":
    print("HURRAY✨✨")
elif response == "no":
    print("😢😢😢")
    print("We will serve you better. Drop your complaints or suggestions in the suggestion box")
else:
    print("Invalid option")
price_of_food = float(input("How much was your meal: #"))
print("You are to pay 3% tip for your goods")
total = price_of_food * 0.03 + price_of_food
print(total)
print("Single payment or joint payment")
print("a. single payment")
print("b. joint payment")
choose = str(input())
if choose == "a" or choose == "single payment":
    print("👌")
    print(total)
elif choose == "b" or choose == "joint payment":
    print("👌How many people are paying?")
    no_of_people = int(input())
    each_pays = total / no_of_people
    print(f"Each person is to pay {each_pays}")
else:
    print("❌")
print("payment option a: bank tansfer, b: cash")
payment_option = str(input("Click a or b to determine mode of payment: ")).lower()
if payment_option == "a" or payment_option == "bank transfer":
    print("✔")
elif payment_option == "b" or payment_option == "cash":
    print("✔")

else:
    print("Invalid Request😢")
print("Thanks for shopping with us 💖💖💖")