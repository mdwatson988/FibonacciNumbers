class Fibonacci:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.fib_list = [0, 1]

    # recursive method to calculate and store all Fib numbers up to limit, first two numbers are always 0 and 1
    def populate_list(self):
        next_number = self.fib_list[-1] + self.fib_list[-2]
        # upper and lower limit function ensures limits are greater than 0 so no edge cases to handle
        # base case ends recursive step
        if next_number > self.upper_limit:
            # finally, remove list values lower than lower limit
            while self.fib_list[0] < self.lower_limit:
                self.fib_list.pop(0)
            # end function call
            return
        # first, recursively populate list until upper limit reached
        else:
            self.fib_list.append(next_number)
            return self.populate_list()

    # method to display the fibonacci list
    def display_list(self):
        print(f"\nThe Fibonacci sequence with an upper limit of {self.upper_limit} is: {self.fib_list}\n")
