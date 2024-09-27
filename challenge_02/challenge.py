#Load the inputs
f = open("input.txt", "r")

max_colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

good_games = []
min_cube_powers = []

for x in f:
    row = str.split(x, ':')

    game_id = int(str(row[0]).split(' ')[1])
    games = str(row[1]).split(';')

    game_mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    print(game_id)
    valid_game = True

    for game in games:
        colors = game.split(',')

        for c in colors:
            color = c.strip().split(' ')
            count = int(color[0])
            
            if count > game_mins[color[1]]:
                # valid_game = False
                # print(f'too many {color[1]}')
                # break
                game_mins[color[1]] = count

        # if valid_game == False:
        #     break
        
    # print(valid_game)
    # if valid_game:
    #     good_games.append(game_id)
    print(games)
    print(game_mins)

    min_cube_powers.append(game_mins['red'] * game_mins['green'] * game_mins['blue'])

print(sum(min_cube_powers))

