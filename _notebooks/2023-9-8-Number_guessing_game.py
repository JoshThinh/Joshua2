import random

secret_number = random.randint(1, 10)

attempts = 0

print("Welcome to my guessing game!")
print("I'm thinking of a number from 1 to 10.")

while True:
    guess = int(input("Guess my number!"))
    attempts += 1
    
    if guess > secret_number:
        print("Guess lower")
    
    elif guess < secret_number:
        print("Guess higher")
    
    else:
        print(f"Congratulations, you guessed my number {secret_number} in {attempts} attempts!!")
        break
        
    
    