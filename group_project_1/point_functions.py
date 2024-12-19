def point_value(players_cards):
    players_point = {}
    for player, cards in players_cards.items():
        points = 0
        for card in cards:
            if card[0] == 'J':
                points += 11
            elif card[0] == 'Q':
                points += 12
            elif card[0] == 'K':
                points += 13
            elif card[0] == 'A':
                points += 20
            else:
                points += int(card[:-1])
        players_point[player] = points
    return players_point
