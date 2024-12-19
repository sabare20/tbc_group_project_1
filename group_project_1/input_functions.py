def input_name(players_count=3):
    players = []
    for i in range(int(players_count)):
        while True:
            player_name = input(f'Enter {i + 1} player name: ').strip()
            if not player_name:
                print("Name must be a string! Please try again")
            elif player_name in players:
                print("Please choose a different name.")
            else:
                break
        players.append(player_name)
    return players