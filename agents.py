"""
Every agent should simply be a function that accepts two arguments

The first is "board" which is an array of length 9 representing a tic tac toe board as such

0|1|2
-+-+-
3|4|5
-+-+-
6|7|8

The second argument "player" is the player number, 0 if the agent is playing x, 1 if the agent is playing 1

"""


import random
import consts

def stoogeAgent(board, player):
    """This agent plays randomly"""

    #collect open squares
    possibleMoves = []
    for x in range(len(board)):
        if board[x] == consts.UNOWNED:
            possibleMoves.append(x)        
    
    #randomly choose open square
    return possibleMoves[random.randint(0,len(possibleMoves)-1)]
