from Tip.app import tip_calc

def cash_payment():
    cash = int(input("How much cash are you paying "))
    tip = tip_calc()
    print(f"We'll charge 3% of what you bought which is {tip}")
    total_cost = tip + purchase_cost
    print("Are making a joint paymment or single payment")
    print("a. Single payment")
    print("b. Joint payment")
    response = input("")
    if response == "a":
        tip = 0.03 * purchase_cost
        print(f"We'll charge 3% of what you bought which is {tip}")
        total_cost = tip + purchase_cost
        print(f"Your total cost is {total_cost}")
        balance = cash - total_cost
        print(f"Your balance is {balance}")
    elif response == "b":
        print("How many of you are paying")
        number = int(input())
        payment = total_cost / number
        print(f"You all are to pay ${payment} each")
        balance = cash - total_cost
        if balance == 0:
            print("You don not have any balance with us")
        else:
            print(f"Your payment was collected successfully and your balance is {balance}")
    else:
        print("invalid request")