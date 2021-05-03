#Zoe Gerst
#CS 362
#5/3/21

def name(a, b):

    name_test = True

    for input_one in a:

        if input_one.isalpha() == False:

            return ("Invalid input.")
        
    for input_two in b:

        if input_two.isalpha() == False:

            return ("Invalid input.")

    if a == "" or b == "":

        return ("No inputs.")

    else:

        return (a + " " + b)