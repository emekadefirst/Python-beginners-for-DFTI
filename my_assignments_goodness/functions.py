login_with_username_andpasswords={"Chinwe Obinna": "obinna45", "Ayoola Steven": "blessing5", "Okechukwu Goodness": "1245kec", "Israel Deborah": "lamda", "Loveth Ebenezer": "wakandafrv", "Ekemini Iniobong":"westend"}
already_existing_accounts_with_balance= {"Chinwe Obinna": 450000, "Ayoola Steven": 4500, "Okechukwu Goodness": 100000, "Israel Deborah": 30000, "Loveth Ebenezer": 70000, "Ekemini Iniobong":450000}
loginphoneandpassword={9078675664: "obinna45", 9067644523: "blessing5", 8179502239: "1245kec", 7092562548: "lamda", 7034562456: "wakandafrv", 8178674343:"westend"}
email_and_password={"chinwe@gmail.com": "obinna45", "stevena@gmail.com": "blessing5", "keccy@gmail.com": "1245kec", "debbyis@gmail.com": "lamda", "loebenezer@gmail.com": "wakandafrv", "ekems@gmail.com":"westend"}
already_existing_accounts=("Chinwe Obinna", "Ayoola Steven", "Okechukwu Goodness", "Israel Deborah", "Loveth Ebenezer", "Ekemini Iniobong")



def chooselogin():
    print("\nLogin with: \n1. Username \n2. Phone number \n3. email")
    reply = int(input())
    if reply == 1:
        response = str(input("Username: "))
        while response in already_existing_accounts:
            click = str(input("Password: "))
            while click in login_with_username_andpasswords[response]:
                print(f"Your login was successful, {response}")
                break
            break
    elif reply == 2:
        response = int(input("Phone Number: "))
        num = 10
        while response!=num and response in loginphoneandpassword:
            click = str(input("Password: "))
            while click in loginphoneandpassword[response]:
                print(f"Your login was successful, user {response}")
                break 
            break
        else:
            print("Invalid Request!")
    elif reply == 3:
        response = str(input("Email: "))
        while response in email_and_password:
            click = str(input("Password: "))
            while click in email_and_password[response]:
                print(f"Your login was successful, user {response}")
                break
            break
        else:
            print("Invalid Response!")
    else:
        print("Invalid Response!")
        return(chooselogin())