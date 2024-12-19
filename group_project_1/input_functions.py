def input_name(players_count=3):
    players = []
    for i in range(int(players_count)):
        player_name = input(f'Enter {i+1} player name: ')
        while player_name in players:  
            print("Please choose a different name.")
            player_name = input(f'Enter {i+1} player name: ')
        players.append(player_name)
    return players
