# UUGame-Engine

Definitions:
A valid board is defined by: The board is represented by a vector of length 24. The indices are arranged in a spiral with zero at top left and then going clock wise, see print board for more details. The values of the array are 0 for black, 1 for white and -1 for empty. The positions of the pieces on the board must conform to the rules of the game.

A player is 0 for black and 1 for white

Difficulty levels are 0 for easy, 1 for normal, 2 for hard

A *move* is either the placement of a stone at a position on the board, the removal of a stone from a position on the board or moving a stone from one position of the board to another.

The phase is a tuple of integers with the first element the phase for black and the second the phase for white

*Functions*:

*Function*: main()
Description: Reads input file, finds the best move and writes an updated board into an output file.

*Function*: readinputfile(filename)
Description: Reads input file
Pre-conditions: The file conforms to the right format, see US007
Post-conditions: Returns a tuple where the elements are, in order: 0: valid board 1: player whose turn it is 2: the phse of the game
				 3: the game turn 4: the difficulty level. These values must correspond to their counterparts in the input file.

*Function*: writeoutputfile(filename, board, player, turn, phase, difficulty)
Description: Writes the output file
Pre-conditions: filename is a valid file name. board is a valid board. player, turn, phase, difficulty are the player, turn, phase and difficulty of the current game
Post-conditions: Writes a file conforming to the right format (see US007). This file will contain the corresponding values from the input variables.

*Function*: adjacentLocations(position)
Pre-conditions: position is a valid position (in range 0:23)
Post-conditions: For every postition on the board, the functions returns its adjacent positions.

*Function*: checkNextRow(position, board, player):
Pre-conditions: position is a valid position (in range 0:23), board is valid and player is either 0 or 1 (representing black or white)
Post-condistions: returns True if a player can make a row of three stones in the next move.

*Function*: checkNextRow2(position, board, player):
Pre-conditions: position is a valid position (in range 0:23), board is valid and player is either 0 or 1 (representing black or white)
Post-condistions: returns True if a player can make a row of two stones in the next move.

*Function*: isRow(position, board):
Pre-conditoins: position and board is valid.
Post-conditions. returns True if placing a stone in position 'position' makes a three in a row.

*Function*: isRow2(position, board):
Pre-conditoins: position and board is valid.
Post-conditions. returns True if placing a stone in position 'position' makes a two in a row.

*Function*: findnextmove(board, player, phase, turn, difficulty)
Pre-conditions: board is a valid board. player is a player. difficulty is a difficulty level.
Post-conditions: returns the best possible move, according to the difficulty level, that player can make from the specified board and phase.

*Function*: minmaxstart(board, depth, player, phase, turn, difficulty)
Description: Use minmax method with alpha beta pruning to find a value for the best move.
Pre-conditions: board is a valid board, player is the player at this depth, difficulty is the difficulty level, depth >= 0 is the depth of the recursion
Post-conditions: if player is 2, of all possible moves at this depth return the one for which minmaxstart returns the lowest value
				 if player is 1, of all possible moves at this depth return the one for which minmaxstart returns the highest value

*Function*: heuristic(board, player)
Description: Calculates the value of the board for the indicated player. The heuristics are
	- 3 in a row: 500 pts
	- 2 in a row:
Pre-conditions: board is a valid board, player is the player at this depth of the minmax search tree
Post-conditions: returns the heuristic value of this board for this player

*Function*: validmove(board, move, turn, phase)
Pre-conditions: board is a valid board, move is either a placed stone or a removed stone, turn is the game turn, phase is the phase of the game
Post-conditions: returns true if this move is possible given this board, turn and phase, according to the rules of the game
				         false otherwise

*Function*: updateboard(board, move, player, phase, turn)
Description: Make a move and steal a piece if possible
Pre-conditions: board is a valid board, move is a valid move, player is the player, phase is the phase of the game, turn is the game turn
Post-conditions: returns a valid board for which the indicated move has been performed, according to the game rules.
