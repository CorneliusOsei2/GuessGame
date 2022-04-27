
import time, sys

class Intro:

    message = '''
           |||||||      |||      |||   ||||||||||      ||||||        ||||||
        |||       |||   |||      |||   |||           |||     |||   |||    |||
        |||             |||      |||   |||           |||           |||
        |||             |||      |||   ||||||||||      ||||||        ||||||
        |||     |||||   |||      |||   ||||||||||            |||          |||
        |||       |||   |||      |||   |||           |||     |||   |||     |||
        |||       |||   |||      |||   |||           |||     |||   |||     |||
           |||||||         ||||||      ||||||||||       |||||         |||||

'''  
        


    def greet(self):
        for letter in Intro.message:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.005)
        
        # Get player info
        player = input("What is your name: ")
        print("You are so welcome to Guess, Player ", player, "😃")
