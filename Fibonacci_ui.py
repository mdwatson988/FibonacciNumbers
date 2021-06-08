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
      "number up to that limit.\n")

# begin loop to run program
while True:

    # initialize current Fibonacci object with correct upper limit
    current_fib = Fibonacci(lower_limit(), upper_limit())

    # create and print fibonacci list
    current_fib.populate_list()
    current_fib.display_list()

    go_again_input = input(
        "Would you like to see another Fibonacci list? Press \"N\" to stop or any other key to continue.\n")
    if go_again_input.upper() == "N":
        break
