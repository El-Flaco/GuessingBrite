from src.games import Game
from src.humangame import HumanGame

class TestGames:

    def setup_method(self):
        self.game = Game()

    def test_start_game(self):
        assert self.game.finished is False
    
    def test_human_game(self):
        assert isinstance(self.game.mode, HumanGame)