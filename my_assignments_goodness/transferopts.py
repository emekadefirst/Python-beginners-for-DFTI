def transfer():
    while True:
        print("Choose the bank you are Transfering to: \n1. GT Bank \n2. Eco Bank \n3. Access Bank \n4. Wema Bank \n5. United Bank For Africa \n6. Other Options ")
        reply = input(">> ").lower()
        if reply == "1" or reply == "gtb" or reply == "gt bank" or reply == "gtbank":
            # Transfer to GT Bank
            recipient_account_number = int(input("Enter the recipient's GT Bank account number: "))
            num=10
            while recipient_account_number!=num:
                                amount = int(input("Enter the amount you want to transfer: "))

                                # Placeholder for transfer process
                                print(f"Transferring ₦{amount} to GT Bank account number {recipient_account_number}...")
                                print("Transfer successful! \nThnaks for banking with us😉")
                                break
            else:
                print("Invalid!")
        elif reply == "2" or reply == "eco bank" or reply == "eco":
            # Transfer to Eco Bank
            recipient_account_number = int(input("Enter the recipient's Eco Bank account number: "))
            num=10
            while recipient_account_number!=num:
                            amount = int(input("Enter the amount you want to transfer: "))

                            # Placeholder for transfer process
                            print(f"Transferring ₦{amount} to Eco Bank account number {recipient_account_number}...")
                            print("Transfer successful! \nThanks for banking with us😉")
                            break
            else:
                print("Invalid!")
        elif reply == "3" or reply == "access bank" or reply == "access" :
            # Transfer to Access Bank
            recipient_account_number = int(input("Enter the recipient's Access Bank account number: "))
            num=10
            while recipient_account_number!=num:
                            amount = int(input("Enter the amount you want to transfer: "))

                            # Placeholder for transfer process
                            print(f"Transferring ₦{amount} to Access Bank account number {recipient_account_number}...")
                            print("Transfer successful! \nThanks for banking with us😉")
                            break
            else:
                print("Invalid!")
        elif reply == "4" or reply == "wema" or reply == "wema bank":
            # Transfer to Wema Bank
            recipient_account_number = int(input("Enter the recipient's Wema Bank account number: "))
            num=10
            while recipient_account_number!=num:
                            amount = int(input("Enter the amount you want to transfer: "))

                            # Placeholder for transfer process
                            print(f"Transferring ₦{amount} to Wema Bank account number {recipient_account_number}...")
                            print("Transfer successful! \nThanks for banking with us😉")
                            break
            else:
                print("Invalid!")
        elif reply == "5" or reply == "uba" or reply == "united bank for africa":
            # Transfer to United Bank For Africa
            recipient_account_number = int(input("Enter the recipient's United Bank For Africa account number: "))
            num=10
            while recipient_account_number!=num:
                            amount = int(input("Enter the amount you want to transfer: "))

                            # Placeholder for transfer process
                            print(f"Transferring ₦{amount} to United Bank For Africa account number {recipient_account_number}...")
                            print("Transfer successful! \nThanks for banking with us😉")
                            break
            else:
                print("Invalid!")
        elif reply == "6" or reply == "other transfer options":
            # Other transfer options (placeholder)
            print("Choose Other transfer options:\n7. First Bank \n8. Globus Bank \n9.Opay \n10.Palmpay")
            choice = input(">> ").lower()
            if choice == "7" or reply == "first bank":
                # Transfer to First Bank
                    recipient_account_number = int(input("Enter the recipient's First Bank account number: "))
                    num=10
                    while recipient_account_number!=num:
                                    amount = int(input("Enter the amount you want to transfer: "))

                                    # Placeholder for transfer process
                                    print(f"Transferring ₦{amount} to First Bank  account number {recipient_account_number}...")
                                    print("Transfer successful! \nThanks for banking with us😉")
                                    break
                    else:
                        print("Invalid!")
            elif choice == "8" or reply == "globus bank":
                # Transfer to Globus Bank
                    recipient_account_number = int(input("Enter the recipient's Globus Bank account number: "))
                    num=10
                    while recipient_account_number!=num:
                                    amount = int(input("Enter the amount you want to transfer: "))

                                    # Placeholder for transfer process
                                    print(f"Transferring ₦{amount} to Globus Bank  account number {recipient_account_number}...")
                                    print("Transfer successful! \nThanks for banking with us😉")
                                    break
                    else:
                        print("Invalid!")
            elif choice == "9" or reply == "opay":
                # Transfer to OPAY
                    recipient_account_number = int(input("Enter the recipient's OPAY account number: "))
                    num=10
                    while recipient_account_number!=num:
                                    amount = int(input("Enter the amount you want to transfer: "))

                                    # Placeholder for transfer process
                                    print(f"Transferring ₦{amount} to OPAY  account number {recipient_account_number}...")
                                    print("Transfer successful! \nThanks for banking with us😉")
                                    break
                    else:
                        print("Invalid!")
            elif choice == "10" or reply == "palmpay":
                # Transfer to Palmpay
                    recipient_account_number = int(input("Enter the recipient's Palmpay account number: "))
                    num=10
                    while recipient_account_number!=num:
                                    amount = int(input("Enter the amount you want to transfer: "))

                                    # Placeholder for transfer process
                                    print(f"Transferring ₦{amount} to Palmpay account number {recipient_account_number}...")
                                    print("Transfer successful! \nThanks for banking with us😉")
                                    break
                    else:
                        print("Invalid!")
            else:
                    print("invalid bank choice")
        else:
            print("Invalid Option")
        break
    return(transfer)