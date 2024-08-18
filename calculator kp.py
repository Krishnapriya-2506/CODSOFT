def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nWELCOME TO A SIMPLE CALCULATOR!!!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter the number of the operation you want to perform: ")
    
    if choice == '1':
        print(f"Adding {num1} and {num2} is: {add(num1, num2)}")
    elif choice == '2':
        print(f"Subtracting {num1} from {num2} is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Multiplying {num1} and {num2} is: {multiply(num1, num2)}")
    elif choice == '4':
        if num2 != 0:
            print(f"Dividing {num1} by {num2} is: {divide(num1, num2)}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input! Please choose a valid operation.")

if __name__ == "__main__":
    main()
