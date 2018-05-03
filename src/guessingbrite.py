from humangame import HumanGame
from computergame import ComputerGame


class PlayGame:

    def __init__(self):
        self.select_mode()
        
    def select_mode(self):
        print("\n__ Welcome to guessingBrite __")
        print("\nIn this game someone has to guess a number between 1 and 100")
        print("\nThere are two game modes:\
                \n\t[1] - You guess the number I thought.\
                \n\t[2] - I guess the number you thought.\
                \n\t[Q] - EXIT -> ")
        mode = ""
        while mode not in ["1", "2", "q", "Q"]:
            mode = input("\nSelect an option to play: ")
        if mode in ["q", "Q"]:
            return
        self.start_game(mode)
    
    def start_game(self, mode):
        if mode == "1":
            self.mode = HumanGame()
        else:
            self.mode = ComputerGame()
        self.mode.play()
        PlayGame()

PlayGame()