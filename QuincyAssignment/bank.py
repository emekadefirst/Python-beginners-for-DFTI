# Open account
# Transfer
# Airtime
# Internet
# Balance
# Bills & Utilites 

import random

print("Welcome To Our Bank")
print("Kindly select an option with a number")
print("1. Open account")
print("2. Transfer")
print("3. Airtime")
print("4. Internet")
print("5. Balance")
print("6. Bills & Utilites")

response = int(input("\nEnter your choice >>  "))

#Open Account
if response == 1:
    print(f"you've selected {response} to open an account")
    print("Kindly fill your details below!!!")
    firstname = str(input("\nInput your First_Name Here >> ")).title()
    lastname = str(input("Input your Last_Name Here >> ")).title()
    othername = str(input("Input your Other_Name Here >> ")).title()
    email = str(input("Input your Email Here >> "))
    Address = str(input("Input your Address Here >> "))

    accountnum = random.randrange(0000000000,9999999999)

    print(f"\nDear {firstname} {lastname} {othername}, your account has been successfully created, \nYour account number is {accountnum} \nThanks for joining the family")

elif response == 2:
    print(f"you've selected {response} to make a transfer, Kindly select receiving Bank")
    print("1. First Bank")
    print("2. Access Bank")
    print("3. UBA")
    print("4. GT Bank")
    print("5. Zenith Bank")
    print("6. Opay")
    print("7. Palmpay")
    print("8. Kuda Bank")
    bank = int(input("\nEnter your choice >> "))
    list = [" ", "First Bank", "Access Bank", "UBA", "GT Bank", "Zenith Bank", "Opay", "Palmpay", "Kuda Bank"]
    num = [1,2,3,4,5,6,7,8]
    for i in num :
        y = i
        # print(y)
        if bank <= 0 or bank >=9:
            print("\nInvalid input")
            
        else:
            print(f"You've selected {bank} to transfer to {list[bank]}, Kindly enter amount to send ")
            beneficiaryacc = input("Please type in receiver's account number >> ")
            if int(len(beneficiaryacc)) < 10:
                print("\nReceiver's account number less than 10 Digits!") 
            elif int(len(beneficiaryacc)) > 10 :
                print("\nReceiver's account number is more than 10 Digits!")
            else:
                amount = int(input("\nEnter amount to transfer >> "))
    #print(f"Dear {firstname}, Kindly confirm you want to send {amount} to {list[bank]} account number: {beneficiaryacc}")
                print(f"\nKindly confirm you want to send N{amount} to {list[bank]} account number: {beneficiaryacc}")
                iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                if iagree == "y" or iagree == "yes":
                    print("\nYour transfer is successful!")
                elif iagree == "n" or iagree == "no":
                    print("\nYour transfer is terminated!")
                else: print("\nInvalid input")
        break
