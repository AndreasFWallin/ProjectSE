# -*- coding: utf-8 -*-
import Server
import copy
import json
import random
random.seed(1)

# The 'printboard' function visualizes the current state of the board.
# It uses a board as input and prints every point on the board, in a
# "human-friendly" way.

def printboard(board):
    board1=[]
    for i in range(len(board)):
        if board[i]==0:
            board1.append("o")
        elif board[i]==1:
            board1.append("x")
        else:

            board1.append(" ")

    print(board1[0],"----------------",board1[1],"----------------",board1[2])
    print('|                  |                   |')
    print("|  ",board1[8],"------------",board1[9],"-------------",board1[10],"  |")
    print('|   |              |               |   |')
    print("|   |  ",board1[16],"--------",board1[17],"--------",board1[18],"   |   |")
    print('|   |   |                      |   |   |')
    print(board1[7],"-",board1[15],"-",board1[23],"                    ",board1[19],"-",board1[11],"-",board1[3])
    print('|   |   |                      |   |   |')
    print("|   |  ",board1[22],"--------",board1[21],"--------",board1[20],"   |   |")
    print('|   |              |               |   |')
    print("| ",board1[14],"-------------",board1[13],"-------------",board1[12],"  |")
    print('|                  |                   |')
    print(board1[6],"----------------",board1[5],"---------------- ",board1[4])


# The 'invert_board' function takes the current board as input
# and inverts each position and returns the inverted version of the board.
# "Black player" becomes "White player" and vice versa. Empty  board-slots stays empty.
def invert_board(board):
    invertedboard = []
    for i in board:
        if i == 1:                    # If current position on the board is '1' (white),
            invertedboard.append(0)   # add a '0' (black) to the new board.
        elif i == 0:
            invertedboard.append(1)
        else:
            invertedboard.append(-1)
    return invertedboard              # Return the new, inverted board.



def numbOfBlockedPices(board):
    blocked_0=0
    blocked_1=0
    res=False
    for i in range(24):
        if board[i]==0:
            adjlist=adjacentLocations(i)
            for pos in adjlist:
                if board[pos]<0:
                    res=False
            if res:
                blocked_0+=1
            res=True
    for i in range(24):
        if board[i]==1:
            adjlist=adjacentLocations(i)
            for pos in adjlist:
                if board[pos]<0:
                    res=False
            if res:
                blocked_1+=1
            res=True
    return blocked_0-blocked_1


#printboard(vec)
def heuristic(board,player,turn,difficulty):
    value=0
    # determinimng what different things are worth depending on the state of the game
    #reward=[a mill, a blocked pice, two in a row with an empty spot as the tird in the row, difference of pices on the board]
    if(difficulty==3):
        if turn<18:
           reward=[40,2,8,22] #rewardfunction for phase one
        elif numOfStones(board,1)==3 and turn>18:
         reward=[55,0,0,10] #rewardfunction for phase 3
        else:
           reward=[43,20,0,30] #rewardfunction for phase 2
    elif(difficulty==2):
        if turn<18:
           reward=[40,20,8,22]
        elif numOfStones(board,1)==3 and turn>18:
         reward=[0,0,0,20]
        else:
           reward=[20,3,0,30]
    else:
        if turn<18:
            reward=[10,10,10,10]
        elif turn%3==0:
            reward=[0,0,0,0]
        elif numOfStones(board,1)==3 and turn>18:
            value+= -board.count(0)*10
            reward=[0,0,0,0]
        else:
            reward=[10,10,10,10]


    #calculate number of mills on the board
    for i in range(24):
        if isRow(i, board)==True and board[i]==1:
            value+=reward[0]/3
        elif isRow(i, board)==True and board[i]==0:
            value-=reward[0]/3

   # Following loops add values if there are two stones in a row
   # and if there's a 3 piece configuration12
    #for i in range(0,23):
       # currentList = adjacentLocations(i)
      #  for j in currentList:
            #if (len(currentList)==4):
              #  value+=50
           # if board[j]==board[i] and board[i]==1:
           #     value+=100
          #  elif (board[j]==board[i] and board[i]==0):
        #        value-=100
        #if pieceConfiguration3(board, player):
        #   value += 100
    #looks for two pices in a row and if the last place is empty

    #calculates the difference in blocked pices between the players
    value += numbOfBlockedPices(board)*reward[1]

    #calculates the numbe of two in a row with a empry spot in the last place
    for i in range(24):
        if(board[i]==-1):
            board[i]=1
            if(isRow(i,board)):
                value+=reward[2]
            board[i]=0
            if(isRow(i,board)):
                value-=reward[2]
            board[i]=-1

    value+= (board.count(1)-board.count(0))*reward[3]


    if board.count(1)==3 and turn>18:
        value-= 100 #10000000000000000000000000
    elif board.count(0)==3 and turn>18:
        value+= 100#10000000000000000000000000




    if board.count(1)<3 and turn>18:
        value-= 1000000 #10000000000000000000000000
    elif board.count(0)<3 and turn>18:
        value+= 1000000 #10000000000000000000000000

    # Counts number of stones player have in comparison to the opponent
    value += numOfStones(board,1) - numOfStones(board,0)

    return value


