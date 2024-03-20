#BANK TRANSFER AND AIRTIME RECHARGE

from bank_app2 import account_opening,transfer,Internet,bills,Airtime

print("WELCOME TO JAIZ BANK")
print ("1. Account Opening \n2. Transfer \n3. Internet \n4. Bill and Utility \n5. Airtime")   
serv = str(input(": "))

if serv == "1":
        account_opening()
elif serv == "2": 
        transfer()
    # INTERNET
elif serv == "3":
        Internet()
    # BILLS AND UTILITY
elif serv == "4":
        bills()
    # AIRTIME
elif serv == "5":
        Airtime()
else:
        print("Invalid Resquest!")

