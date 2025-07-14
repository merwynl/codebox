
# Number guessing game
import random

lowest = 1
highest = 100
answer = random.randint(lowest, highest)
guesses = 0
is_running = True

print("Welcome to Number Guesser")
print(f"Select a number between {lowest } and {highest}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        if guess < lowest or guess > highest:
            print("Out of range!")
            print(f"Select a number between {lowest} and {highest}")
        elif guess < answer:
            print("Too low! Try again!")
        elif  guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Congrats! The answer is {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print ("Invalid guess!")
        print(f"Select a number between {lowest} and {highest}")