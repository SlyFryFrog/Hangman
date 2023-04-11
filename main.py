# Create terminal-based hangman game
from pics import hangman_pics
from word_dict import words
import random


class Hangman:
    def __init__(self):
        '''Sets game to default start; prompts user for guess'''
        self.word = words[random.randint(0, len(words) - 1)]
        self.total_attempts = 0
        self.correct_guesses = []
        self.wrong_guesses = []
        self.new_game_req = False
        
        get_new_token = True

        while True:
            
            # Checks if it's a new game
            if get_new_token:
                get_new_token = False
                print("\n\nWelcome to a new start!\n")
            
            
            # Prints unknown/known letters and hangman drawing
            print(
            f"{hangman_pics[self.total_attempts]}\n"
            f"{Hangman.update(self)}\n"
            )
            
            self.u_guess = input("Guess a letter: ")

            # Checks if user's guess is correct
            Hangman.guess(self)
            
            # Checks if user requested a new game
            if self.new_game_req:
                break
        
        # Prompts user for new game
        u_input = input("New game (y/n)? ")
                
        if u_input.lower() == 'y':
            Hangman()
        else:
            exit()
            

    def hang(self):
        '''Checks amount of attempts and updates drawing accordingly'''
        self.total_attempts = self.total_attempts + 1
        
        if self.total_attempts == len(hangman_pics) - 1:
            print(
                f"{hangman_pics[-1]}"
                f"\nThe word was: {self.word}"
                "\nGAME OVER!"
            )
            
            # Asks user if they want to play again
            self.new_game_req = True
        else:
            print(hangman_pics[self.total_attempts])


    def guess(self):
        '''Checks if users guess is valid, correcot, or incorrect'''
        if len(self.u_guess) > 1 or self.u_guess == ' ':
            print("Invalid guess")
            return
        
        if self.u_guess not in self.correct_guesses:
            # Checks if user input is correct and updates it accordingly
            if self.u_guess.lower() in self.word or self.u_guess.upper() in self.word:
                self.correct_guesses.append(self.u_guess.upper())
                self.correct_guesses.append(self.u_guess.lower())
                
                print("Correct")
                Hangman.update(self)
                
            elif self.u_guess.lower() in self.wrong_guesses:
                print(f"You've already guessed {self.u_guess}")

            else:
                self.wrong_guesses.append(self.u_guess.lower())
                print("Wrong")
                Hangman.hang(self)
        
        elif self.u_guess in self.correct_guesses:
            print(f"'{self.u_guess}' was already revealed as a correct guess, try a different letter.")
        
        else:
            print("Uknown error, exiting...")
            exit()
    
    def update(self):
        '''Updates word displayed to accurately present up-to-date information'''
        self.unknown_word = self.word

        # Updates word displayed
        for letter in self.word:
            if letter not in self.correct_guesses:
                if letter == ' ':
                    pass

                # Replaces all unknown letters with '_'    
                else:
                    self.unknown_word = self.unknown_word.replace(letter, "_")
            else:
                pass
        
        # Checks if user revealed all the letters
        if self.unknown_word == self.word:
            print(
                f"\nThe word was: {self.word}"
                "\nYOU WIN!"
            )
            self.new_game_req = True
            
        return self.unknown_word

    
if __name__ == '__main__':
    Hangman()