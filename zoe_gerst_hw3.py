#Zoe Gerst
#CS 362
#4/25/2021
#leap year program but with error handling

try:

    year = int(input("Enter a year: "))

    if(year % 4) == 0:

        if(year % 100) == 0:

            if(year % 400) == 0:

                print("{0} is a leap year".format(year))

            else:

                print("{0} is not a leap year".format(year))

        else:

            print("{0} is a leap year".format(year))

    else:

        print("{0} is not a leap year".format(year))

except ValueError:

    print("Not a valid input!")