from humangame import HumanGame
from computergame import ComputerGame


class Game:

    def __init__(self):
        self.finished = False
        self.select_mode()
        
    def select_mode(self):
        print("\n__ Welcome to guessingBrite __")
        print("\nIn this game someone has to guess a number between 1 and 100")
        print("\nThere are two game modes:\
                \n\t[1] - You guess the number I thought.\
                \n\t[2] - I guess the number you thought.")
        mode = ""
        while mode not in ["1", "2"]:
            mode = input("\nEnter 1 or 2 to select the game mode: ")
        self.start_game(mode)
    
    def start_game(self, mode):
        if mode == 1:
            self.mode = HumanGame()
        else:
            self.mode = ComputerGame()

Game()