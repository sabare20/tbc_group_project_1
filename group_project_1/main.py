from input_functions import input_name
from card_functions import dast_for_games, dealing_cards
from point_functions import point_value
from tie_functions import tie
from change_card import change_card

def main():
    dast = dast_for_games()
    players = input_name(3)

    while len(players) > 1:
        players_cards = dealing_cards(dast, players)
        print("Players' Cards - ", players_cards)
        
        players_points = point_value(players_cards)
        print(f'points :{players_points}')
        print(50*"*") 
        
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
        
        print(50*"*") 
        print("Final Cards:", players_cards)
        print("Players' Final Points:", players_points)
        print(50*"*") 

        min_points = min(players_points.values())
        losers = [player for player, points in players_points.items() if points == min_points]

        if len(losers) == 1:
            print(f"{losers[0]} is out of the game.")
            players.remove(losers[0])
            print(50*"*")
        else:
            print(f" Tie between {losers}")
            result = tie(dast, losers, {player: players_cards[player] for player in losers})
            
            if type(result) == str:  # if a winner is found
                print(f"{result} wins.")
                players = [player for player in players if player not in  losers]
                players.append(result)  # shevcvale remove
            else:
                print("Tie continues between:", result)
                players = result

    print(f"Winner of the game is {players[0]}! Please enter again .")

if __name__ == "__main__":
    main()
