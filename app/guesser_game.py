from random import sample
from app.const import DIGITS, SIZE
from .game import Game


class GuesserGame(Game):
    def __init__(self):
        self.secret_number = self.generate_secret()

    def generate_secret(self):
        secret_number = ''.join(sample(DIGITS, SIZE))
        return secret_number

    def validate_guess(self, guess):
        if len(guess) != SIZE or len(set(guess)) != SIZE:
            print('You did not put a number with {} unique digits.'.format(
                SIZE), 'Try again.')
            return False
        return True

    def play(self):
        attemps = 1
        while True:
            guess = Game.valid_input(
                '\nGuess {}: Enter a {}-digit number --> '.format(
                    attemps, SIZE))
            if not self.validate_guess(guess):
                continue
            result = self.check_numbers(guess, self.secret_number)
            if self.is_over(result):
                break
            print('You got {} good and {} regular. Try again.'.format(
                result['good'], result['regular']))
            attemps += 1
