from march724 import Pot

def create_pot():
    name = str(input("What is your desired name\n>> "))
    type = str(input("What is your desired type\n>> "))
    pot = Pot(name, type)
    print(pot.cook())
    return "Pot created"

def utensils():
    create = create_pot()
    return create


utensils()