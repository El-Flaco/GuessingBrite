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
        self.numbers.append(random.randint(self.min_limit, self.max_limit + 1))
    
    def check_guess(self, comparator):
        if comparator == ">":
            self.min_limit = self.number
        elif comparator == "<":
            self.max_limit = self.number