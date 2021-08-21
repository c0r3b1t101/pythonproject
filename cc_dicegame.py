
import random

high_score = 0


def dice_game():

    global high_score

    choice = "1"

    while choice == "1":
        print("Current High Score:", high_score,
              " \n1) Roll Dice \n2) Leave Game")
        choice = input("Enter your choice: ")

        if choice == "1":
            roll1 = random.randint(1, 6)
            print("You roll a...", roll1)
            roll2 = random.randint(1, 6)
            print("You roll a...", roll2)

            total_roll = roll1 + roll2
            print("You rolled a total of:", total_roll)

            if high_score < total_roll:
                high_score = total_roll
                print("New High Score!\n")
        elif choice == "2":
            print("Thank you for playing!")
            break


dice_game()
