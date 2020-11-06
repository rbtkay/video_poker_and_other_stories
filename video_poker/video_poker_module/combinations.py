

def check_combination(final_hand):
    possible_pairs_or_three_of_kind = count_number_of_cards(final_hand)
    combination = {
        "Paire": 0,
        "Brelan": 0,
        "Quinte": 0,
        "Flush": 0,
        "Full": 0,
        "Carre": 0,
        "QuinteFlush": 0,
        "RoyalFlush": 0
    }

    for key in possible_pairs_or_three_of_kind.keys():
        if possible_pairs_or_three_of_kind[key] == 2:
            combination["Paire"] += 1
        if possible_pairs_or_three_of_kind[key] == 3:
            combination["Brelan"] += 1
        if possible_pairs_or_three_of_kind[key] == 4:
            combination["Carre"] += 1

    if combination["Paire"] == 1 and combination["Brelan"] == 1:
        combination["Full"] = 1
    if is_quinte(final_hand):
        combination["Quinte"] = 1
    if is_flush(final_hand):
        combination["Flush"] = 1
    if is_flush(final_hand) and is_quinte(final_hand):
        combination["QuinteFlush"] = 1
    if is_flush(final_hand) and is_quinte(final_hand) and sort_hand(final_hand)[0] == 10:
        combination["RoyalFlush"] = 1

    return combination


def count_number_of_cards(final_hand):
    possible_pairs = dict()

    for card in final_hand:
        card_value = card.split('-')[0]
        if card_value not in possible_pairs:
            possible_pairs[card_value] = 0

    for card in final_hand:
        card_value = card.split('-')[0]
        possible_pairs[card_value] += 1

    return possible_pairs



def is_quinte(cards):
    serie_a_begin = sort_hand(cards)[0]
    serie_a_end = sort_hand(cards)[1]

    for index in range(len(serie_a_begin)):
        if index != 0:
            if int(serie_a_begin[index]) - int(serie_a_begin[index - 1]) != 1:
                for i in range(len(serie_a_end)):
                    if i != 0:
                        if int(serie_a_end[index]) - int(serie_a_end[index - 1]) != 1:
                            return False
    return True


def is_flush(cards):
    initial_color = cards[0].split('-')[1]
    for card in cards:
        card_color = card.split('-')[1]
        if card_color != initial_color:
            return False



def sort_hand(cards):
    cards_values = list(map(lambda item: item.split('-')[0], cards))
    sorted_hand_with_as_begin = list(map(lambda card: adjust_numbers(card, False), cards_values))
    sorted_hand_with_as_end = list(map(lambda card: adjust_numbers(card, True), cards_values))

    sorted_hand_with_as_begin.sort()
    sorted_hand_with_as_end.sort()

    return sorted_hand_with_as_begin, sorted_hand_with_as_end


def adjust_numbers(card, is_as_begin):
    if card == 'J':
        return 11
    if card == 'Q':
        return 12
    if card == 'K':
        return 13
    if card == 'A':
        if is_as_begin:
            return 1
        else:
            return 14

    return int(card)


