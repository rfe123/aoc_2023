#Load the inputs
f = open("input.txt", "r")

max_colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}

good_games = []

for x in f:
    row = str.split(x, ':')

    game_id = int(str(row[0]).split(' ')[1])
    games = str(row[1]).split(';')

    print(game_id)
    valid_game = True

    for game in games:
        colors = game.split(',')

        for c in colors:
            color = c.strip().split(' ')
            count = int(color[0])

            print(color)
            
            if count > max_colors[color[1]]:
                valid_game = False
                print(f'too many {color[1]}')
                break

        if valid_game == False:
            break
        
    print(valid_game)
    if valid_game:
        good_games.append(game_id)

print(sum(good_games))

