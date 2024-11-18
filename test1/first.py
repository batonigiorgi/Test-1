def calculate(num1, num2, operation):
    if operation == "+":  
        return num1 + num2
    elif operation == "-":  
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":  
        if num2 == 0:  
            return "Error"
        return num1 / num2 
    else:  
        return "Error"

num1 = 10 
num2 = 3  
operation = "/"  

result = calculate(num1, num2, operation)
print("result: ", result)
