# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and conditionals. You'll practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️	Select a Secret Word

#### Description
Use the `words` list in `starter-code.py` to randomly choose the word the player must guess.

#### Requirements
Completed program should:

- Randomly select a word from the predefined `words` list
- Store the selected word for use throughout the game

### 🛠️	Track Game State

#### Description
Set up the variables needed to keep track of the player's progress as they guess letters.

#### Requirements
Completed program should:

- Keep track of the letters guessed so far
- Count the number of incorrect guesses made
- Define a maximum number of allowed incorrect guesses

### 🛠️	Build the Guessing Loop

#### Description
Implement the main game loop that lets the player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Display the current progress using an underscore format (e.g., `_ _ _`) for unguessed letters
- Accept a letter guess from the player
- Update the game state based on whether the guess is correct or incorrect
- Repeat until the word is fully guessed or attempts are exhausted

### 🛠️	Display the Result

#### Description
Show the player whether they won or lost once the game ends.

#### Requirements
Completed program should:

- Display a win message when the word is fully guessed
- Display a lose message when incorrect guesses reach the maximum
- Reveal the secret word when the player loses