def move_1(board, player):
    move_list_1=[] #creats an empty list to store the moves in
    for i in range(24): #loops thorgh all the positions on the board
        if(board[i]<0): #chscks if position is empty
            newBoard=copy.deepcopy(board)  #makes a copy off current board and changes it
            newBoard[i]=player
            #checks if a row is created and removes a pice it is created.

            if isRow(i, newBoard):


                move_list_1=remove_piece(newBoard,move_list_1,player)
            else:
                move_list_1.append(newBoard)
    return move_list_1

def remove_piece(newBoard,move_list_1,player):
    if player==0:
        opponent=1
    else:
        opponent=0
    for i in range(len(newBoard)):
        if newBoard[i]==opponent:

            if not isRow(i,newBoard):
                newBoard_copy=copy.deepcopy(newBoard)
                newBoard_copy[i]=-1
                move_list_1.append(newBoard_copy)
            else:
                newBoard_copy=copy.deepcopy(newBoard)
                move_list_1.append(newBoard_copy)

    return move_list_1



def move_2(board,player):
    move_list_1=[]
    for i in range(24):
        if(board[i]==player):
            close_list=adjacentLocations(i)
            for pos in close_list:
                if board[pos]==-1:
                    newBoard=copy.deepcopy(board)
                    newBoard[i]=-1
                    newBoard[pos]=player
                    if isRow(pos,newBoard):
                        move_list_1=remove_piece(newBoard,move_list_1,player)
                    else:
                        move_list_1.append(newBoard)
    return move_list_1

def move_3(board, player):
    move_list_1=[]
    for i in range(24):
        if (board[i]==player):
            for k in range(24):
                if board[k]==-1:
                    newBoard=copy.deepcopy(board)
                    newBoard[i]=-1
                    newBoard[k]=player
                    if isRow(k,newBoard):
                        move_list_1=remove_piece(newBoard,move_list_1,player)
                    else:
                        move_list_1.append(newBoard)
    return move_list_1





#function to count stones. value is 0 for black stones, 1 for white stones
def numOfStones(board, value):
    return board.count(value)


# Function to find adjacent locations for a given location.
# Returns a list of adjacent location
def adjacentLocations(position): #adjecent locations without the diagonals
    adjacent = [
        [1, 7],
        [0, 2, 9],
        [1, 3],
        [2, 4, 11],
        [3, 5],
        [4, 6, 13],
        [5, 7],
        [0, 6, 15],
        [9, 15],
        [1, 8, 10, 17],
        [9, 11],
        [3, 10, 12, 19],
        [11, 13],
        [5, 12, 14 , 21],
        [ 13, 15],
        [7, 8, 14, 23],
        [ 17, 23],
        [9, 16, 18],
        [ 17, 19],
        [11, 18, 20],
        [19, 21],
        [13, 20, 22],
        [ 21, 23],
        [15, 16, 22]
    ]
    return adjacent[position]

 # Function to check if 2 positions have the player on them
# Takes player symbol as input (0 or 1)
# Board list as input
# p1 and p2, the two positions
# Returns boolean values
def isPlayer(player, board, p1, p2):
    if (board[p1] == player and board[p2] == player):
        return True
    else:
        return False

