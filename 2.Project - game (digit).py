from random import randint

def guess_number():
    num = randint(1, 1000)
    max_attempts = 10
    i = 0

    print("A number between 1 and 1000 has been chosen. Try to guess it!")
    print("You have 10 attempts.\n")

    while i < max_attempts:
        i += 1
        try:
            guess = int(input(f"Attempt {i}/{max_attempts}. Enter your guess (Only integers allwoed): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        
        if guess == num:
            print(f"Congratulations! You guessed the number {num}.")
            break
        elif guess > num:
            print("Too high.")
        else:
            print("Too low.")
    else:
        print(f"Unfortunately you lost you've reached the maximum number of attempts.")
        print(f"The correct number was {num}. You can try again!")

    print("\nGame Over!")

guess_number()