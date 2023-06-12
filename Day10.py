# Day 10 --> Functions with Outputs

# def my_function():
#    result = 3 * 2
#    return result

# output = my_function()

# return statements will exit a function

# can use """ """ to write docstrings; used to write multi-line strings

# ctrl + / --> shortcut to make code into comments

# Calculator w/ functions

# Functions

# def add(n1, n2):
#   return n1 + n2
#
# def sub(n1, n2):
#   return n1 - n2
#
# def multi(n1, n2):
#   return n1 * n2
#
# def divide(n1, n2):
#   return n1 / n2
#
# operations = {
#    "+" : add,
#    "-" : sub,
#    "*" : multi,
#    "/" : divide
# }
# exit_program = False
#
# while not exit_program:
#     num1 = int(input("What is the first number? "))
#     num2 = int(input("What is the second number? "))
#
#     for operator in operations:
#         print(operator)
#
#     symbol = input("Pick an operation from the list printed: ")
#     function_choice = operations[symbol]
#     answer = function_choice(num1, num2)
# # if (symbol == "+"):
# #   answer = add(num1, num2)
# # if (symbol == "-"):
# #   answer = sub(num1, num2)
# # if (symbol == "*"):
# #   answer = multi(num1, num2)
# # if (symbol == "/"):
# #   answer = divide(num1, num2)
#     print(f"{num1} {symbol} {num2} = {answer}")
#
#     user_choice = input("Would you like to try again? Enter 'y' to continue, 'n' to exit: ").lower()
#     if user_choice == 'n':
#         break
# print("\nThank you! Have a great day.")

# Functions are useful for passing values into another function

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    # print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            # clear()
            calculator()


calculator()
