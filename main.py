from random import choice

options = ["R", "P", "S"]


while True:
    computer = choice(options)

    user = input("""Enter your choice
    "R" for Rock
    "P" for Paper
    "S" for Scissors: """)

    print(f"\n\nUser {user} : Computer: {computer}\n\n")

    if user.upper() not in options:
        print("Error: Your input should be one of 'R', 'P', 'S'")
        continue

    else:
        if user.upper() == computer.upper():
            print("YOU DRAW: Play again/n")
            continue

        elif (user.upper() == "R") and (computer.upper() == "S"):
                print("YOU WON!!!")
                break

        elif (user.upper() == "R") and (computer.upper() == "P"):
            print("YOU LOOSE!!!")
            break

        elif (user.upper() == "P") and (computer.upper() == "S"):
            print("YOU LOOSE!!!")
            break

        elif (user.upper() == "P") and (computer.upper() == "R"):
            print("YOU WON!!!")
            break

        elif (user.upper() == "S") and (computer.upper() == "P"):
            print("YOU WON!!!")
            break
        elif (user.upper() == "S") and (computer.upper() == "R"):
            print("YOU LOOSE!!!")
            break     