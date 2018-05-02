from src.computergame import ComputerGame


class TestComputerGame:

    def test_computer_guess_a_number_between_1_and_100(self):
        self.game = ComputerGame()
        assert self.game.number >= 1 and self.game.number <= 100