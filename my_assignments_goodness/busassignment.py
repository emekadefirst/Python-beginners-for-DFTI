print("WELCOME TO OUR BUS TERMINAL.")
print("Hope your day has been lovely. Yes: lovely(😁), no: bad(😡), and meh: not quite lovely(😕)")
reply = str(input(" ")).lower()
if reply == "yes":
    print("Awesome!")
elif reply == "no":
    print("Don't worry, we've got you covered in this blissful ride")
else:
    print("You're about to take the ride of your life!")
print('''The following are our bus stops. 
Notice: we do not stop anywhere else that is not designated in the options below''')
print("1. Iyana Ipaja - 500\n2. Isheri Christ Embassy - 700\n3. Igando Phase 2 - 900\n4. First Gate - 300\n5. Ikotun - 800\nPick your Option")
stops={"Iyana Ipaja":500, "Isheri Christ Embassy":700, "Igando Phase 2":900, "First Gate":300, "Ikotun":800} 
stops_reply = str(input("Input>> "))
if stops_reply == "Iyana Ipaja":
    seats = int(input("Number of seats: "))
    print(stops["Iyana Ipaja"])
    total = seats * stops["Iyana Ipaja"]
    print(total)
elif stops_reply == "Isheri Christ Embassy":
    no_of_seats = int(input("Number of seats: "))
    print(stops["Isheri Christ Embassy"])
    total = no_of_seats * stops["Isheri Christ Embassy"]
    print(total)
elif stops_reply == "Igando Phase 2":
    seats = int(input("Number of seats: "))
    print(stops["Igando Phase 2"])
    total = seats * stops["Igando Phase 2"]
    print(total)
elif stops_reply == "First Gate":
    seats = int(input("Number of seats: "))
    print(stops["First Gate"])
    total = seats * stops["First Gate"]
    print(total)
elif stops_reply=="Ikotun":
    seats = int(input("Number of seats: "))
    print(stops["Ikotun"])
    total = seats * stops["Ikotun"]
    print(total)
else:
    print("Invalid Response")
print("How would you like to pay? \na. Bank transfer \nb. Cash")
response = str(input("")).lower()
if response == "a" or response=="Bank transfer":
    print("You may Proceed")
    print("✔")
elif response=="b" or response=="Cash":
    print("Do you have the exact amount? NOTE: We do not have petty cash \na. yes \nb. no")
    choose = str(input(" ")).lower()
    if choose == "yes" or choose=="a":
        print("You may proceed")
        print("✔")
    elif choose == "no" or choose=="b":
        print("Choose another payment option")
        print("proceed with bank transfer? Yes or no")
        again = str(input(" "))
        if again == "yes": 
            print("Proceed with payment")
        elif again == "no":
            print("HAVE A WONDERFUL DAY, COME AGAIN NEXT TIME.")
        else:
            print("Invalid Option")
    else:
        print("Invalid")
else:
    print("Error")

print("KECCY'S TRANSIT, THE CHOICE YOU'LL NEVER REGRET🎇🎇")
