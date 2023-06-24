# Create terminal-based hangman game
from pics import hangman_pics
from word_dict import words
import random


class Hangman:
    def __init__(self):
        self.prompt()
        
    def prompt(self):
        '''Sets game to default start; prompts user for guess'''
        self.word = words[random.randint(0, len(words) - 1)]
        self.total_attempts = 0
        self.correct_guesses = []
        self.wrong_guesses = []

        print("\n\nWelcome to a new start!\n")

        while True:
            # Prints unknown/known letters and hangman drawing
            print(
            f"{hangman_pics[self.total_attempts]}\n"
            f"{Hangman.update(self)}\n"
            )
            
            self.u_guess = input("Guess a letter: ")

            # Checks if user's guess is correct
            self.guess()
    

    def replay(self):
        '''Prompts user to replay'''
        u_input = input("Replay (y/n)? ")
        if u_input.lower() == 'y':
            self.prompt()
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
            self.replay()


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
                self.update()
                
            elif self.u_guess.lower() in self.wrong_guesses:
                print(f"You've already guessed '{self.u_guess},' which was revealed to be wrong.")

            else:
                self.wrong_guesses.append(self.u_guess.lower())
                print("Wrong")
                self.hang()
        else:
            print(f"'{self.u_guess}' was already revealed as a correct guess, try a different letter.")

    
    def update(self):
        '''Updates word displayed to accurately present up-to-date information'''
        self.unknown_word = self.word

        # Updates word displayed
        for letter in self.word:
            if letter not in self.correct_guesses:
                if letter == ' ':
                    continue

                # Replaces all unknown letters with '_'    
                else:
                    self.unknown_word = self.unknown_word.replace(letter, "_ ")
            else:
                continue
        
        # Checks if user revealed all the letters
        if self.unknown_word == self.word:
            print(
                f"\nThe word was: {self.word}"
                "\nYOU WIN!"
            )
            self.replay()
            
        return self.unknown_word

    
if __name__ == '__main__':
    Hangman()
