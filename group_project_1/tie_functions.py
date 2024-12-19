def max_colours_count(cards_for_colour):
    players_max_colour_count = {}
    for player, cards in cards_for_colour.items():
        cards_colour_dict = {}
        for card in cards:
            card_colour = card[-1]
            cards_colour_dict[card_colour] = cards_colour_dict.get(card_colour, 0) + 1
        max_colour_count = max(cards_colour_dict.values())
        players_max_colour_count[player] = max_colour_count
    return players_max_colour_count

def max_value_count(cards):
    players_max_value_count = {}
    for player, cards in cards.items():
        cards_dict = {}
        for card in cards:
            card_value = card[:-1] if card[:-1].isdigit() else card[0]
            cards_dict[card_value] = cards_dict.get(card_value, 0) + 1
        max_value_count = max(cards_dict.values())
        players_max_value_count[player] = max_value_count
    return players_max_value_count

def tie(dast, players, players_cards):
    print('colour round ')
    max_colours = max_colours_count(players_cards)
    print(f' same colour cards max count {max_colours}')
    max_colour = max(max_colours.values())
    winner_tied_players_by_colour = [player for player, count in max_colours.items() if count == max_colour]
    
    if len(winner_tied_players_by_colour) == 1:
        return winner_tied_players_by_colour[0]
    
    print('value round')
    max_values = max_value_count(players_cards)
    print(f' same value cards max count {max_values}')
    max_value = max(max_values.values())
    winner_tied_players_by_value = [player for player, count in max_values.items() if count == max_value]
    
    if len(winner_tied_players_by_value) == 1:
        return winner_tied_players_by_value[0]
    
    print('It is TIE.Play whole game again .')
    return winner_tied_players_by_value
