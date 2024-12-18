import random

# დასტის შექმნა 

def dast_for_games():
    colours = ['S','H','D','C']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    dast = []
    for colour in colours:
        for value in values:
            card = value + colour
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

def dealing_cards(dast = [],players_count = 3,cards_count = 5,players = []):
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
                points += int(card[:-1])
        players_point[key] = points
    return players_point

# გამარჯვებულის პოვნა

def find_loser(players_point = {}):
    
    min_point = min(players_point.values())
    loser = [key for key,value in players_point.items() if value == min_point]
    
    if len(loser) == 1:
        return 'loser', loser[0]
    elif len(loser) == 2 :
        return 'game continue between losers',loser
    else:                                       # თუ ორ მოთამშეს აქვს თანაბარი ქულები შემდეგი რაუნდი მხოლოდ მაგ ორს შორისაა.
        return 'Tie'


def find_winner(players_points = {}):
    max_point = max(players_points.values())
    winner = [key for key,value in players_points.items() if value == max_point]
    loser_compared_winners = [key for key,value in players_points.items() if value != max_point]
    if len(winner) == 1:
        return 'winner',winner[0]
    elif len(winner) == 2:
        return 'loser',loser_compared_winners[0]
    else:                                       # თუ ორ მოთამშეს აქვს თანაბარი ქულები შემდეგი რაუნდი მხოლოდ მაგ ორს შორისაა.
        return 'Tie'
     

# დათვლა ფერების მიხედვით. ერთი მოთამაშის კარტებს იღებს 

def max_colours_count(cards_for_colour = {}):  # cards = dealing_cards()
    
    players_max_colour_count = {} 
    
    cards_colour_dict = {}     #card_colour:count
    
    for key,value in cards_for_colour.items():
    
        for card in value:
            card_colour = card[-1]
            
            if card_colour not in cards_colour_dict.keys():
                cards_colour_dict[card_colour] = 1
            elif card_colour in cards_colour_dict.keys():
                cards_colour_dict[card_colour] += 1
                
        max_colour_count = max(cards_colour_dict.values())
        
        players_max_colour_count[key] = max_colour_count
        
    return players_max_colour_count

# დათვლა მნიშვნელობების მიხედვით

def max_value_count(cards = {}):  # ცარდს = dealing_cards()
    
    players_max_value_count = {}
    
    for key,value in cards.items():
        
        cards_dict = {}    #card_value:count
        
        for card in value:
            card_value = card[:-1]
            
            if card_value not in cards_dict.keys():
                cards_dict[card_value] = 1
            elif card_value in cards_dict.keys():
                cards_dict[card_value] += 1
                
        max_value_count = max(cards_dict.values())
        
        players_max_value_count[key] = max_value_count
        
    return players_max_value_count

# კარტის შეცვლა 

def change_card(dast_for_game=None, players_cards=None, player=''):

    if dast_for_game is None:
        dast_for_game = []
    if players_cards is None:
        players_cards = {}

    player_cards = players_cards.get(player)
    print(f"{player} - {player_cards}")
    
    while True:  # Loop until the player provides a valid card
        card_for_change = input("Enter the card you want to change: ").strip()
        
        if card_for_change in player_cards:
            player_cards.remove(card_for_change)  # Remove the chosen card from the player's hand
            dast_for_game.append(card_for_change)  # Add the old card back to the deck
            
            new_card_from_dast = random.choice(dast_for_game)  # Pick a random card from the deck
            dast_for_game.remove(new_card_from_dast)  # Remove the chosen card from the deck
            player_cards.append(new_card_from_dast)  # Add the new card to the player's hand
            
            print(f"{player}'s new hand: {player_cards}")
            players_cards[player] = player_cards  # Update the player's hand in the players dictionary
            break
        else:
            print("Error: Entered card is not in your hand. Please try again.")
    
    return players_cards



# main ფუნქცია 

def main():
    winner_of_game = ''
    
    dast = dast_for_games()
    
    players = input_name(3)
    
    print(50 * '-')
    while len(players) > 1 :
        
        players_count = len(players)
        
        players_cards = dealing_cards(dast,players_count,5,players)
        print(players_cards)
        
        players_points = point_value(players_cards)
        print(players_points)
        
        print(50 * '-')
        
        for player in players:
            while True:  # Loop until valid input is provided
                input_answer = input(f"Do you want to change one card, {player}? (yes/no): ").strip().lower()
                if input_answer == 'yes':
                    players_cards = change_card(dast, players_cards, player)
                    break  # Exit the loop after handling the card change
                elif input_answer == 'no':
                    print(f"{player} kept their cards.")
                    break  # Exit the loop after confirming no card change
                else:
                    print("Error: You must enter only 'yes' or 'no'. Please try again.")
        
        print(50 * '-')
        
        print("Final Cards:", players_cards)
        
        finale_points = point_value(players_cards)
        print('Final points :',finale_points)
        
        print(50 * '-')
        
        loser = find_loser(finale_points)
        
        if loser[0] == 'loser':
            
            print(loser[0]+' - '+loser[1])
            players.remove(loser[-1])
            print(f'Leftover players : {players}')
            print(50 * '-')
            
        elif len(loser[-1]) == 2:
            losers = loser[-1]   
            losers_cards = {}
            
            for loser in losers:
                losers_cards[loser] = players_cards.get(loser)
            losers_colors_count = max_colours_count(losers_cards)
            loser_loser = find_loser(losers_colors_count)
            
            if loser_loser == 'Tie':
                losers_value_count = max_value_count(losers_cards)
                loser_loser = find_loser(losers_value_count)
                
                if loser_loser == 'Tie':
                    print('Tie between losers.play whole game again.')
                    continue
                else:
                    real_loser = loser_loser[-1]
                    print(f' real loser is {real_loser}')
                    players.remove(real_loser)
                    print(f'leftover players : {players}')
            else:
                real_loser_by_colour = loser_loser[-1]
                players.remove(real_loser_by_colour)
                print(f'leftover players : {players}')
        else:
            players_colour_count = max_colours_count(players_cards)
            winner_by_colour = find_winner(players_colour_count)
            if winner_by_colour[0] == 'winner is:':
                print(winner_by_colour[0]+winner_by_colour[1])
                winner_of_game = winner_by_colour[-1]
                break
                
            elif winner_by_colour[0] == 'we have loser':
                print(winner_by_colour[0]+winner_by_colour[1])
                players.remove(winner_by_colour[-1])
                print(f'leftover players : {players}')
            else:
                players_value_count = max_value_count(players_cards)
                winner_by_value = find_winner(players_value_count)
                if winner_by_value[0] == 'winner is:':
                    print(winner_by_value)
                    winner_of_game = winner_by_value[-1]
                    break
                elif winner_by_colour[0] == 'we have loser':
                    print(winner_by_colour)
                    players.remove(winner_by_value[-1])
                    
    if winner_of_game:
        print(f'WINNER OF GAME IS {winner_by_colour[0]}')
    else:
        print(f'WINNER OF GAME IS {players[0]}')
            
if __name__ == '__main__':
    main()
    

