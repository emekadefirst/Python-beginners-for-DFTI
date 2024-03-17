def airtime():
    while True:
        print("1. MTN \n2. Glo \n3. 9mobile")
        pick = int(input("Option: "))
        if pick == 1:
            phone_number = int(input("Phone number: "))
            limit = 11
            while phone_number != limit:
                amount=int(input("Amount:# "))
                print(f"Your have successfully bought #{amount} airtime")
                break
        elif pick==2:
            phone_number = int(input("Phone number: "))
            limit = 11
            while phone_number != limit:
                amount=int(input("Amount: # "))
                print(f"Your have successfully bought #{amount} airtime")
                break
        elif pick==3:
            phone_number = int(input("Phone number: "))
            limit = 11
            while phone_number != limit:
                amount=int(input("Amount: # "))
                print(f"Your have successfully bought #{amount} airtime")
                break
        else:
            print("Invalid Request")
        break
        return(airtime())