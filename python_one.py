x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Enter the operation (addition, subtraction, multiplication , division): ")

if operation == "addition":
    result = x + y
elif operation == "subtraction":
    result = x - y 
elif operation == "multiplication":
    result = x * y  
elif operation == "division":
    if y != 0:
        result = x / y
    else:
        result = "Error: Division by zero is not allowed."  
else:
    result = "Error: Invalid operation."