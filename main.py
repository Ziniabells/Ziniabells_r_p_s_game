from random import choice

options = ["R", "P", "S"]

tie = True

while tie:
    cpu = choice(options)

    user = input("""Enter your choice
    "R" for Rock
    "P" for Paper
    "S" for Scissors: """)

    if user.upper() not in options:
        print("Error: Your input should be one of 'R', 'P', 'S'")
        continue

