#!/usr/bin/env python3

def admin_login(username, password):
    # SOLVED
    if ((username == "admin" or username == "ADMIN") and (password == "12345")) :
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # SOLVED
    if temperature < 34:
        return "It's brisk out there!"
    elif temperature > 35 and temperature < 74 :
        return "It's a little chilly out there!"
    elif temperature > 98:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
    pass

def fizzbuzz(num):
    # SOLVED
    if (num % 3 == 0) and (num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    # SOLVED
    if (operation == "+"):
        return  num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
    pass
