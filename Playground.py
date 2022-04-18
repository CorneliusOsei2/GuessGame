from Intro import Intro
from Game import Game

class Playground:

    def __init__(self, low, high):
        self.intro = Intro()

        # Print greeting
        self.intro.greet()
        self.game = Game(low, high)
        self.game.start_game()



    