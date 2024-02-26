import random

def choose_word():
    words = ["car", "house", "python", "stepgeorgia", "school"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def check_word(guess, word):
    return guess == word

def hangman():
    word = choose_word()
    max_attempts = 10
    guessed_letters = []
    attempts = 0
    
    print("Welcome to the best game - Hangman!")
    print("Try to guess chosen word...")
    
    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Enter a letter or guess the whole word: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try another one.")
                continue
            guessed_letters.append(guess)
            if guess in word:
                print("Correct guess!")
            else:
                attempts += 1
                print("Incorrect guess!")
                print(f"Attempts remaining: {max_attempts - attempts}")
        elif len(guess) > 1 and guess.isalpha():
            if check_word(guess, word):
                print("\nCongratulations! You've won and guessed the word:", word)
                break
            else:
                attempts += 1
                print("Incorrect guess!")
                print(f"Attempts remaining: {max_attempts - attempts}")
        else:
            print("Invalid input. Please enter a single letter or guess the whole word.")
            continue
        
        if set(word) <= set(guessed_letters):
            print("\nCongratulations! You've won and guessed the word:", word)
            break
        elif attempts == max_attempts:
            print("\nSorry, you've run out of attempts and lost :(")
            print("The word was:", word)
            break

hangman()