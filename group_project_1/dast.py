import random
def dast_for_games():
    colors = ['S','H','D','S']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    dast = []
    for color in colors:
        for value in values:
            card = value + color
            dast.append(card)
    return dast*4


players = {}  # g გლობალურად უნდა იყოს განსაზღვრული . როცა მხოლოდ ფუნქციაშია განსაზღვრული არ ცანს სხვაგან .ანუ მეინშიც განვსაზღვროთ.
def input_name(players_count):
    global players
    for i in range(int(players_count)):
        player_name = input(f'enter {i+1} player name :')
        players[f'player {i+1}'] = player_name
    print(players)   
    
input_name(3)


# დარიგების კოდი
dast_for_game = dast_for_games() # დასტა თამაშისთვის
#players_cards = {}    # სხვა ფუნქციაში გვჭირდება და გლობალურად უნდა იყოს განსზღვრული
def dealing_cards(dast=dast_for_game,players_count=3,cards_count=5):
    global players_cards 
    for i in range(players_count):
        #print(f'{i+1} player cards :',end = ' ')
        cards = []
        for n in range(cards_count):
            card = random.choice(dast)
            dast_for_game.remove(card)
            #print(card,end=' ')
            cards.append(card)
        #print()
        players_cards[f'player {i+1}'] = cards
    print(players_cards)




# ქულების მინიჭება


def point_value(players_cards):
    players_point = {}
    for key,value in players_cards:
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

def find_winner(players_point):
    global players
    
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
        
     

# დათვლა ფერების მიხედვით 
    
def max_colors_count(cards):
    cards_color_dict = {}     #card_color:count
    
    for card in cards:
        card_color = card[1]
        
        if card_color not in cards_color_dict.keys():
            cards_color_dict[card_color] = 1
        elif card_color in cards_color_dict.keys():
            cards_color_dict[card_color] += 1
            
    print(cards_color_dict)
    max_count = max(cards_color_dict.values())
    print(max_count)

#დათვლა მნიშვნელობების მიხედვით
def max_value_count(cards):
    cards_dict = {}     #card_value:count
    
    for card in cards:
        card_value = card[0]
        
        if card_value not in cards_dict.keys():
            cards_dict[card_value] = 1
        elif card_value in cards_dict.keys():
            cards_dict[card_value] += 1
            
    print(cards_dict)
    max_count = max(cards_dict.values())
    print(max_count)

#['3D','5C','10S','KH','AD']
# კარტის შეცვლა 
def change_card(player_cards):    # კარტის დასტა ნაკლული უნდა იყოს ანუ გლობალურად უნდა შეიცვალოს დარიგეის ფუნქვციიდან.
    card_for_change = input('enter card which you want to change :')
    if card_for_change in player_cards:   
        player_cards.remove(card_for_change)
        dast_for_game.append(card_for_change)
    else :
        raise ValueError('Error.entered card is not in your cards .')
    new_card_from_dast = random.choice(dast_for_game)
    player_cards.append(new_card_from_dast)
    print(player_cards)






def main(player_count,card_number):
    
    dast_for_games()
    
    players_cards = {}
    
    dealing_cards(dast_for_games(),player_count,card_number)
    
    players_points = {}
    
    point_value(players_cards)
    
    find_winner(players_points)
    
if __name__ == '__main__':
    main(3,5)
    
    
    
    
    

    
    

        
        
    