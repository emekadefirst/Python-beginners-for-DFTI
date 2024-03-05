import random as r
import string as s

def generate_password(): #request
    ul = s.ascii_uppercase
    ll = s.ascii_lowercase
    punctuation = s.punctuation

    first_letter = ''.join(r.sample(ul, 4))
    second_letter = ''.join(r.sample(ll, 4))

    comma = ''.join(r.sample(punctuation, 4))
    all_value = first_letter + second_letter + comma
    password = list(all_value)
    r.shuffle(password)

    shuffled_password = ''.join(password)
    return shuffled_password#response



def create_user():
    username = str(input("Enter your username below\n>> "))
    email = str(input("Enter your email below\n>> "))
    password = generate_password()
    return f"{username}  with {email} has created, and here is your password {password}"


def print_user_info():
    user_info = create_user()
    print(user_info)
    return "Successful 200 OK"

print_user_info()



