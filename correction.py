




def check():
    reply = str(input("Enter your password let me check\n>> "))
    for i in reply:
            if i.isupper() or i == (s.punctuation) or i == (range(10)):
                print("Password is strong")
                break

    else:
        pas = gen_pass()
        print(f"Your Password is weak, How about you try \n{pas}")
        
check()