def isPlayer2(player, board, pos):
    if (board[pos]==player):
        return True
    else:
        return False



#the function used for diagonals dont know felt cute might delete later
#- removed, didnt feel cute anymore.

# Function to check if a player can make a row in the next move,
# by traversing the current board and checks if that Player
# can place a stone such that the Player gets 3 stones in a row.
# Return True if the player can create a row on that given position.
def checkNextRow(position, board, player):
    row = [
        (isPlayer(player, board, 1, 2)  or isPlayer(player, board, 6, 7)),
        (isPlayer(player, board, 0, 2) or isPlayer(player, board, 9, 17)),
        (isPlayer(player, board, 0, 1) or isPlayer(player, board, 3, 4) ),
        (isPlayer(player, board, 2, 4) or isPlayer(player, board, 11, 19)),
        (isPlayer(player, board, 2, 3)  or isPlayer(player, board, 5, 6)),
        (isPlayer(player, board, 4, 6) or isPlayer(player, board, 13, 21)),
        (isPlayer(player, board, 4, 5) or isPlayer(player, board, 0, 7)),
        (isPlayer(player, board, 0, 6) or isPlayer(player, board, 15, 23)),
        (isPlayer(player, board, 9, 10)  or isPlayer(player, board, 14, 15)),
        (isPlayer(player, board, 8, 10) or isPlayer(player, board, 1, 17)),
        (isPlayer(player, board, 8, 9) or isPlayer(player, board, 11, 12)),
        (isPlayer(player, board, 3, 19) or isPlayer(player, board, 10, 12)),
        ( isPlayer(player, board, 10, 11) or isPlayer(player, board, 13, 14)),
        (isPlayer(player, board, 5, 21) or isPlayer(player, board, 12, 14)),
        (isPlayer(player, board, 13, 12) or isPlayer(player, board, 15, 8) ),
        (isPlayer(player, board, 8, 14) or isPlayer(player, board, 7, 23)),
        (isPlayer(player, board, 17, 18) or isPlayer(player, board, 22, 23)),
        (isPlayer(player, board, 1, 9) or isPlayer(player, board, 16, 18)),
        (isPlayer(player, board, 16, 17) or isPlayer(player, board, 19, 20)),
        (isPlayer(player, board, 18, 20) or isPlayer(player, board, 3, 11)),
        (isPlayer(player, board, 18, 19)  or isPlayer(player, board, 22, 21)),
        (isPlayer(player, board, 20, 22) or isPlayer(player, board, 5, 13)),
        (isPlayer(player, board, 20, 21) or isPlayer(player, board, 16, 23)),
        (isPlayer(player, board, 22, 16) or isPlayer(player, board, 7, 15))
    ]

    return row[position]


