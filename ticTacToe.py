import agents as agentFunctions
import consts
consts.UNOWNED = -1
consts.X_OWNED = 0
consts.O_OWNED = 1

consts.TURN_MAP = ["X", "O"]

consts.X_GRAPHIC = """            
            
   .____,   
  . \  / ,  
  |`-  -'|  
  |,-  -.|  
  ' /__\ `  
   '    `   
            
            
"""

consts.O_GRAPHIC = """            
            
    ____    
  ,' __ `.  
 / ,'  `. \ 
 | |    | | 
 \ `.__,' / 
  `.____,'  
            
            
"""

#agents for x and 0 are in 0 and 1 respectivly
agents = [None,None]

def portionOfRow(col, subRow, value):
    """Draws part of a row for a given column"""
    if value == consts.UNOWNED:
        return " " * 12
    elif value == consts.X_OWNED:
        return consts.X_GRAPHIC.split('\n')[subRow]
    elif value == consts.O_OWNED:
        return consts.O_GRAPHIC.split('\n')[subRow]
    
    #dunno whats going on if we get here    
    return "?" * 13

def drawRow(row):
    """Draws a single row in the board"""
    
    for subRow in range(10):
        subRowString = ""
        for col in range(3):
            if col > 0:
                #second two columns have a pipe after them
                subRowString += "|"
            subRowString += portionOfRow(col, subRow, row[col])
        print subRowString

def drawBoard(board):
    """Renders the gameboard to the console oh-so-fashionably"""
    
    for x in range(3):
        drawRow(board[x*3:x*3+3])
        if x < 2:
            #first two rows have a line under them
            print "-" * (12*3+2)
    
    
def same(board, layout):
    """Returns winner if all elements of board[tiles[x]] are the same, None otherwise"""
    if board[layout[0]] == board[layout[1]] and board[layout[1]] == board[layout[2]]:
        return board[layout[0]]
    return None
    
def winner(board):
    """Takes in a board and reports the winner. If there is no winner, it returns UNOWNED"""
    
    #all winning layouts
    layouts = [[0,1,2], [3,4,5], [6,7,8],\
               [0,3,6], [1,4,7], [2,5,8],\
               [0,4,8], [2,4,6]]

    #go through all layouts and see if they have a set of only one player's pieces
    for layout in layouts:
        winner = same(board, layout)
        if winner != None and winner != consts.UNOWNED:
            return layout

    #no winner, check if board is full, if so it is a cat's game
    count = 0
    for x in board:
        if x != consts.UNOWNED:
            count += 1
    if count == 9:
        return consts.UNOWNED #cats game

    return None

def gamePrompt(turn):
    """Prompts the player whose turn it is to enter a move"""
    proposed_move = raw_input("%s's turn next, enter your move (? for help): " % consts.TURN_MAP[turn])
    return proposed_move

def showHelp():
    """This function simply displays the game's help 'page'"""
    print "To make a move enter a value from 0-8" 
    print "Look at the diagram below:"
    print """0|1|2
-+-+-
3|4|5
-+-+-
6|7|8"""

def executeMove(board, move, turn):
    """Places a piece belging to player "turn" to space "move" on the board"""
    board[move] = turn
    return board

def tryMove(board, move):
    """Determins if the move is acceptable given the current game state, returns an error message or None"""
    #needs to be on the game board (0-8)
    if move < 0 or move > 8:
        return "Move is off of the board! Please make a move 0-8."

    #Needs to be an unoccupied tile
    if board[move] != consts.UNOWNED:
        return "A piece is already there! Please make a move in an empty square."
    
    #otherwise its an ok move
    return None

def getValidMove(board, turn, error=None):
    """Doesn't return the move until it is valid"""
    #if there was an error show it
    if error:
        print error
        
    #get user input
    if agents[turn] == "Human":
        move = gamePrompt(turn)
    else:
        print("\nAgent for %s is moving.\n" % consts.TURN_MAP[turn])
        move = agents[turn](board, turn)
    
    #show help and ask for move again
    if move == "?":
        showHelp()
        return getValidMove(board, turn, error=None)


    #try to cast the move to a number
    try:
        move = int(move)
    except:
        return getValidMove(board, turn, "Please enter a number for your move.")

    #try the move and see if there is an error
    error = tryMove(board, move)
    #if there is we get another move
    if error:
        return getValidMove(board, turn, error)
    
    return move

def game(xagent, oagent):
    """This is the min game function"""
    #x goes first, so x will be player 0
    turn = 0
    #initialize the game board
    board = [consts.UNOWNED] * 9
    #set agents
    agents[0] = xagent
    agents[1] = oagent

    #repeat as long as there is no winner
    while (winner(board) == None):
        #draw the game board
        drawBoard(board)
        
        #have the player enter their move
        move = getValidMove(board, turn)

        #make the move
        board = executeMove(board, move, turn)
        
        #update turn
        turn = (turn + 1) % 2

    #draw the board a lst time and announce the winner
    drawBoard(board)
    if winner(board) == consts.UNOWNED:
        print "Cats game!"
    else:
        print "Congratulations %s wins at %s" % (consts.TURN_MAP[board[winner(board)[0]]], winner(board))
    return winner(board)
            

#starts the game if this file is executed
if __name__ == '__main__':
    game("Human", agentFunctions.stoogeAgent)

