
def isPalindrome(string):

    length = len(string)
    first = 0
    last = length - 1 
    results = 1

    while(first<last):

           if(string[first] == string[last]):
               first = first + 1
               last = last - 1

           else:
               results = 0
               break

    return int(results)

string = input("Enter string: ")

results = isPalindrome(string)

if(results):

    print("It is a palindrome.")
else:

    print("It is not a palindrome.")