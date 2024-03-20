import random as r
import string as s

def gen_pass():
    ul = s.ascii_uppercase
    ll = s.ascii_lowercase
    punctuation = s.punctuation
    digi = s.digits
    

    first_letter = ''.join(r.sample(ul, 4))
    second_letter = ''.join(r.sample(ll, 4))
    third_digi = ''.join(r.sample(digi,4))

    comma = ''.join(r.sample(punctuation, 4))
    all_value = first_letter + second_letter + comma + third_digi
    password = list(all_value)
    r.shuffle(password)

    shuffled_password = ''.join(password)
    return shuffled_password