import random
lowest_number = 1
highest_number = 100
guesses = 0
answer = random.randint(lowest_number,highest_number)
is_running =True
print("Lets play python Number Guessing Game!")
print(f"Select the number between {lowest_number} to {highest_number}")


while is_running:
    guess = input("Enter your Guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1

        if guess < lowest_number or guess > highest_number:
            print("The Number is out of range")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print("Correct!!!")
            is_running = False
    else:
        print("Please enter Correct Number")


print(f"Number of guesses:{guesses}")