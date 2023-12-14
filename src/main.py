from colorama import init, Fore
from words import words
import random

init(autoreset=True)
word = random.choice(list(words))

print(Fore.GREEN + "Welcome to Wordle-Term!")
print(Fore.LIGHTMAGENTA_EX + "How to play: " + Fore.RESET + "\nGuess the five letter word in 6 tries or less!\nOnce you guess your first word, 3 colors will appear:\nGray: Letter is not in the word\nYellow: Letter is in the word, but not in the correct position\nGreen: Letter is in the word and in the correct position\nGood luck!\n")
print(Fore.LIGHTBLUE_EX + f"word: {word}")

input("Press enter to continue...")
print("\n" * 100)

guesses = 0
while guesses < 6:
    guess = input("Enter your guess: ")
    
    if guess == word:
        print(Fore.GREEN + "Congratulations! You guessed the word correctly!")
        break
    
    if len(guess) != len(word):
        print(Fore.RED + "Please enter a word that is 5 letters long.")
        continue
    
    guesses += 1
    
    table = ""
    for i in range(len(word)):
        if guess[i] == word[i]:
            table += Fore.GREEN + f"|{guess[i]}|"
        elif guess[i] in word:
            table += Fore.YELLOW + f"|{guess[i]}|"
        else:
            table += Fore.LIGHTBLACK_EX + f"|{guess[i]}|"
    table += "\n"
    
    print(table)
else:
    print(Fore.RED + "You ran out of guesses! The word was: " + word)

