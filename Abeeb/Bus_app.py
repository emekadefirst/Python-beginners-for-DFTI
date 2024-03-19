print("Oshodi to toll gate!")
Airport = 100
Cement = 150
Dopemu = 200
Yana_paja = 250
Abule_egba = 300
Agbado = 400
Toll_gate = 500

print("1. Airport = 100 \n2. Cement = 150 \n3. Dopemu = 200 \n4. Yana paja = 250 \n5. Abule Egba = 300 \n6. Agbado = 400 \n7. Toll gate = 500")
Dest = str(input("Where you dey go: "))
if Dest == "Airport" or Dest == "1":
    print("Your money na 100")
    load = 0.3 * Airport
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Airport
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")

elif Dest == "Cement" or Dest == "2":
    print("Your money na 150")
    load = 0.3 * Cement
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Cement
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
elif Dest == "Dopemu" or Dest == "3":
    print("Your money na 200")
    load = 0.3 * Dopemu
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Dopemu
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
elif Dest == "Yana Paja" or Dest == "4":
    print("Your money na 250")
    load = 0.3 * Yana_paja
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Yana_paja
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
elif Dest == "Abule Egba" or Dest == "5":
    print("Your money na 300")
    load = 0.3 * Abule_egba
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Abule_egba
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
elif Dest == "Agbado" or Dest  == "6":
    print("Your money na 400")
    load = 0.3 * Agbado
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Agbado
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
elif Dest == "Toll gate" or Dest == "7":
    print("Your money na 500")
    load = 0.3 * Toll_gate
    print("You carry load: ")
    print("a. Yes")
    print("b. No")
    Resp = str(input(""))
    if Resp == "a" or Resp == "Yes":
           print(f"You go pay N{load} for your load oo")
           total_pay = load + Toll_gate
           print(f"Your total money na {total_pay}")
    else:
            print("Wole pelu change e oo!! ")
else:
    print("Ko lo!! \nZoooooom!!!!!")
 
 