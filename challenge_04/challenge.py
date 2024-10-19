#Load the inputs
f = open("input.txt", "r")

all_winners = []
all_cards = []

card_wins = []

for x in f:
    card_split = x.split(':')
    # card = int(card_split[0].split(' ')[-1])

    numbers = card_split[1].split('|')
    winners = [int(n) for n in numbers[0].split(' ') if n != '']
    card_numbers = [int(n) for n in numbers[1].split(' ') if n != '']

    win_counter = -1
    for cn in card_numbers:
        if cn in winners:
            win_counter += 1

    card_wins.append(pow(2, win_counter)) if win_counter>-1 else card_wins.append(0)

print(sum(card_wins))
