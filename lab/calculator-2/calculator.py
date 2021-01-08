"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def check_two_digits():
    """Check if the user has two valid digits"""
    if tokenize_user_input[1].isdigit and tokenize_user_input[2].isdigit:
        return True
    else:
        print("Please try with two digits number.")

def check_one_digit():
    """Check if the user has one valid digit"""
    if tokenize_user_input[1].isdigit:
        return True
    else:
        print("Please try with one digit number.")

# Replace this with your code

while True:
    #read input
    user_input = input("> ")
    # tokenize input
    tokenize_user_input = user_input.split(" ") #take the string - break it up to a smaller part
        # if the first token is "q":
    if tokenize_user_input[0] == "q":
        break
    elif len(tokenize_user_input) < 2 or len(tokenize_user_input) > 3:
        print("Not a valid input. Try again")
    else:
        operator = tokenize_user_input[0]
        if operator == "+":
            check_two_digits()
            print(add(float(tokenize_user_input[1]), float(tokenize_user_input[2])))
        else:
            print("Incorrect operator. Try again.")    