# Works in the same principle as CheckNextRow above,
# but looks for the possibility of placing a stone such that
# there are two stones in a row. Also returns true where the stone
# could be placed in the given position.
def checkNextRow2(position, board, player):
    row = [
        (isPlayer2(player, board,1) or isPlayer2(player,board,7) or isPlayer2(player,board,8)), #Adjecents to pos 0
        (isPlayer2(player, board,0) or isPlayer2(player,board,2) or isPlayer2(player,board,9)), #Adjecents to pos 1
        (isPlayer2(player, board,1) or isPlayer2(player,board,10) or isPlayer2(player,board,3)), #Adjecents to pos 2..
        (isPlayer2(player, board,2) or isPlayer2(player,board,11) or isPlayer2(player,board,4)),
        (isPlayer2(player, board,3) or isPlayer2(player,board,12) or isPlayer2(player,board,5)),
        (isPlayer2(player, board,4) or isPlayer2(player,board,13) or isPlayer2(player,board,6)),
        (isPlayer2(player, board,5) or isPlayer2(player,board,14) or isPlayer2(player,board,7)),
        (isPlayer2(player, board,6) or isPlayer2(player,board,15) or isPlayer2(player,board,0)),
        (isPlayer2(player, board,0) or isPlayer2(player,board,15) or isPlayer2(player,board,9) or isPlayer2(player,board,16)), #Adjecents to pos 8
        (isPlayer2(player, board,8) or isPlayer2(player,board,1) or isPlayer2(player,board,10) or isPlayer2(player,board,17)), #Adjecents to pos 9
        (isPlayer2(player, board,9) or isPlayer2(player,board,2) or isPlayer2(player,board,11) or isPlayer2(player,board,18)),
        (isPlayer2(player, board,10) or isPlayer2(player,board,3) or isPlayer2(player,board,12) or isPlayer2(player,board,19)),
        (isPlayer2(player, board,11) or isPlayer2(player,board,4) or isPlayer2(player,board,13) or isPlayer2(player,board,20)),
        (isPlayer2(player, board,12) or isPlayer2(player,board,5) or isPlayer2(player,board,14) or isPlayer2(player,board,21)),
        (isPlayer2(player, board,13) or isPlayer2(player,board,6) or isPlayer2(player,board,15) or isPlayer2(player,board,22)),
        (isPlayer2(player, board,14) or isPlayer2(player,board,7) or isPlayer2(player,board,8) or isPlayer2(player,board,23)),
        (isPlayer2(player, board,8) or isPlayer2(player,board,17) or isPlayer2(player,board,23)), #Adjecents to pos 16
        (isPlayer2(player, board,9) or isPlayer2(player,board,16) or isPlayer2(player,board,18)), #Adjecents to pos 17
        (isPlayer2(player, board,10) or isPlayer2(player,board,17) or isPlayer2(player,board,19)),
        (isPlayer2(player, board,11) or isPlayer2(player,board,18) or isPlayer2(player,board,20)),
        (isPlayer2(player, board,12) or isPlayer2(player,board,19) or isPlayer2(player,board,21)),
        (isPlayer2(player, board,13) or isPlayer2(player,board,20) or isPlayer2(player,board,22)),
        (isPlayer2(player, board,14) or isPlayer2(player,board,21) or isPlayer2(player,board,23)),
        (isPlayer2(player, board,15) or isPlayer2(player,board,16) or isPlayer2(player,board,22)),
    ]
    return row[position]


# Returns true if a player has a 2-row on the given position.
def isRow2(position, board):
    p = board[position]
    # The player on that position
    if p != -1:
        # If there is some player on that position
        return checkNextRow2(position, board, p)
    else:
        return False

# Return True if a player has a 3-row on the given position
# Each position has an index
def isRow(position, board):
    p = board[position]
    # The player on that position
    if p != -1:
        # If there is some player on that position
        return checkNextRow(position, board, p)
    else:
        return False

# ??????????????
def is2Piece(board, lst, player):
    if board[lst[0]] == player and board[lst[1]] == -1:
        return 1
    return 0

# ???????????
def pieceConfiguration3(board, player):
    rowfrom = [
        [[1,2],[8,16],[7,6]],
        [[9,17]],
        [[1,0],[10,18],[3,4]],
        [[11,19]],
        [[3,2],[12,20],[5,6]],
        [[13,21]],
        [[5,4],[14,22],[7,0]],
        [[15,23]],
        [[9,10],[15,14]],
        [],
        [[9,8],[11,12]],
        [],
        [[11,10],[13,14]],
        [],
        [[13,12],[15,8]],
        [],
        [[8,0],[17,18],[23,22]],
        [[9,1]],
        [[10,2],[17,16],[19,20]],
        [[11,3]],
        [[12,4],[19,18],[21,22]],
        [[13,5]],
        [[14,6],[21,22],[23,16]],
        [[15,7]]
    ]
    for pos in rowfrom:
        if sum([is2Piece(board,lst,player) for lst in pos]) > 1:
            return True
    return False

#board is the current laout on the board

#depth is how many moves in the futures we should look for
#turn is an integer for checking in what game stae we are
#player represent minimizing of maximizing player
#alpha and beta are things ?????????????????

