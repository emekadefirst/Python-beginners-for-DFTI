print("Welcome To AC Bus Terminal")
print("Choose a number for location")
print("1. Akowonjo")
print("2. Dopemu")
print("3. Oshodi")
print("4. Agege")
print("5. Egbeda")

selected_location = int(input())

if selected_location == 1:
   print("You are headed for Akowonjo, since you selected ", f"{selected_location}")
   print("We charge N300")
elif selected_location == 2:
   print("You are headed for Dopemu, since you selected ", f"{selected_location}")
   print("We charge N150")
elif selected_location == 3:
   print("You are headed for Oshodi, since you selected ", f"{selected_location}")
   print("We charge N450")
elif selected_location == 4:
   print("You are headed for Agege, since you selected ", f"{selected_location}")
   print("We charge N350")
elif selected_location == 5:
   print("You are headed for Egbeda, since you selected ", f"{selected_location}")
   print("We charge N100")
else :
    print("Invalid Input")

reply = str(input("Do you have change? Type \"Y\" for Yes and \"N\" for No   ")).lower()

if reply == "y" or reply == "yes":
   print("Welcome, Please Enter")
elif reply == "n" or reply == "no":
   print("Sorry, Kindly step out of the queue and find change")
else :
    print("Invalid Input")