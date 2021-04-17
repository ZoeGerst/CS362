
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1, 2, 3, or 4): ")
    if choice in ('1', '2', '3', '4'):
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if choice == '1':
            print(first, "+", second, "=", add(first, second))

        elif choice == '2':
            print(first, "-", second, "=", subtract(first, second))

        elif choice == '3':
            print(first, "*", second, "=", multiply(first, second))

        elif choice == '4':
            print(first, "/", second, "=", divide(first, second))
        break
    