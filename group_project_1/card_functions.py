from random import choice

def dast_for_games():
    colours = ['S', 'H', 'D', 'C'] 
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    dast = []
    for colour in colours:
        for value in values:
            card = value + colour
            dast.append(card)
    return dast * 4

def dealing_cards(dast, players, cards_count=5):
    players_cards = {}
    for player in players:
        cards = []
        for _ in range(cards_count):
            card = choice(dast)
            dast.remove(card)
            cards.append(card)
        players_cards[player] = cards
    return players_cards
