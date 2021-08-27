import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []
while diamonds:
    choice = input(
        "press enter to pick a card or type Q and press enter to quit")

    if choice == "":
        card = random.randint(0, len(diamonds)-1)
        hand.append(diamonds[card])
        print(f"Your card is {diamonds[card]}")
        diamonds.pop(card)
        print(f"Cards remaining in deck: {diamonds}")
        print(f"Your hand is: {hand}")
    elif choice.lower() == "q":
        break
    else:
        print("Please enter a valid function")
if not diamonds:
    print("There are no more cards to pick.")
