import random

def get_random_word():
    word_list = ['python', 'developer', 'internship', 'hangman', 'project', 'keyboard', 'program']
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            incorrect_guesses += 1
            print("Wrong guess.")

    else:
        print("\nGame over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
