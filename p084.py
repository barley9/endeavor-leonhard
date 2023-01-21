import numpy as np


rng = np.random.default_rng()

square_name = [
    'GO',   'A1', 'CC1', 'A2',  'T1', 'R1', 'B1',  'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1',  'C2',  'C3', 'R2', 'D1',  'CC2', 'D2', 'D3',
    'FP',   'E1', 'CH2', 'E2',  'E3', 'R3', 'F1',  'F2',  'U2', 'F3',
    'G2J',  'G1', 'G2',  'CC3', 'G3', 'R4', 'CH3', 'H1',  'T2', 'H2',
]
num_squares = len(square_name)
square_index = {name : i for i, name in enumerate(square_name)}  # enable lookup by name for more readable code

next_railroad = np.roll(np.repeat([5, 15, 25, 35], 10), -5)
next_utility = np.array((12 * [12]) + ((28 - 12) * [28]) + ((num_squares - 28) * [12]))  # square_index['U1'] = 12, square_index['U2'] = 28


def simulate_game(num_turns: int, die_faces: int) -> np.ndarray:
    """Returns an array containin the number of times a turn was ended on each board square"""
    
    # Community chest/Chance card piles
    chest = rng.permutation(14 * [None] + ['GO', 'JAIL'])
    chance = rng.permutation(6 * [None] + ['GO', 'JAIL', 'C1', 'E3', 'H2', 'R1', 'nextR', 'nextR', 'nextU', 'back3'])
    chest_idx = 0
    chance_idx = 0
    
    # Count number of turns ended on each square
    ended_on = np.zeros(shape=num_squares, dtype=int)

    p = square_index['GO']  # start at 'GO'
    doubles = 0  # count the number of times in a row player has rolled doubles
    dice_rolls = rng.integers(low=1, high=die_faces + 1, size=(num_turns, 2), dtype=np.int16)

    turn = 0
    while turn < num_turns:
        turn += 1

        d1, d2 = dice_rolls[turn - 1]  # roll two 6-sided dice
        if d1 == d2:
            doubles += 1
        else:
            doubles = 0

        if doubles == 3:  # if player rolls doubles three times in a row, go to jail
            p = square_index['JAIL']
            doubles = 0
            ended_on[p] += 1
            continue
        
        p = (p + d1 + d2) % num_squares  # move player d1 + d2 spaces
        if square_name[p] == 'G2J':  # go to jail
            p = square_index['JAIL']
        elif (p == square_index['CC1']) or (p == square_index['CC2']) or (p == square_index['CC3']):  # community chest
            card = chest[chest_idx]  # pick top card
            chest_idx = (chest_idx + 1) % len(chest)  # rotate card pile
            if card is not None:
                p = square_index[card]
        elif (p == square_index['CH1']) or (p == square_index['CH2']) or (p == square_index['CH3']):  # chance
            card = chance[chance_idx]
            chance_idx = (chance_idx + 1) % len(chance)
            if card is None:
                pass
            elif card == 'nextR':
                p = next_railroad[p]
            elif card == 'nextU':
                p = next_utility[p]
            elif card == 'back3':
                p = (p - 3) % num_squares
            else:
                p = square_index[card]
        ended_on[p] += 1

    return ended_on


if __name__ == '__main__':
    N = 100  # number of games to simulate
    counts = np.zeros(shape=num_squares, dtype=int)  # count how many turns the player ends on each square
    for i in range(N):
        print('game {} / {}'.format(i + 1, N), end='\r')
        counts += simulate_game(num_turns=100_000, die_faces=4)
    print()
    top3 = np.argsort(counts)[-3:][::-1]  # indices of top 3 most frequent squares
    print('modal string:', ''.join('{:02}'.format(i) for i in top3))

    import matplotlib.pyplot as plt

    xs = np.arange(len(counts))
    bar_list = plt.bar(xs, counts / np.sum(counts))
    for i in top3:
        bar_list[i].set_color('r')
    plt.xticks(xs, square_name, rotation='vertical')
    plt.show()