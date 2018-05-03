import random


class HumanGame:

    def __init__(self):
        self.number = random.randint(1, 101)
        self.play()
    
    def check_number(self, guess):
        if not guess.isnumeric():
            return None
        else:
            guess_number = int(guess)
            if guess_number < 1 or guess_number > 100:
                return None
            if guess_number == self.number:
                return 0
            elif guess_number < self.number:
                return -1
            return 1
    
    def play(self, guess):
        print("\nI thought in a number between 1 and 100")
        guess = input("\nCan you guess it?: ")
        result = self.check_number(guess)
        while result != 0:
            if result == 1:
                new_guess = input("The number I've thought is LOWER: ")
            elif result == -1:
                new_guess = input("The number I've thought is GREATER: ")
            else:
                new_guess = input("Please, enter a number between 1 and 100: ")
            result = self.check_number(new_guess)
        print("\nCongratulations, you won!\n")
        
game = HumanGame()