from src.computergame import ComputerGame


class TestComputerGame:

    def setup_method(self):
        self.game = ComputerGame()
        self.game.guess()

    def test_computer_guess_a_number_between_1_and_100(self):
        assert self.game.number >= 1 and self.game.number <= 100
    
    def test_guess_a_greater_number_after_a_lower_guess(self):
        previous_guess = self.game.number
        self.game.check_guess(">")
        self.game.guess()
        assert self.game.number > previous_guess
    
    def test_guess_a_lower_number_after_a_greater_guess(self):
        previous_guess = self.game.number
        self.game.check_guess("<")
        self.game.guess()
        assert self.game.number < previous_guess
    
    def test_number_is_1(self):
        while self.game.number != 1:
            self.game.check_guess("<")
            self.game.guess()
        assert self.game.number == 1
    
    def test_number_is_100(self):
        while self.game.number != 100:
            self.game.check_guess(">")
            self.game.guess()
        assert self.game.number == 100
    
    def test_guess_the_correct_number(self):
        assert self.game.check_guess("=") == 1
    
    def test_wrong_comparator(self):
        assert self.game.check_guess("9") == None