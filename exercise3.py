#!/usr/bin/env python3


def decide_rps(player1, player2):
    Dictionary1 = {'Rock Paper': 2, 'Rock Scissors': 1, 'Paper Rock': 1, 'Paper Scissors': 2, 'Scissors Paper': 1,
                   'Scissors Rock': 2, 'Rock Rock': 0, 'Paper Paper': 0, 'Scissors Scissors': 0}
    ComputeValue = player1+' '+player2
    print(ComputeValue)
    for indexValue in Dictionary1:
        if indexValue == ComputeValue:
            return Dictionary1[ComputeValue]
    else:
        return "Invalid Input"

print(decide_rps('Rock', 'Pen'))

