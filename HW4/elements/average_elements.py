#Zoe Gerst
#CS 362
#5/3/2021
def ave_elements(x):

    inputs = 0.0
    elements = 0.0
    elements_test = True

    for input_one in x:

        for input_two in str(input_one):

            if input_two.isdigit() == False and input_two != '-' and input_two != '.':

                elements_test = False

        if(elements_test == True):
            
            inputs = inputs + input_one
            elements = elements + 1

    if elements_test == False:

        return ("Invalid input.")

    if len(x) == 0:

        return ("No inputs.")

    return (round((inputs / elements), 5))

    
