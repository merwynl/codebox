# Simple calculator program
operator = input("Please enter an operator (+ - * / % ** //): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "*":
    result =  num1 + num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "%":
    result =  num1 % num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "**":
    result = num1 ** num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
elif operator == "//":
    result =  num1 // num2
    print(f"The result of {num1} {operator} {num2}: {round(result, 2)}")
else:
    print("Incorrect value &/ operator detected. Please assign a valid operator!")