def minmaxstart(board,depth,turn,player,alpha,beta,difficulty):
    if depth==0 :
        return heuristic(board,player,turn,difficulty)  #returns evaluation for bootom node
    if player==1:#this is maximizing player
        value=-10000000000
        if turn<18:
            moves=move_1(board,1)
        elif numOfStones(board,1)==3 and turn>18:
            moves=move_3(board,1)
        else:
            moves=move_2(board,1)

        for newVec in moves:
            value=max(value,minmaxstart(newVec,depth-1,turn+1,0,alpha,beta,difficulty))
            alpha=max(alpha,value)
            if alpha>=beta:
                    break
        return value
    else:
        value=10000000000
        if turn<18:
            moves=move_1(board,0)
        elif numOfStones(board,0)==3 and turn>18:
            moves=move_3(board,0)
        else:
            moves=move_2(board,0)

        for newVec in moves:
            value=min(value,minmaxstart(newVec,depth-1,turn+1,1,alpha,beta,difficulty))
            beta=min(beta,value)
            if alpha>=beta:
                break
        return value


def findNextMove(board,player,turn,depth,difficulty):
    bestMove=[]
    bestMoveVal=-100000000000000000
    currentMove=-1000000
    if turn==0:
        board[11]=1
        return board
    elif turn==1:
        for i in range(24):
            if board[i]==0:
                for pos in adjacentLocations(i):
                    if 7<pos and pos<16:
                        board[pos]=1
                        return board
    elif turn<18:
        moves=move_1(board,1)
    elif numOfStones(board,1)==3 and turn>18:
        moves=move_3(board,1)
    else:
        moves=move_2(board,1)
    for newVec in moves:
         currentMove=minmaxstart(newVec,depth,turn+1,0,-10000000,1000000000,difficulty)
         if(bestMoveVal<=currentMove):
             bestMoveVal=currentMove
             bestMove=newVec

    return bestMove



#this whileloop() p


#  ----------PSUDEO-CODE---------------------------
#function alphabeta(node, depth, α, β, maximizingPlayer) is
#    if depth = 0 or node is a terminal node then
#        return the heuristic value of node
#    if maximizingPlayer then
#        value := −∞
#        for each child of node do
#            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
#            α := max(α, value)
#            if α ≥ β then
#                break (* β cut-off *)
#        return value
#    else
#        value := +∞
#        for each child of node do
#            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
#            β := min(β, value)
#            if α ≥ β then
#                break (* α cut-off *)
#        return value


# readInputFile takes the .json file as input and interprets it.
# Returns the necessary information such the the Game Engine can
# calculate the next move.
def readInputFile(filename):
    with open(filename) as f:
        data = json.load(f)
    # check keys in board
    count = 0
    keys = list(data['Board'].keys())
    #print(keys)
    if len(keys) != 24:
        raise ValueError('Board must have 24 keys')
    #for x in keys:
        #if int(x) != count:
            #print(int(x))
            #print(count)
            #raise ValueError('Keys in board must have values 0 to 23 in ascending order')
        #count = count + 1
    return (list(data['Board'].values()), data['Player'], data['Turn'], data['Difficulty'])

# Definitions for the .json file.
def readablePlayer(player):
    dict = {
        1: 'W',
        0: 'B'

    }
    return dict.get(player, ' ')


# writeOutputFile takes the current board state the the corresponding information
# to write a .json output file. Also prints a visualization of the board in the file.
def writeOutputFile(filename, board, player, turn, difficulty):

    data = {}
    data['Board'] = {x:y for x,y in enumerate(board,0)}
    data['Player'] = player
    data['Turn'] = turn
    data['Difficulty'] = difficulty

    b = list(map(readablePlayer, board))
    data['Visual'] = []
    data['Visual'].append({
        'A':b[0]+'-----'+b[1]+'-----'+b[2],
        'B':'|     |     |',
        'C':'| '+b[8]+'---'+b[9]+'---'+b[10]+' |',
        'D':'| |   |   | |',
        'E':'| | '+b[16]+'-'+b[17]+'-'+b[18]+' | |',
        'F':'| | |   | | |',
        'G':b[7]+'-'+b[15]+'-'+b[23]+'   '+b[19]+'-'+b[11]+'-'+b[3],
        'H':'| | |   | | |',
        'I':'| | '+b[22]+'-'+b[21]+'-'+b[20]+' | |',
        'J':'| |   |   | |',
        'K':'| '+b[14]+'---'+b[13]+'---'+b[12]+' |',
        'L':'|     |     |',
        'M':b[6]+'-----'+b[5]+'-----'+b[4]
    })
    data['Index map'] = []
    data['Index map'].append({
        'A':' 0------- 1------- 2',
        'B':' |        |        |',
        'C':' |  8---- 9----10  |',
        'D':' |  |     |     |  |',
        'E':' |  | 16-17-18  |  |',
        'F':' |  | |      |  |  |',
        'G':' 7-15-23    19-11- 3',
        'H':' |  | |      |  |  |',
        'I':' |  | 22-21-20  |  |',
        'J':' |  |     |     |  |',
        'K':' | 14----13----12  |',
        'L':' |        |        |',
        'M':' 6------- 5------- 4'
    })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2,sort_keys=True)

