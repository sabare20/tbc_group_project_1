import random

# დასტის შექმნა 

def dast_for_games():
    colors = ['S','H','D','S']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    dast = []
    for color in colors:
        for value in values:
            card = value + color
            dast.append(card)
    return dast*4

# მოთამაშეების სახელების მიღება 

def input_name(players_count = 3):
    players = {}
    for i in range(int(players_count)):
        player_name = input(f'enter {i+1} player name :')
        players[f'player {i+1}'] = player_name
    return players   


# კარტის დარიგება 

def dealing_cards(dast=dast_for_games(),players_count = 3,cards_count = 5):
    players_cards = {}
    for i in range(players_count):
        
        cards = []        
        for n in range(cards_count):
            card = random.choice(dast)
            
            dast.remove(card)
            cards.append(card)
            
        players_cards[f'player {i+1}'] = cards
    print(players_cards)    
    return players_cards



# ქულების მინიჭება

def point_value(players_cards = dealing_cards()):
    players_point = {}
    for key,value in players_cards.items():
        points = 0
        for card in value:
            if card[0] == 'J':
                points += 11
            elif card[0] == 'Q':
                points += 12 
            elif card[0] == 'K':
                points += 13
            elif card[0] == 'A':
                points += 20
            else:
                points += int(card[0])
        players_point[key] = points
    print(players_point)
    return players_point

# გამარჯვებულის პოვნა

def find_winner(players_point = point_value() , players = input_name()):
    
    
    max_point = max(players_point.values())
    min_point = min(players_point.values())
    winner = [key for key,value in players_point.items() if value == max_point]
    loser = [key for key,value in players_point.items() if value == min_point]
    
    if winner[0] == winner[-1]:
        winner_name = players.get(winner[0])
        print(f'Winner is {winner_name}') # ფლეიერების  დიქტიდან წამოვიღოთ სახელები და ჩავანაცვლოთ.
    elif loser[0] == loser[-1]:
        loser_name = players.get(loser[0])
        print(f'Loser is {loser_name}')
    else:
        print('Tie')

find_winner()