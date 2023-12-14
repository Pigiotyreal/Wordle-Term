from colorama import init, Fore, Back, Style
from words import words
import random

init(autoreset=True)
word = random.choice(list(words))

print(Fore.GREEN + "Welcome to Wordle-Term!")
print(Fore.LIGHTBLUE_EX + f"word: {word}")