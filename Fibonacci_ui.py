from Fibonacci import *


# create functions used for program
def upper_limit():
    while True:
        upper_limit_input = input("\nEnter the upper limit for your Fibonacci numbers list: ")
        try:
            upper_limit = int(upper_limit_input)
            if upper_limit > 0:
                return upper_limit
            else:
                print("Please enter a value greater than 0.")
        except ValueError:
            print("Please enter a whole number for your upper limit.")


def lower_limit():
    while True:
        lower_limit_input = input("\nEnter the lower limit for your Fibonacci numbers list: ")
        try:
            lower_limit = int(lower_limit_input)
            if lower_limit >= 0:
                return lower_limit
            else:
                print("Please enter a value greater than or equal to 0.")
        except ValueError:
            print("Please enter a whole number for your lower limit.")


def set_integer():
    while True:
        integer_input = input("\nEnter the integer you wish to check: ")
        try:
            integer = int(integer_input)
            # setting integer will also set upper limit for fib list
            if integer >= 0:
                return integer
            else:
                print("Please enter a value greater than or equal to 0.")
        except ValueError:
            print("Please enter a whole number you wish to check.")


# function for user manually setting upper/lower limit and seeing resulting list
def fib_list():
    # initialize current Fibonacci object with correct upper limit
    current_fib = Fibonacci(lower_limit(), upper_limit())

    # create and print fibonacci list
    current_fib.populate_list()
    current_fib.display_list()


def fib_int():
    integer = set_integer()

    # the integer makes a handy upper limit
    current_fib = Fibonacci(0, integer)
    current_fib.populate_list()

    # if integer is found in Fibonacci numbers list, return True, the integer, and number's location in the sequence
    if integer in current_fib.fib_list:
        return True, integer, (current_fib.fib_list.index(integer) + 1)
    # or return False and just the integer
    else:
        return False, integer


print("\n****************************************")
print("****************************************")
print("**********      WELCOME!      **********")
print("****************************************")
print("****************************************")
print("**********     FIBONACCI      **********")
print("**********      NUMBERS       **********")
print("****************************************")
print("****************************************\n\n")

print("Welcome to the Fibonacci numbers tool. With this tool you can input an upper limit and see every Fibonacci "
      "number up to that limit. Or if you'd prefer, you can check if a certain number is a Fibonacci number.\n")

# begin loop to run program
while True:
    # check user input
    while True:
        user_decision_input = input(
            'If you want to see a list of all Fibonacci numbers with certain limits, press "L"\n'
            'If you want to check if an integer is a Fibonacci number, press "I"\n')
        if user_decision_input.upper() == "L":
            fib_list()
            break
        elif user_decision_input.upper() == "I":
            fib_answer = fib_int()
            if fib_answer[0]:
                print(f'Yes, {fib_answer[1]} is a Fibonacci number! It is number {fib_answer[2]} in the sequence.\n')
            else:
                print(f'Sorry, {fib_answer[1]} is not a Fibonacci number.\n')
            break
        else:
            print('Please enter "L" to see a list of Fibonacci numbers or "I" to check an integer\n')
    go_again_input = input(
        "Would you like to use the Fibonacci tool again? Press \"N\" to stop or any other key to continue.\n")
    if go_again_input.upper() == "N":
        break
