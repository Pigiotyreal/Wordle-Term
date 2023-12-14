from colorama import init, Fore, Back, Style
from words import words
import random

init(autoreset=True)
word = random.choice(list(words))

print(Fore.GREEN + "Welcome to Wordle-Term!")
print(Fore.LIGHTMAGENTA_EX + "How to play: " + Fore.RESET + "\nGuess the five letter word in 6 tries or less!\nOnce you guess your first word, 3 colors will appear:\nGray: Letter is not in the word\nYellow: Letter is in the word, but not in the correct position\nGreen: Letter is in the word and in the correct position\nGood luck!\n")
print(Fore.LIGHTBLUE_EX + f"word: {word}")