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
    players = []
    for i in range(int(players_count)):
        player_name = input(f'enter {i+1} player name :')
        players.append(player_name)
    return players   

# კარტის დარიგება 

def dealing_cards(dast = [],players_count = 3,cards_count = 5,players = {}):
    players_cards = {}
    for i in range(players_count):
        
        cards = []        
        for n in range(cards_count):
            card = random.choice(dast)
            
            dast.remove(card)
            cards.append(card)
            
        players_cards[players[i]] = cards
            
    return players_cards

 
 
# ქულების მინიჭება

def point_value(players_cards = {}):
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
    return players_point

# გამარჯვებულის პოვნა

def find_loser(players_point = {}):
    
    min_point = min(players_point.values())
    loser = [key for key,value in players_point.items() if value == min_point]
    
    if len(loser) == 1:
        return f'Loser is {loser[0]}'
    else:
        return 'Tie'

# დათვლა ფერების მიხედვით. ერთი მოთამაშის კარტებს იღებს 

def max_colors_count(cards_for_color = {}):  # cards = dealing_cards()
    
    players_max_color_count = {} 
    
    cards_color_dict = {}     #card_color:count
    
    for key,value in cards_for_color.items():
    
        for card in value:
            card_color = card[1]
            
            if card_color not in cards_color_dict.keys():
                cards_color_dict[card_color] = 1
            elif card_color in cards_color_dict.keys():
                cards_color_dict[card_color] += 1
                
        max_color_count = max(cards_color_dict.values())
        
        players_max_color_count[key] = max_color_count
        
    return players_max_color_count

# დათვლა მნიშვნელობების მიხედვით

def max_value_count(cards = {}):  # ცარდს = dealing_cards()
    
    players_max_value_count = {}
    
    cards_dict = {}     #card_value:count
    
    for key,value in cards.items():
    
        for card in value:
            card_value = card[0]
            
            if card_value not in cards_dict.keys():
                cards_dict[card_value] = 1
            elif card_value in cards_dict.keys():
                cards_dict[card_value] += 1
                
        max_value_count = max(cards_dict.values())
        
        players_max_value_count[key] = max_value_count
    return players_max_value_count

# კარტის შეცვლა 

def change_card(dast_for_game = [],player_cards = {}): # კარტის დასტა ნაკლული უნდა იყოს ანუ გლობალურად უნდა შეიცვალოს დარიგეის ფუნქვციიდან.
    card_changed = False
    for key,value in player_cards.items():
        
        print(F'{key} - {value}')
        card_for_change = input('enter card which you want to change :')
        if card_for_change in value:   
            value.remove(card_for_change)
            dast_for_game.append(card_for_change)  
            card_changed = True
        else :
            raise ValueError('Error.entered card is not in your cards .')
        new_card_from_dast = random.choice(dast_for_game)
        value.append(new_card_from_dast)
        print(value)
        player_cards[key] = value
        
        if card_changed == True :
            break
    print(player_cards)

# main ფუნქცია 

def main():
    while True:
        # Initialize the deck
        dast = dast_for_games()

        # Get player names
        players = input_name()
        print("Players:", players)
        
        # Deal cards to players
        player_cards = dealing_cards(dast, 3, 5, players)
        print("Initial Cards:", player_cards)
        
        # Allow each player to change one card
        for player in players:
            input_answer = input(f'Do you want to change one card, {player}? (yes/no): ').lower()
            if input_answer == 'yes':
                player_cards = change_card(dast,player_cards)
            else:
                print(f"{player} kept their cards.")
        print(player_cards)
        # Display final cards
        print("Final Cards:", player_cards)
        
        # Calculate points for all players
        players_point = point_value(player_cards)
        print("Player Points:", players_point)
        
        # Find the loser and remove them
        loser = find_loser(players_point)    
        print(f"The loser is: {loser}")
        
        players.remove(loser)
        print(f"Remaining players: {players}")
        
        # End the game if only one player remains
        if len(players) == 1:
            print(f"The winner is: {players[0]}!")
            return players[0]
        
if __name__ == '__main__':
    print("Game Over. Winner:", main())


        
        
    
    
    
