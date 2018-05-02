import random


class HumanGame:

    def __init__(self):
        self.number = random.randint(1, 101)
    
    def check_number(self, guess):
        if not guess.isnumeric():
            raise ValueError("number should be between 1 and 100")
        else:
            guess_number = int(guess)
            if guess_number < 1 or guess_number > 100:
                raise ValueError("number should be between 1 and 100")
            if guess_number == self.number:
                return 0
            elif guess_number < self.number:
                return -1
            return 1