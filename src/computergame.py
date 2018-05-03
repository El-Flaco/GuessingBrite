import random


class ComputerGame:

    def __init__(self):
        self.min_limit = 1
        self.max_limit = 100
        self.numbers = []

    @property
    def number(self):
        return self.numbers[-1] if self.numbers else None

    def guess(self):
        if self.max_limit - self.min_limit > 1:
            guess = random.randint(self.min_limit, self.max_limit + 1)
        else:
            if self.number == self.max_limit:
                guess = self.min_limit
            else:
                guess = self.max_limit
        self.numbers.append(guess)
    
    def check_guess(self, comparator):
        if comparator == ">" or comparator == "+":
            self.min_limit = self.number + 1
            return 0
        elif comparator == "<" or comparator == "-":
            self.max_limit = self.number - 1
            return 0
        elif comparator == "=" or comparator == "y" or comparator == "Y":
            return 1
            
    def play(self):
        print("\nThink a number between 1 and 100, I will guess it")
        self.guess()
        comparator = input("\nYour number is " + str(self.number) + "?: ")
        result = self.check_guess(comparator)
        while result != 1:
            if result == None:
                print("Please enter > or + when your number is greater,\
                       \n\t< or - when your number is lower,\
                       \n\tand =, y or Y when it is the number.")
            else:
                self.guess()
            comparator = input("\nYour number is " 
                                    + str(self.number) + "?: ")
            result = self.check_guess(comparator)
        print("\nCongratulate me, I won!")