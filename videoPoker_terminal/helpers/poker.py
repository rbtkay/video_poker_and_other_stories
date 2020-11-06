from helpers.draws import first_draw, second_draw, choose_cards_to_keep
from helpers.winning import calculate_points
from helpers.combinations import check_combination

def video_poker():
    deck = ['2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h', '2-d',
            '3-d',
            '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d', '2-c', '3-c', '4-c',
            '5-c',
            '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c', '2-s', '3-s', '4-s', '5-s', '6-s',
            '7-s',
            '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s']

    bankroll = int(input("What is your bankroll ? "))

    while bankroll > 0:
        try:
            bet = int(input("\nHow much for your bet ? (input -1 if you want to exit the game)"))
            if bet == -1:
                break

            if bet > bankroll:
                print("Your bet is higher than your bankroll")
            else:
                bankroll = start_game(deck, bet, bankroll)
        except ValueError:
            print("wrong input, your input should be a number")

    print(f"\nThe game is over, your bankroll is {bankroll}")


def start_game(all_cards, bet, bankroll):
    multiplier = machine(all_cards)
    bet_result = bet * multiplier

    print(f"\nYour {bet} became {bet_result}")

    remaining_bankroll = bankroll - bet + bet_result
    print(f"\n{remaining_bankroll} is remaining in your bankroll")
    return remaining_bankroll


def machine(cards_deck):
    initial_hand = first_draw(cards_deck)

    # print(cards_deck)
    cards_to_keep = choose_cards_to_keep(initial_hand)
    final_hand = second_draw(cards_to_keep, cards_deck)
    print("\nfinal hand - ", final_hand)

    combinations = check_combination(final_hand)

    print(combinations)
    return calculate_points(combinations)

