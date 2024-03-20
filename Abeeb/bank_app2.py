
import random

def account_opening():
    print("kindly follow the prompt below to open an account with us.")
    # OPENING ACCOUNT
    print("Account Type: \nA. Savings \nB. Current")
    Acct_type =input(": ").strip()
    Title =input("Title: ").strip()
    Surname =input("Surname: ").strip().title()
    Name =input("First Name: ").strip().title()
    input("Residential Address: ").strip().title(),input("Marital Status: ").strip().title()
    dateof_birth =input("DOB (dd/mm/yyyy): ").strip()
    NIN =int(input("NIN: "))
    Phone =int(input("Phone Number: "))
    print(f"Dear {Title} {Surname},\nIt serves us pleasure to have you here. To complete your account, kindly upload your passport,NIN, and a current utility bill.\nHowever, your account is under process, expect your account details shortly. Thank you!! ")
    print('>>>>>>LOADING..........................')
    input("Click ENTER button! ")
    
    acctnm = (random.randrange(1100000000,9080999019))
    print(f"We are pleased to inform you that your account has been successfully created. \nYour account number is:{acctnm} \nAccount Name:{Surname} {Name}")
    print("Congratulations")


def transfer():
    print("TRANSFER")
    print("What bank do you want to transfer to? ")
    print("1. Access Bank \n2. First Bank \n3. Polaris Bank \n4. Opay \n5. Zenith Bank \n6. FCMB \n7. Other banks")
    farm = {"Access Bank":1, "First Bank":2,"Polaris Bank":3,"Opay":4, "Zenith Bank":5,"FCMB":6,"Other bank":7}
    response = int(input("Enter Bank: "))
    for x in farm.values():
        if response == x:
            #Transfer to All Banks
            recipient_account_number = int(input("Enter recipient's account number "))
            Ac = 11
            while recipient_account_number!= Ac:
                print("Confirming account name...")
                amount = int(input("Enter the amount to be transferred:#"))
                print(f"Transferring N{amount} to Access Bank account number {recipient_account_number}....")
                print("Transfer Processing...")
                print("Transfer Successful?????? \nThank you for banking with us!?")
                break    
    else:
        print("Invalid Input")


