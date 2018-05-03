import random

class ComputerGame:

    def __init__(self):
        self.min_limit = 1
        self.max_limit = 100
        self.numbers = []
        self.guess()

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
            self.min_limit = self.number
        elif comparator == "<" or comparator == "-":
            self.max_limit = self.number
        elif comparator == "=":
            return 1
        else:
            None