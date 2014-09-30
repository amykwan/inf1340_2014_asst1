#!/usr/bin/env python3


def RpsGame(player1, player2):
    Dictionary1 = {'rock paper': 2, 'rock scissors': 1, 'paper rock': 1, 'paper scissors': 2, 'scissors paper': 1,
                   'scissors rock': 2}
    ComputeValue = player1+' '+player2
    print(ComputeValue)
    for indexValue in Dictionary1:
        if indexValue == ComputeValue: #print(Dictionary1[input])
            return Dictionary1[ComputeValue]
    else:
        return 0

print(RpsGame('rock','scissors'))