# Function to run the game. Uses file with necessary information as input.
def runUUGame(filename):
    try:
        (board, player, turn, difficulty) = readInputFile(filename)
    except IOError:
        board = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        turn = 0
        player = 0
        difficulty = 1
    if player != 0 and player != 1:
        raise ValueError('Player must be 0 or 1')
    if not isinstance(turn, int) or turn < 0:
        raise ValueError('Turn must be non-negative integer')
    if not (difficulty == 0 or difficulty == 1 or difficulty == 2):
        raise ValueError('Difficulty must be 0, 1 or 2')
    board = findNextMove(board, player, turn, difficulty + 2,3)
    writeOutputFile(filename, board, 1 - player, turn + 1, difficulty)


'''
try:
    #readInput
    with open('board.json') as jsonfile:
        data = json.load(jsonfile)
        turn = data['Turn']
        turn += 1
        board = list(data['Board'].values())
        player = data['Player']
        difficulty = data['Difficulty']
        filename = 'test.json'
        jsonfile.close()
        #print(board)
except IOError:
    print('The game will now be started from the beginning. Good luck soldier.\n')
    phase = 1
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    turn = 0
    player = 0
    difficulty = 2
    filename = 'board.json'

board = findNextMove(board,1,turn,difficulty,3)
writeOutputFile(filename,board,player,turn,difficulty)
'''



#runnign the code below this comment will run the code for differen difficulties of the ai
#playing against each other printing who is winning.

'''board=[]
for p in range(24):
    board.append(-1)
print("diff 1 starts against diff 2")
turn=0
while(True):
    board=findNextMove(board,1,turn, 1,1)
    turn+=1
    if board.count(0)<=2 and turn>18:
        print("1 wins")
        break
    board=invert_board(board)
    print(turn)
    if(turn%10==0):
        print(turn)

    board=findNextMove(board,1,turn, 2,2)
    if board.count(0)<=2 and turn>18:
        print(" 2 wins")
        break
    board=invert_board(board)
    turn+=1


board=[]
for p in range(24):
    board.append(-1)
print("diff 2 starts against diff 1")
turn=0
while(True):
    board=findNextMove(board,1,turn, 2,2)
    turn+=1
    if board.count(0)<=2 and turn>18:
        print("2 wins")
        break
    board=invert_board(board)
    if(turn%10==0):
        print(turn)

    board=findNextMove(board,1,turn, 1,1)
    if board.count(0)<=2 and turn>18:
        print(" 1 wins")
        break
    board=invert_board(board)
    turn+=1



board=[]
for p in range(24):
    board.append(-1)
print("diff 3 starts against diff 2")
turn=0
while(True):
    board=findNextMove(board,1,turn, 3,3)
    turn+=1
    if board.count(0)<=2 and turn>18:
        print("3 wins")
        break
    board=invert_board(board)
    if(turn%10==0):
        print(turn)

    board=findNextMove(board,1,turn, 2,2)
    if board.count(0)<=2 and turn>18:
        print(" 2 wins")
        break
    board=invert_board(board)
    turn+=1


board=[]
for p in range(24):
    board.append(-1)
print("diff 2 starts against diff 3")
turn=0
while(True):
    board=findNextMove(board,1,turn, 2,2)
    turn+=1
    if board.count(0)<=2 and turn>18:
        print("2 wins")
        break
    board=invert_board(board)
    if(turn%10==0):
        print(turn)

    board=findNextMove(board,1,turn, 3,3)
    if board.count(0)<=2 and turn>18:
        print(" 3 wins")
        break
    board=invert_board(board)
    turn+=1
'''

# TEST runUUGame
# runUUGame('board.json')
