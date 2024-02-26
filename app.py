import random as r
import string as s


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
print(shuffled_password)
    
