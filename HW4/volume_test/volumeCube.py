

def volume_calc(a, b, c):
    volume_calc_test = True
    ifDec = False;

    for firstInput in str(a):

        if firstInput.isdigit() == False and (firstInput != '.'):

            volume_calc_test = False;

        elif firstInput == '.' and ifDec == False:

            ifDec = True;

    for secondInput in str(b):

        if secondInput.isdigit() == False and (secondInput != '.'):

            volume_calc_test = False;

        elif secondInput == '.' and ifDec == False:

            ifDec = True;
        
    for thirdInput in str(c):

        if thirdInput.isdigit() == False and (thirdInput != '.'):

            volume_calc_test = False;

        elif thirdInput == '.' and ifDec == False:

            ifDec = True;
    
    if volume_calc_test == True:

        return round((a * b * c), 5)

    else:

        return ("Invalid input!")

