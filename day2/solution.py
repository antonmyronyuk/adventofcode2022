with open('input.txt') as input_file:
    plays = [play.split() for play in input_file.read().split('\n') if play]


play_scores = {'X': 1, 'Y': 2, 'Z': 3}
win_score = 6
draw_score = 3
win_combination = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw_combination = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose_combination = {'A': 'Z', 'B': 'X', 'C': 'Y'}

score = 0
for opponent_move, move in plays:
    score += play_scores[move]
    if move == win_combination[opponent_move]:
        score += win_score
    elif move == draw_combination[opponent_move]:
        score += draw_score

print(score)  # part 1


score = 0
for opponent_move, strategy in plays:
    match strategy:
        case 'X':
            move = lose_combination[opponent_move]
        case 'Y':
            move = draw_combination[opponent_move]
            score += draw_score
        case 'Z':
            move = win_combination[opponent_move]
            score += win_score
        case _:
            raise ValueError('Unknown strategy')

    score += play_scores[move]

print(score)  # part 2
