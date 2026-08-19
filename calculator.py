# Simple Calculator for StudentSOS Agent
# This calculator performs basic arithmetic operations

def add(x, y):
    """Add two numbers and return the result"""
    return x + y


def subtract(x, y):
    """Subtract two numbers and return the result"""
    return x - y


def multiply(x, y):
    """Multiply two numbers and return the result"""
    return x * y


def divide(x, y):
    """Divide two numbers and handle division by zero"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y


def calculator():
    """Main calculator function"""
    # Get first number from user
    num1 = float(input("Enter first number: "))
    
    # Get second number from user
    num2 = float(input("Enter second number: "))
    
    # Show operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user's choice
    choice = input("\nEnter your choice (1/2/3/4): ")
    
    # Perform calculation based on user's choice
    if choice == '1':
        result = add(num1, num2)
        print(f"\n{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"\n{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"\n{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"\n{num1} / {num2} = {result}")
    else:
        print("\nInvalid choice! Please enter 1, 2, 3, or 4.")


# Run the calculator
if __name__ == "__main__":
    calculator()
