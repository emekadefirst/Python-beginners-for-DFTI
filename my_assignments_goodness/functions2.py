def choosenewsignup():
        first_name = str(input("First name: ")).capitalize()
        last_name = str(input("Last name: ")).capitalize()
        other_names = str(input("Other names: ")).capitalize()
        names = (f"{first_name} {last_name} {other_names}")
        date_of_birth=input("Date of birth? \n Follow the format: day/month/year \n")
        home_address=input("Home Address: ")
        while True:
            ph_num=int(input("Phone Number: "))
            lim=11
            while ph_num!=lim:
                sex=int(input("Sex: \n1. Male \n2. Female \n"))
                if sex==1 or 2:
                    marital_status=int(input("Marital Status: \n1. Single \n2. Married \n "))
                    if marital_status==1 or 2:
                        email = str(input("Email: "))
                        username = str(input("Username:"))
                        password = str(input("Password:"))
                        confirm_password = str(input("Confirm Password:"))
                        if password == confirm_password:
                            number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                            import random
                            result = ""
                            for _ in range(10):  # Generate 10 digits for the account number
                                digit = random.randint(0, 9)  # Generate a random digit between 0 and 9
                                result += str(digit)  
                                print(f"\nThank you for filling out the form.\n Here are your account details: \nDate of Birth: {date_of_birth}\nAddress: {home_address}\nPhone number: {ph_num}")
                                print(f"\nYour Login was Successful! \nWelcome, {names} \n Your account number is {result}")
                                break                                            
                        else:
                            print("Signup Failed")
                    else:
                        print("Invalid Command!")
                else:
                    print("Invalid Command!")  
                break      
            else:
                print("Error!")
            break
        return(choosenewsignup)
