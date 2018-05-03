from src.games import Game
from src.humangame import HumanGame
from src.computergame import ComputerGame

class TestGames:

    def setup_method(self):
        self.game = Game()

    def test_start_game(self):
        assert self.game.finished is False
    
    def test_human_game(self):
        self.game.start_game(1)
        assert isinstance(self.game.mode, HumanGame)
    
    def test_computer_game(self):
        self.game.start_game(2)
        assert isinstance(self.game.mode, ComputerGame)