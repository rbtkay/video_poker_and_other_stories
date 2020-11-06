import random


def first_draw(cards):
    hand = []
    for _ in range(0, 5):
        if len(cards) <= 0:
            break

        select_card = random.choice(cards)
        hand.append(select_card)
        cards.remove(select_card)

    return hand


def second_draw(cards_to_keep, cards_deck):
    number_missing_card = 5 - len(cards_to_keep)
    for _ in range(number_missing_card):
        select_card = random.choice(cards_deck)
        cards_to_keep.append(select_card)
        cards_deck.remove(select_card)

    return cards_to_keep


def choose_cards_to_keep(hand):
    print(f"\nYour hand: {hand}")
    cards_to_keep = []

    while True:
        choice = input("\nDo you want to keep some cards ? (Y/N)")
        if(type(choice) is str and (choice.lower() == "y" or choice.lower() == "n")):
            break
        else:
            print("wrong input")

    i = 0
    while choice.lower() == "y":
        chosen_index = int(input("\nChoose the card you want to keep (using the index)"))  # TODO: check that the input is a number

        cards_to_keep.append(hand.get(chosen_index))
        del hand[chosen_index]
        print(f"You chose to keep: {cards_to_keep}")

        print(f"Keep another card ? (Y/N)")
        answer = input("Y/N: ").lower()

        if answer == "n":
            break

        print(f"remaining cards to choose from {hand}")

        i = i + 1
        if i > 4:
            break

    return cards_to_keep
