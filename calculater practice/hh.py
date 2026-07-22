print("First Calculator")

num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")

num2 = input("Enter second number: ")

if num2 == "":
    print("Error: Second number is required!")
else:
    num2 = int(num2)

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        print("Result:", num1 / num2)

        if num2 != 0:           
            print("Error: Division by zero!")

    else:
        print("Invalid operator!")