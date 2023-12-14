# Wordle-Term

Wordle-Term is a command-line game inspired by the popular game Wordle. It allows you to guess a hidden word by entering different combinations of letters.

## How to Play

1. Clone the repository:
    ```
    git clone https://github.com/Pigiotyreal/Wordle-Term
    ```

2. Navigate to the project directory:
    ```shell
    cd Wordle-Term
    ```

3. Run the game:
    ```shell
    python wordleterm.py
    ```

4. Enter your guesses by typing a combination of letters and pressing Enter.

5. The game will provide feedback on your guess:
    - Gray: Letter is not in the word
    - Yellow: Letter is in the word, but not in the correct position
    - Green: Letter is in the word and in the correct position

6. Keep guessing until you find the word or run out of attempts.

## Command-line Arguments

The game supports the following command-line argument:

- `--show-word`: By default, the word is not displayed, use this argument to reveal the word at the start of the game.

To use the `--show-word` argument, run the game with the following command:
```shell
python wordleterm.py --show-word
```

## Contributing
We welcome contributions to this project. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## TODO
- [ ] Add support for custom wordlists
- [ ] Make the game more intuitive

## License
This project is licensed under the terms of the [MIT License](LICENSE).