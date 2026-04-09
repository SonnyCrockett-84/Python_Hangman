# Python Hangman Game

A classic Hangman game implemented in Python, offering both a terminal-based (CLI) experience and a graphical user interface (GUI) using Tkinter.

## Features

- **Dual Modes:** Choose between a classic command-line experience or a modern graphical interface.
- **Dynamic Word Selection:** Uses a built-in list or an extensive dictionary file (`dictionary.txt`) for varied gameplay.
- **Visual Feedback:** Animated ASCII art in the console and visual progress in the GUI.
- **Input Validation:** Detects duplicate guesses and invalid characters to ensure smooth gameplay.
- **Replayability:** Easy "play again" options to start a new round immediately.

![Hangman Project](img/Hangman%20Projekt.png)

## Project Structure

- `hangman_advanced.py`: The main script for the command-line (CLI) version.
- `gui.py`: The graphical user interface version built with Tkinter.
- `hangmanpics.py`: Contains the ASCII art graphics for the hangman stages.
- `randomWords.py`: Logic for selecting random words from lists.
- `menus.py` & `userInput.py`: Helper functions for menus and user input handling.
- `dictionary.txt`: A comprehensive word list for the game.

## Installation & Setup

### Prerequisites

Ensure you have Python 3 installed on your system. The GUI version requires `tkinter`, which is typically included with standard Python installations.

### Running the CLI Version

Open your terminal, navigate to the project directory, and run:

```bash
python hangman_advanced.py
```

### Running the GUI Version

To play with the graphical interface, run:

```bash
python gui.py
```

## How to Play

1. The game selects a secret word at random.
2. Guess letters one by one to reveal the word.
3. Each incorrect guess brings you closer to the "hangman" limit.
4. You have 6 attempts before the game ends.
5. Win by guessing the full word before running out of lives!

## License

This project was created for educational purposes. Feel free to use, modify, or extend it for your own projects.
