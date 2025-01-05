def calculate(num1, num2, operation):
    if operation=='+':
        return num1+num2
    elif operation=='-':
        return num1-num2
    elif operation=='*':
        return num1*num2
    elif operation=='/':
        if num2!=0:
            return num1/num2
        else:
            return "Division by zero is not possible."
    else:
        return "Invalid operation."

try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Enter an operation (+, -, *, /): ")

    result=calculate(num1, num2, operation)
    print(f"The result is: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
