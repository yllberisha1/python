def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"


result1 = calculate(10, 5, "+")
result2 = calculate(10, 5, "-")
result3 = calculate(10, 5, "*")
result4 = calculate(10, 0, "/")
result5 = calculate(10, 5, "%")


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
