
def sentence(string):

    return ' '.join(string.split(' ')[::-1])

print(sentence(input('Input sentence:')))