import random

def computer_guesses_number():
    print("\n🎯 Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Computer guesses the middle number
        user_feedback = input(f"Is your number {guess}? (Enter 'h' for too high, 'l' for too low, 'c' for correct): ").lower()

        if user_feedback == 'c':
            print(f"🎉 I guessed your number {guess} in {attempts} attempts! 🎉")
            break
        elif user_feedback == 'h':
            high = guess - 1  # Narrow the range to lower half
        elif user_feedback == 'l':
            low = guess + 1  # Narrow the range to upper half
        else:
            print("⚠️ Invalid input! Please enter 'h' (too high), 'l' (too low), or 'c' (correct).")

if __name__ == "__main__":
    computer_guesses_number()
