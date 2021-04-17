
import random

def password():

    length = input("Length of password: ")
    letters = 'abcdefghijklmnopqrstuvwxyz'
    generate = ''.join(random.choices(letters, k=(length)))

