from src.guessingbrite import PlayGame
from src.computergame import ComputerGame
from src.humangame import HumanGame


class TestPlayGame:

    def setup_method(self):
        self.game = PlayGame()

    def test_human_game(self):
        self.game.start_game("1")
        assert isinstance(self.game.mode, HumanGame)
    
    def test_computer_game(self):
        self.game.start_game("2")
        assert isinstance(self.game.mode, ComputerGame)