def Internet():
    print("Service Providers")
    print("1. MTN NG DATA \n2. GLO NG DATA \n3. AIRTEL NG DATA \n4. SMILE NG")
    provider = str(input("Choose a provider: "))
    if provider == "1" or provider == "MTN":
        print("Enter package>> ")
        twoK_gb_for_a_year = 450000
        OneK_gb_for_a_year = 250000
        fourH_gb_for_a_year = 120000
        two5_gb_for_a_3MONTH = 450000
        seventyfive_gb_for_a_month = 16000
        print("2000GB FOR 1 YEAR \n1000GB FOR 1 YEAR \n400GB FOR 1 YEAR \n250GB FOR 3 MONTHS \n75GB FOR A MONTH")
        package = (input("Enter gig from the above: "))
        if package == "2000GB":
            print(f"Your payment for this package is N{twoK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "1000GB":
            print(f"Your payment for this package is N{OneK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "400GB":
            print(f"Your payment for this package is N{fourH_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "250GB":
            print(f"Your payment for this package is N{two5_gb_for_a_3MONTH}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "75G":
            print(f"Your payment for this package is N{twoK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        else:
            print("Not Available")
            
    elif provider == "2" or provider == "GLO":
        print("Enter package")
        twoK_gb_for_a_year = 350000
        OneK_gb_for_a_year = 250000
        fourH_gb_for_a_year = 50000
        two5_gb_for_a_3MONTH = 40000
        seventyfive_gb_for_a_month = 14000
        print("2100GB FOR 1 YEAR \n1100GB FOR 1 YEAR \n500GB FOR 1 YEAR \n350GB FOR 3 MONTHS \n85GB FOR A MONTH")
        package = (input("Enter gig from the above: "))
        if package == "2100GB":
            print(f"Your payment for this package is N{twoK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "1100GB":
            print(f"Your payment for this package is N{OneK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "500GB":
            print(f"Your payment for this package is N{fourH_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "350GB":
            print(f"Your payment for this package is N{two5_gb_for_a_3MONTH}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "85GB":
            print(f"Your payment for this package is N{seventyfive_gb_for_a_month}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        else:
            print("Not Available")
    
    elif provider == "3" or provider == "AIRTEL":
        print("Enter package")
        twoK_gbi_for_a_year = 550000
        OneK_gbe_for_a_year = 350000
        fourH_gbo_for_a_year = 220000
        two5_gba_for_a_3MONTH = 430000
        seventyfive_gbs_for_a_month = 17000
        print("2100GB FOR 1 YEAR \n1020GB FOR 1 YEAR \n500GB FOR 1 YEAR \n450GB FOR 3 MONTHS \n80GB FOR A MONTH")
        package = (input("Enter gig from the above: "))
        if package == "2100GB":
            print(f"Your payment for this package is N{twoK_gbi_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "1020GB":
            print(f"Your payment for this package is N{OneK_gbe_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "500GB":
            print(f"Your payment for this package is N{fourH_gbo_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "450GB":
            print(f"Your payment for this package is N{two5_gba_for_a_3MONTH}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "80GB":
            print(f"Your payment for this package is N{seventyfive_gbs_for_a_month}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        else:
            print("Not Available")
       
    elif provider == "4" or provider == "SMILE":
        print("Enter package")
        twiK_gb_for_a_year = 470000
        On1K_gb_for_a_year = 290000
        foureH_gb_for_a_year = 150000
        twoo5_gb_for_a_3MONTH = 490000
        peventyfive_gb_for_a_month = 19000
        print("3000GB FOR 1 YEAR \n2000GB FOR 1 YEAR \n600GB FOR 1 YEAR \n450GB FOR 3 MONTHS \n74GB FOR A MONTH")
        package = (input("Enter gig from the above: "))
        if package == "3000GB":
            print(f"Your payment for this package is N{twiK_gb_for_a_year}")
            print("Recipent")
            numb = int(input("Phone Number:"))
            print (f"{package} has been successfully delivered to {numb}")
        elif package == "2000GB":
            print(f"Your payment for this package is N{On1K_gb_for_a_year}")
        elif package == "600GB":
            print(f"Your payment for this package is N{foureH_gb_for_a_year}")
        elif package == "450GB":
            print(f"Your payment for this package is N{twoo5_gb_for_a_3MONTH}")
        elif package == "74GB":
            print(f"Your payment for this package is N{peventyfive_gb_for_a_month}")
        else:
            print("Not Available")
        print("Recipent")
        numb = int(input("Phone Number:"))
        print (f"{package} has been successfully delivered to {numb}")
    else: 
        return "Invalid input"


def bills():
    print("Utility and Bill")
    print("1. TV Subscription \n2. Electricity")
    bill = input(">> ")
    if bill == "1" or bill == "TV":
        print("Select Service Porvider for subcription")
        print("DSTV \nGOTV \nSTARTIME")
        Service_provider = str(input(": "))
        # FOR DSTV
        if Service_provider == "DSTV":
            print("Choose a package")
            premium = float(18000)
            compact = float(12000)
            Confam = float(10000)
            yanga = float(8000)
            print("1. Premium \n2. Compact \n3. Confam \n4. Yanga")
            Package = str(input(": "))
            if Package == "1" or Package == "Premium":
                print(f"You will be charged N{premium} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == premium :
                    print("Your premium package subscription was successful. \nThank you!")
                elif payment > premium:
                    balance = payment - premium
                    print(f"Your premium package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            elif Package == "2" or Package == "Compact":
                print(f"You will be charged N{compact} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == compact :
                    print("Your compact package subscription was successful. \nThank you!")
                elif payment > compact:
                    balance = payment - compact
                    print(f"Your compact package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!")
            elif Package == "3" or Package == "Confam":
                print(f"You will be charged N{Confam} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == Confam :
                    print("Your confam package subscription was successful. \nThank you!")
                elif payment > Confam:
                    balance = payment - Confam
                    print(f"Your confam package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!")
            elif Package == "4" or Package == "Yanga":
                print(f"You will be charged N{yanga} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == yanga :
                    print("Your yanga package subscription was successful. \nThank you!")
                elif payment > yanga:
                    balance = payment - yanga
                    print(f"Your yanga package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!")
            else:
                print("Invalid Input \nKindly enter the available package")
        # FOR GOTV
        elif Service_provider == "GOTV":
            print("Choose a package")
            max = float(12000)
            supa = float(9000)
            smallie = float(5000)
            print("1.GOTV MAX \n2.GOTV SUPA \n3.GOTV SMALLIE")
            Package = str(input(": "))
            if Package == "1" :
                print(f"You will be charged N{max} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == max :
                    print("Your max package subscription was successful. \nThank you!")
                elif payment > max:
                    balance = payment - max
                    print(f"Your max package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            elif Package == "2" :
                print(f"You will be charged N{supa} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == supa :
                    print("Your supa package subscription was successful. \nThank you!")
                elif payment > supa:
                    balance = payment - supa
                    print(f"Your supa package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            elif Package == "3" :
                print(f"You will be charged N{smallie} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == smallie :
                    print("Your smallie package subscription was successful. \nThank you!")
                elif payment > smallie:
                    balance = payment - smallie
                    print(f"Your smallie package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            # FOR STARTIME
        elif Service_provider == "STARTIME":
            print("Choose a package")
            super = float(65000)
            classic = float(45000)
            smart= float(3000)
            print("1.SUPER \n2.CLASSIC \n3.SMART")
            Package = str(input(": "))
            if Package == "1" :
                print(f"You will be charged N{super} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == super :
                    print("Your super package subscription was successful. \nThank you!")
                elif payment > super:
                    balance = payment - super
                    print(f"Your super package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            elif Package == "2" :
                print(f"You will be charged N{classic} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == classic :
                    print("Your classic package subscription was successful. \nThank you!")
                elif payment > classic:
                    balance = payment - classic
                    print(f"Your classic package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!") 
            elif Package == "3" :
                print(f"You will be charged N{smart} for this package")
                int(input("Smart Card Number: "))
                payment = float(input("Enter Amount: "))
                if payment == smart :
                    print("Your smart package subscription was successful. \nThank you!")
                elif payment > smart:
                    balance = payment - smart
                    print(f"Your smart package subscription was sucessful, your balance is N{balance} \n Thank You!!")
                else:
                    print("Insufficient balance!")

        # ELECTRICITY
    elif bill == "2" or bill == "Electricity":
        print("Choose a Provider")
        print("1. IKEDC NG \n2. IBEDC NG \n3. PHED NG")
        Service_provider = str(input(": "))
        if Service_provider == "1":
            print("Choose a package")
            print("1. AEDC PREPAID \n2. AEDC POSTPAID")
            Package = str(input(": "))
            if Package == "1" :
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            elif Package == "2":
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            else:
                print("Sorry! Invalid Input")
        elif Service_provider == "2":
            print("Choose a package")
            print("1. AEDC PREPAID \n2. AEDC POSTPAID")
            Package = str(input(": "))
            if Package == "1" :
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            elif Package == "2":
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            else:
                print("Sorry! Invalid Input")
        elif Service_provider == "3":
            print("Choose a package")
            print("1. AEDC PREPAID \n2. AEDC POSTPAID")
            Package = str(input(": "))
            if Package == "1" :
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            elif Package == "2":
                print("Input your Metre Number below. ")
                int(input("Metre Number: "))
                payment = float(input("Enter Amount: "))
                print(f"Dear Customer, \nYour recharge of N{payment} was successful.Congratulations!!")
            else:
                print("Sorry! Invalid Input")
        else:
            print("Invalid!!")
    else:
        print("Invalid input! \nKindly enter the available package.")


def Airtime():
    print("Select Network Provider")
    print("1. MTN \n2. GLO \n3. AIRTEL \n4. 9MOBILE")
    reply = str(input(" "))
    #MTN Recharge
    if reply == "1" or reply == "MTN":
        Phone_Number = int(input("Enter MTN phone number "))
        print("Select Amount")
        print("1. 100")
        print("2. 200")
        print("3. 500")
        print("4. 1000")
        print("5. 5000")
        print("6. Others")
        answer = str(input(" "))
        if answer == "1" or answer == "100":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "2" or answer == "200":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "3" or answer == "500":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "4" or answer == "1000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "5" or answer == "5000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        else:
            enter_amount = int(input("Enter the amount#"))
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
    #GLO Recharge
    elif reply == "2" or reply == "GLO":
        Phone_Number = int(input("Enter GLO phone number "))
        print("Select Amount")
        print("1. 100")
        print("2. 200")
        print("3. 500")
        print("4. 1000")
        print("5. 5000")
        print("6. Others")
        answer = str(input(" "))
        if answer == "1" or answer == "100":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "2" or answer == "200":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "3" or answer == "500":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "4" or answer == "1000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "5" or answer == "5000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        else:
            enter_amount = int(input("Enter the amount#"))
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
    #AIRTEL Recharge
    elif reply == "3" or reply == "AIRTEL":
        Phone_Number = int(input("Enter AIRTEL phone number "))
        print("Select Amount")
        print("1. 100")
        print("2. 200")
        print("3. 500")
        print("4. 1000")
        print("5. 5000")
        print("6. Others")
        answer = str(input(" "))
        if answer == "1" or answer == "100":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "2" or answer == "200":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "3" or answer == "500":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "4" or answer == "1000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "5" or answer == "5000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        else:
            enter_amount = int(input("Enter the amount#"))
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
    #9MOBILE Recharge
    elif reply == "4" or reply == "(9MOBILE)":
        Phone_Number = int(input("Enter 9MOBILE phone number "))
        print("Select Amount")
        print("1. 100")
        print("2. 200")
        print("3. 500")
        print("4. 1000")
        print("5. 5000")
        print("6. Others")
        answer = str(input(" "))
        if answer == "1" or answer == "100":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "2" or answer == "200":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "3" or answer == "500":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "4" or answer == "1000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        elif answer == "5" or answer == "5000":
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
        else:
            enter_amount = int(input("Enter the amount#"))
            print(f"Purchasing airtime... \nAirtime recharge to {Phone_Number} was successful! \nThank you for banking with us?")
    else:
        return "INVALID REQUEST! \nCheck options and try again."
