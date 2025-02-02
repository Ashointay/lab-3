import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number = random.randint(1, 20)
    attempts = 0
    guess = None

    while guess != number:
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
    
    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")

guess_the_number()
