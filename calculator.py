# Simple Calculator

# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4 or + - * /): ")

# Perform calculation
if choice in ('1', '+'):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice in ('2', '-'):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice in ('3', '*'):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice in ('4', '/'):
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation choice.")
