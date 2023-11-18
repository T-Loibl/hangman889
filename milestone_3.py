import random

word_list = ["cherry", "passion fruit", "pineapple", "banana", "kiwi"]
word = random.choice(word_list)

print(word)


def check_guess(guess, word):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        return True
    else: 
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        guess = input("Please enter a single letter.")

        if guess.isalpha() and len(guess) == 1:
            check_guess(guess, word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()