import random

def guess_the_number():
    print("\n🎯 Welcome to the Guess the Number Game! 🎯")
    print("I have chosen a number between 1 and 100. Can you guess it?\n")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get user's guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if user_guess < target_number:
                print("🔼 Too low! Try again.")
            elif user_guess > target_number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {target_number} in {attempts} attempts. 🎉")
                break  # Exit the loop if the guess is correct

        except ValueError:
            print("⚠️ Invalid input! Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    guess_the_number()
