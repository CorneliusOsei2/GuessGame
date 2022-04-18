import random

class Game:

    def __init__(self, low, high):
        self.total_lives = 0
        self.low = low
        self.high = high
        self.target_num = random.randint(low, high)
        

    def start_game(self):
        # Get player info
        player = input("What is your name: ")
        print("You are so welcome to Guess, Player ", player, "😃")

        # Making sure the player provides the right value for total_lives
        while True:
            try:
                temp = int(input("How many lives do you want on this journey: "))

                if type(temp) == int and temp > 0:
                    self.total_lives = temp
                    print(temp, " you shall have! 😉")
                    break

                elif temp == 0:
                    print("Goodbye, you have no life.... 💀")
                    return

            except Exception as e:
                print("**** Your total lives must be a positive integer please ****🙂")

        # Load Game
        self.run_game()

    def run_game(self):
        
        print(
            "\n*******************************************************************************\n \nIn this game, you have " + "\u2764\uFE0F" *self.total_lives + " to correctly guess a number between " + str(self.low)+ " and " + str(self.high) + "\n \n********************************************************************************\n")
        
        warn_count = 0
        guess = ""

        # Run game so far as player has lives
        while True and self.total_lives:
            
            print("Total lives: " + "\u2764\uFE0F" *self.total_lives)

            try:
                temp = input("Enter your guess: ")
                guess = int(temp)
                self.total_lives -= 1

                if self.total_lives:
                    if guess == self.target_num:
                        print("🥳🥂🦅Amazing. You are FANTABULOUS! The Master is proud of you!🤓🙏🏽🚀")
                        return

                    elif guess < self.low or guess > self.high: print("Your guess is not even in the range😑")
                    elif guess > self.target_num: print("Your guess is higher😟")
                    else: print("Your guess is lower 😕")

            except:
                print("Your guess should be a positive Integer. I will not penalize you this one time")
                warn_count += 1

                if warn_count > 1:
                    print("Your guess should be a positive Integer. You lose 1 life, my friend!")
                    self.total_lives -= 1

        print("Better luck next time, Loser 👻")
        