elif response == 3:
    print(f"you've selected {response} to buy airtime, Kindly select network")
    print("1. MTN")
    print("2. Glo")
    print("3. 9mobile")
    print("4. Airtel")
    network = int(input("\nEnter your choice >> "))
    list = [" ", "MTN", "Glo", "9mobile", "Airtel"]
    num = [1,2,3,4]
    for i in num :
        y = i
        # print(y)
        if network <= 0 or network >=5:
            print("\nInvalid input")
        else:
            print(f"\nYou've selected {network} to buy {list[network]} airtime")
            phonenum = input("Please enter you phone number >> ")
            if int(len(phonenum)) < 11:
                print("\nPhone number less than 11 Digits!") 
            elif int(len(phonenum)) > 11 :
                print("\nPhone number is more than 11 Digits!")
            else:
                airtimeamount = int(input("\nKindly enter airtime amount >> "))
                print(f"\nKindly confirm you want to buy N{airtimeamount} {list[network]} airtime for {phonenum}")
                iagree = str(input("\nPress \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                if iagree == "y" or iagree == "yes":
                    print(f"\nAirtime sent successful! and N{airtimeamount} has been deducted from your account balance")
                elif iagree == "n" or iagree == "no":
                    print("\nAirtime purchase terminated!")
                else: print("\nInvalid input")
        break
elif response == 4:
    print(f"you've selected {response} for Internet Purchase, Kindly select network for data purchase")
    print("1. MTN")
    print("2. Glo")
    print("3. 9mobile")
    print("4. Airtel")
    network = int(input("\nEnter your choice >> "))
    list = [" ", "MTN", "Glo", "9mobile", "Airtel"]
    num = [1,2,3,4]
    for i in num :
        y = i
        # print(y)
        if network <= 0 or network >=5:
            print("\nInvalid input")
        else:
            print(f"\nYou've selected {network} to buy {list[network]} data")
            phonenum = input("\nPlease enter phone number >> ")
            if int(len(phonenum)) < 11:
                print("\nPhone number less than 11 Digits!") 
            elif int(len(phonenum)) > 11 :
                print("\nPhone number is more than 11 Digits!")
            else:
                dataamount = int(input("\nKindly enter data amount >> "))
                if dataamount <= 1200 :
                    datasize = int(dataamount/2.4)
                    print(f"\nKindly confirm you want to buy {datasize}mb {list[network]} data for {phonenum} at the price of N{dataamount}")
                    iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                    if iagree == "y" or iagree == "yes":
                        print(f"\nYour {datasize}mb {list[network]} data has been successfully credited to {phonenum} at the price of N{dataamount}, Enjoy")
                    elif iagree == "n" or iagree == "no":
                        print("\nInternet purchase terminated!")
                    else: print("\nInvalid input")
                elif dataamount >=1300 :
                    datasize = int(dataamount/867)
                    print(f"\nKindly confirm you want to buy {datasize}gb {list[network]} data for {phonenum} at the price of N{dataamount}")
                    iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                    if iagree == "y" or iagree == "yes":
                        print(f"\nYour {datasize}gb {list[network]} data has been successfully credited to {phonenum} at the price of N{dataamount}, Enjoy")
                    elif iagree == "n" or iagree == "no":
                        print("\nInternet purchase terminated!")
                    else: print("\nInvalid input")
        break
elif response == 5:
    print(f"\nyou've selected {response} for Balance Check, Kindly select your Bank")
    print("1. First Bank")
    print("2. Access Bank")
    print("3. UBA")
    print("4. GT Bank")
    print("5. Zenith Bank")
    print("6. Opay")
    print("7. Palmpay")
    print("8. Kuda Bank")
    bank = int(input("Enter your choice >> "))
    list = [" ", "First Bank", "Access Bank", "UBA", "GT Bank", "Zenith Bank", "Opay", "Palmpay", "Kuda Bank"]
    num = [1,2,3,4,5,6,7,8]
    for i in num :
        y = i
        # print(y)
        if bank <= 0 or bank >=9:
            print("\nInvalid input")
        else:
            print(f"\nYou've selected {list[bank]} for balance check")
            beneficiaryacc = input("Please enter your account number >> ")
            if int(len(beneficiaryacc)) < 10:
                print("\nAccount number less than 10 Digits!") 
            elif int(len(beneficiaryacc)) > 10 :
                print("\nAccount number is more than 10 Digits!")
            else:
                print(f"\nYour account account balance is N0.00")
        break
elif response == 6:
    print(f"\nyou've selected {response} for utilities and Bill, Kindly select your utility type ")
    print("1. Cable")
    print("2. PHCN")
    typeofpayment = int(input("\nEnter your choice >> "))
    list = [" ", "Cable", "PHCN"]
    num = [1,2]
    for i in num :
        y = i
        # print(y)
        if typeofpayment <= 0 or typeofpayment >=3:
            print("\nInvalid input")
        else:
            print(f"\nYou've selected {typeofpayment} for {list[typeofpayment]} payment, Kindly select Decoder type ")
        break
    if typeofpayment ==1:
        print("1. GoTV")
        print("2. DSTV")
        print("3. Startimes")
        print("4. Box office")
        print("5. Showmax")
        cabletype = int(input("\nEnter your choice >> "))
        list2 = [" ", "GoTV", "DSTV", "Startimes", "Box office", "Showmax"]
        num = [1,2,3,4,5]
        for i in num :
            y = i
            # print(y)
            if cabletype <= 0 or cabletype >=6:
                print("\nInvalid input")
            else:
                print(f"\nYou've selected {cabletype} for {list2[cabletype]} payment")
                decodernum = int(input("\nKindly enter decoder's number >> "))
                subamount = int(input("\nKindly enter subscription amount >> "))
                print(f"\nKindly confirm you want to subscribe N{subamount} for {list2[cabletype]} with smartcard number: {decodernum}")
                iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                if iagree == "y" or iagree == "yes":
                    print("\nYour subscription is successful!")
                elif iagree == "n" or iagree == "no":
                    print("\nYour subscription is canceled!")
                else: print("\nInvalid input")
            break
    elif typeofpayment ==2:
        print("\nKindly select electricity branch or city")
        print("1. Ikeja Electric")
        print("2. Abuja Electric")
        print("3. Eko Electric")
        print("4. Jos Electric")
        print("5. Kogi Electric")
        electriclocation = int(input("\nEnter your choice >> "))
        list3 = [" ", "Ikeja Electric", "Abuja Electric", "Eko Electric", "Jos Electric", "Kogi Electric"]
        num = [1,2,3,4,5]
        for i in num :
            y = i
            # print(y)
            if electriclocation <= 0 or electriclocation >=6:
                print("\nInvalid input")
            else:
                print(f"\nYou've selected {list3[electriclocation]} for Bill payment, Kindly select meter type ")
                print("1. Prepaid")
                print("2. Postpaid")
                electricitem = int(input("\nEnter your choice >> "))
                list2 = [" ", "Prepaid", "Postpaid"]
                num = [1,2]
                for i in num :
                            y = i
                            if electricitem <= 0 or electricitem >=3:
                                print("\nInvalid input")
                            else:
                                print(f"\nYou've selected {list2[electricitem]} for Bill payment")
                                meternum = str(input("\nKindly enter meter number >> "))
                                nepabill = int(input("\nKindly enter bill or unit amount >> "))
                                if len(meternum) >12:
                                    print("\nInvalid input, kindly ensure the number is between 7-12 combinations")
                                elif len(meternum)<=12:
                                    print(f"\nKindly confirm you want to buy electric unit worth N{nepabill} for {list2[electricitem]} meter with ID: {meternum} at {list3[electriclocation]} branch")
                                    iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                                    if iagree == "y" or iagree == "yes":
                                        print(f"\nYour {list2[electricitem]} is successfully recharged!")
                                    elif iagree == "n" or iagree == "no":
                                        print("\nYour bill payment is canceled!")
                                else: print("\nInvalid input")
                            break    
            break          
else:
    print("\nInvalid Selection")