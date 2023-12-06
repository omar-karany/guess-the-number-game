import random

class NumberGuessingGame:
    def __init__(self):
        self.attempts_count = []
        self.pc_number = random.randint(1, 10)

    def welcome_message(self, user_name):
        print(f"Welcome {user_name} to the Number Guessing Game!")

    def display_high_score(self):
        if not self.attempts_count:
            print("There is no high score yet.")
        else:
            print(f"The high score in the game is after {min(self.attempts_count)} attempts.")

    def play_game(self, user_name):
        attempts = 0

        while True:
            try:
                user_number = int(input("Pick a number in the range '1 to 10': "))
                attempts += 1

                if user_number > 10 or user_number < 1:
                    raise ValueError(f"Invalid value, {user_name}! Please try again.")

                elif self.pc_number > user_number:
                    print("Your number is too low.")
                elif self.pc_number < user_number:
                    print("Your number is too high.")

                if user_number == self.pc_number:
                    self.attempts_count.append(attempts)
                    print(f"You win, {user_name}, after {attempts} attempts!")
                    ask = input("Do you want to continue the game? Answer 'y' or 'n': ")
                    if ask.lower() == "n":
                        self.display_high_score()
                        print(f"Goodbye, {user_name}!")
                        break
                    else:
                        attempts = 0
                        self.pc_number = random.randint(1, 10)
                        continue

            except ValueError as err:
                print(err)

if __name__ == "__main__":
    user_name = input("Enter your name, please: ")
    game = NumberGuessingGame()
    game.welcome_message(user_name)
    game.play_game(user_name)