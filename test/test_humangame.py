import pytest

from src.humangame import HumanGame

class TestHumanGame:

    def setup_method(self):
        self.game = HumanGame()
    
    def test_new_game_generates_number_between_1_and_100(self):
        assert self.game.number >= 1 and self.game.number <= 100

    def test_users_input_is_a_number_between_1_and_100(self):
        result = self.game.check_number("50")
        assert result == 0 or result == 1 or result == -1
    
    def test_number_lower_than_1_throws_ValueError(self):
        with pytest.raises(ValueError):
            self.game.check_number("0")
            
    def test_number_greater_than_100_throws_ValueError(self):
        with pytest.raises(ValueError):
            self.game.check_number("200")
    
    def test_string_input_throws_ValueError(self):
        with pytest.raises(ValueError):
            self.game.check_number("two")