import random

word_list = ["cherry", "tangerine", "pineapple", "banana", "kiwi"]

class Hangman: 
    def __init__(self, word_list, num_lives=5):
        """
        Initialise Hangman game. 
        
        Parameters: 
        - word_list (list): List of words that can be picked.
        - word (str): The randomly chosen word from word_list.
        - word_guessed (list): A list of letters in word
        - num_letters (int): The number of unique letters in the word that have not been guessed yet.
        - num_lives (int): Number of lives the player has.
        - list_of_guesses (list): A list of the guesses that have been made.
        """
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives 
        self.list_of_guesses = []
        pass
    def _check_guess(self, guess):
        """
        Method which checks that the guessed letter is in the word, then updates word_guessed, num_letters and num_lives accordingly. 
        
        Parameters: 
        - guess (str): The guessed letter
        """
        guess = guess.lower()
        if guess in self.word: 
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1 
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        """
        Method which asks the user for input, verifies that the input is valid and then calls the check_guess method before ammending list_of_guesses.
        """
        while True:
            guess = input("Please guess a letter: ")
            if not guess.isalpha() or len(guess) != 1: 
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else: 
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True: 
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}. Play again?")
            break

        if game.num_letters > 0:
            game.ask_for_input()
        else: 
            print(f"Congratulations! The word was {game.word}. You won!")
            break

play_game(word_list)





    