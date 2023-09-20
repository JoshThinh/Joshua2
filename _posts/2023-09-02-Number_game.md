---
toc: true
comments: false
layout: post
title: Number Game
description: Plan!!! Analyze hacks and plan.
type: hacks
courses: { compsci: {week: 3} }
---

```python
import random

def main():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print("Please enter a valid number within the specified range.")
                continue

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
def read_and_execute_md(md_file):
    with open(md_file, "r") as file:
        code_block = ""
        in_code_block = False

        for line in file:
            if line.strip() == "```python":
                in_code_block = not in_code_block
                continue

            if in_code_block:
                code_block += line
            elif code_block.strip():
                exec(code_block, globals())
                code_block = ""

if __name__ == "__main__":
    read_and_execute_md("game.md")