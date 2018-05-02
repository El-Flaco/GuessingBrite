from src.humangame import HumanGame

class TestHumanGame:

    def test_new_game_generates_number_between_1_and_100(self):
        self.game = HumanGame()
        assert self.game.number >= 1 and self.game.number <= 100