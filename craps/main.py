import random


def roll_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num = num1 + num2

    print("The sum of dice is", num1, "+", num2, "=", num)

    return num


def game():
    losing_numbers = [2, 3, 12]

    num = roll_dice()

    if num == 7 or num == 11:
        print("You won")
        return

    elif num in losing_numbers:
        print("You lose")
        return

    else:
        goal = num
        print("Now your goal number is", goal)

    while True:
        num = roll_dice()

        if num == goal:
            print("You won")
            break

        elif num == 7:
            print("You lose")
            break

game()