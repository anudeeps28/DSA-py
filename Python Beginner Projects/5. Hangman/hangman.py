import random

def choose_word():
    """Selects and returns a random word from the predefined list."""
    words = ['python', 'java', 'programming', 'hangman', 'challenge']
    return random.choice(words)

def display_hangman(tries):
    """Returns the current state of the hangman as an ASCII art string based on wrong tries."""
    stages = [
        # Stage 0: no wrong guesses
        """
           --------
           |      |
           |      
           |     
           |      
           |     
           -
        """,
        # Stage 1: head
        """
           --------
           |      |
           |      O
           |     
           |      
           |     
           -
        """,
        # Stage 2: head and body
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        # Stage 3: one arm added
        """
           --------
           |      |
           |      O
           |     \\|
           |      
           |     
           -
        """,
        # Stage 4: second arm added
        """
           --------
           |      |
           |      O
           |     \\|/
           |      
           |     
           -
        """,
        # Stage 5: one leg added
        """
           --------
           |      |
           |      O
           |     \\|/
           |     / 
           |     
           -
        """,
        # Stage 6: full figure (loss)
        """
           --------
           |      |
           |      O
           |     \\|/
           |     / \\
           |     
           -
        """
    ]
    return stages[tries]

def play_game():
    """Executes one complete game of Hangman."""
    word = choose_word()
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()   # Letters guessed so far
    wrong_guesses = 0
    max_wrong = 6  # Maximum allowed wrong guesses (stages 0-6)

    # Create a display list for the word with underscores for unguessed letters.
    display_word = ['_' for _ in word]

    while wrong_guesses < max_wrong and '_' in display_word:
        print(display_hangman(wrong_guesses))
        print(f"Word: {' '.join(display_word)}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        
        # Input handling and validation
        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try another one.\n")
            continue

        guessed_letters.add(guess)
        
        # Update game state
        if guess in word_letters:
            for idx, letter in enumerate(word):
                if letter == guess:
                    display_word[idx] = guess
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")
    
    # End-of-game messaging
    if '_' not in display_word:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(display_hangman(wrong_guesses))
        print(f"Sorry, you lost. The word was: {word}")

def main():
    """Main loop to run and potentially restart the game."""
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == '__main__':
    main()
