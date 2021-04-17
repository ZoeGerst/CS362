
import random
import string

def password():

    length = input("Length of password: ")
    LETTERS = string.ascii_letters
    generate = f'{LETTERS}'
    generate = list(generate)
    random.shuffle(generate)
    new_password = random.choices(generate, k = length)
    new_password = ''.join(new_password)

    return new_password

print(password())