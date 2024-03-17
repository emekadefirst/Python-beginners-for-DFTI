def dataopt(): 
    while True:
        print("1. MTN \n2. Glo \n3. 9mobile")
        pick = int(input("Option: "))
        if pick == 1: 
            phone_number = int(input("Phone number: "))
            limit = 11
            while phone_number != limit:
                option_1=("100MB")
                option_2=("200MB")
                option_3=("2.5MB")
                option_4=("1GB")
                option_5=("12GB")
                print("a. 100MB (1 Day @ #100) \nb. 200MB (3 Days @ #200) \nc. 2.5GB (2 Days @ #600) \nd. 1GB (7 Days @ #600) \ne. 12GB (30 Days @ #4000)")
                click = str(input("Option: "))
                if click=="a":
                    print(f"Your have successfully purchased { option_1} data.")
                elif click=="b":
                    print(f"Your have successfully purchased { option_2} data.")
                elif click=="c":
                    print(f"Your have successfully purchased { option_3} data.")
                elif click=="d":
                    print(f"Your have successfully purchased { option_4} data.")
                elif click=="e":
                    print(f"Your have successfully purchased { option_5} data.")
                else:
                    print("Invalid Command")
                break
        elif pick==2:
            phone_number = int(input("Phone number: "))
            limit = 11
            while phone_number != limit:
                option_1=("50MB")
                option_2=("350MB")
                option_3=("1.8GB")
                option_4=("7GB")
                option_5=("9.2GB")
                print("a. 50MB (1 Day @ #50) \nb. 350MB (2 Days @ #200) \nc. 1.8GB (14 Days @ #500) \nd. 7GB (7 Days @ #1500) \ne. 9.2GB (30 Days @ #2000)")
                click = str(input("Option: "))
                if click=="a":
                    print(f"Your have successfully purchased {option_1} data.")
                elif click=="b":
                    print(f"Your have successfully purchased {option_2} data.")
                elif click=="c":
                    print(f"Your have successfully purchased {option_3} data.")
                elif click=="d":
                    print(f"Your have successfully purchased {option_4} data.")
                elif click=="e":
                    print(f"Your have successfully purchased {option_5} data.")
                else:
                    print("Invalid Command")
                break
        elif pick==3:
            phone_number = int(input("Phone number: "))
            limit=11
            while phone_number != limit:
                option_1=("100MB")
                option_2=("650MB")
                option_3=("1GB")
                option_4=("7GB")
                option_5=("6.2GB")
                print("a. 100MB (1 Day @ #100) \nb. 650MB (1 Day @ #200) \nc. 1GB (1 Day @ #600) \nd. 7GB (7 Days @ #1500) \ne. 6.2GB (30 Days @ #1200)")
                click = str(input("Option: "))
                if click=="a":
                    print(f"Your have successfully purchased {option_1} data.")
                elif click=="b":
                    print(f"Your have successfully purchased {option_2} data.")
                elif click=="c":
                    print(f"Your have successfully purchased {option_3} data.")
                elif click=="d":
                    print(f"Your have successfully purchased {option_4} data.")
                elif click=="e":
                    print(f"Your have successfully purchased {option_5} data.")
                else:
                    print("Invalid Command")
                break
            else:
                print("Invalid Request")
        break
        return(dataopt()) 