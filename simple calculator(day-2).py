# Day 2 - Simple Calculator
# Function Definitions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    else: 
        return a / b

# Main Program

print("========== SIMPLE CALCULATOR ==========")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", add(num1, num2))

elif choice == "2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", subtract(num1, num2))

elif choice == "3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", multiply(num1, num2))

elif choice == "4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result =", divide(num1, num2))

else:
    print("Invalid Choice! Please select a number between 1 and 4.")

print("\nThank you for using the calculator!")