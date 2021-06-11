from Fibonacci import Fibonacci
from files import *


# create functions used for program
def upper_limit():
    while True:
        upper_limit_input = input("\nEnter the upper limit for your Fibonacci numbers list: ")
        try:
            fib_upper_limit = int(upper_limit_input)
            if fib_upper_limit > 0:
                return fib_upper_limit
            else:
                print("Please enter a value greater than 0.")
        except ValueError:
            print("Please enter a whole number for your upper limit.")


def lower_limit():
    while True:
        lower_limit_input = input("\nEnter the lower limit for your Fibonacci numbers list: ")
        try:
            fib_lower_limit = int(lower_limit_input)
            if fib_lower_limit >= 0:
                return fib_lower_limit
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


def save_results(results_txt_path, result_string):
    while True:
        save_results_input = input('Would you like to save your results to the .txt file for later access? '
                                   'Press "Y" for "Yes" or "N" for "No": ')

        # if user wants to save the results
        if save_results_input.upper() == "Y":
            # open existing txt file using path from files.py
            text_file = open(results_txt_path, 'a')
            # write the results string to a new line on the file. string will already include an initial new line
            text_file.write(result_string)
            # close the file then break out of loop
            text_file.close()
            break

        # if user doesn't want to save, immediately break out of loop
        elif save_results_input.upper() == "N":
            break
        else:
            print('Press "Y" to save your results or "N" to skip saving results.')


# function for user manually setting upper/lower limit and seeing resulting list
def fib_list():
    # set and check limits
    while True:
        lower = lower_limit()
        upper = upper_limit()

        # if lower limit is larger than upper, get new limits
        if lower >= upper:
            print("\nPlease ensure your lower limit is smaller than your upper limit.")
        else:
            break

    # initialize current Fibonacci object with correct limits
    current_fib = Fibonacci(lower, upper)

    # create and print fibonacci list
    current_fib.populate_list()
    print(current_fib.return_list())

    # check if user wants to save results. if so, save result list string to the .txt file
    save_results(txt_path, current_fib.return_list())


def fib_int():
    integer = set_integer()

    # the integer makes a handy upper limit
    current_fib = Fibonacci(0, integer)
    current_fib.populate_list()

    # if integer is found in Fibonacci numbers list, return True, the integer, and number's location in the sequence
    if integer in current_fib.fib_list:
        fib_answer = [True, integer, (current_fib.fib_list.index(integer) + 1)]
    # or return False and just the integer
    else:
        fib_answer = [False, integer]

    # create answer string using method in Fibonacci class
    answer_string = current_fib.return_integer_answer(fib_answer)

    # print results
    print(answer_string)

    # check if user wants to save results. if so, save integer answer string to the .txt file
    save_results(txt_path, answer_string)


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
        # if user chose the fib list, run fib list function
        if user_decision_input.upper() == "L":
            fib_list()
            # break out of user input loop to check if user wants to go again
            break
        # if user chose the fib integer, run integer function
        elif user_decision_input.upper() == "I":
            fib_int()
            # break out of user input loop to check if user wants to go again
            break
        # go back to user input if anything other than L or I entered
        else:
            print('Please enter "L" to see a list of Fibonacci numbers or "I" to check an integer\n')
    go_again_input = input(
        "\nWould you like to use the Fibonacci tool again? Press \"N\" to stop or any other key to continue.\n")
    # break out of program loop if user doesn't want to continue
    if go_again_input.upper() == "N":
        break
