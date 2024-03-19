import string as s
from gen import gen_pass


def check():
    n = str(input("Enter password let me check\n>> "))
    if any(char.isupper() for char in n) and any(char.isdigit() for char in n) and any(char in s.punctuation for char in n):
        print("Password is strong")

    else:
        return print(f"Password is weak\nWe suggest {gen_pass()}")
        

check()