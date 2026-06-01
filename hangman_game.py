import random

words = ["python", "apple", "tiger", "ocean", "music", "letter", "flower", "carrot", "doctor", "street", "mother"]

print("================================")
print("      WELCOME TO HANGMAN")
print("================================")

play_again = "yes"

while play_again == "yes":

    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_guesses = 6

    print("\nA new game has started!")
    print(f"You have {max_guesses} incorrect guesses.\n")

    while incorrect_guesses < max_guesses:

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)

        # Check if player won
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        guess = input("Enter a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Correct guess!")
        else:
            incorrect_guesses += 1
            remaining = max_guesses - incorrect_guesses
            print("❌ Wrong guess!")
            print("Remaining incorrect guesses:", remaining)

    # Check if player lost
    if incorrect_guesses == max_guesses:
        print("\n💀 Game Over!")
        print("The word was:", secret_word)

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\nThanks for playing Hangman. Goodbye!")