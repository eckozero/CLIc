#!/usr/bin/env python

import Mechanics


"""Reimplementation of CLIc, using (hopefully!) better code
Let's pretend this is V2"""

# Important function below. This allows for easy finding of debugging
# lines rather than using print all of the time.

def debug(*args):
    print args


# Set up the chess board. Rows go down the side (1-8)
# Columns are along the bottom (a-h)

chess_board = [["  8  ","(bR1)", "{bN1}", "(bB1)", "{bQ }", "(bK )", "{bB2}", "(bN2)", "{bR2}"],
	       ["  7  ","{bP1}", "(bP2)", "{bP3}", "(bP4)", "{bP5}", "(bP6)", "{bP7}", "(bP8)"],
	       ["  6  ","(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}"],
	       ["  5  ","{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )"],
	       ["  4  ","(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}"],
               ["  3  ","{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )"],
	       ["  2  ","(wP1)", "{wP2}", "(wP3)", "{wP4}", "(wP5)", "{wP6}", "(wP7)", "{wP8}"],
	       ["  1  ","{wR1}", "(wN1)", "{wB1}", "(wQ )", "{wK }", "(wB2)", "{wN2}", "(wR2)"],
	       ["     ","  A  ", "  B  ", "  C  ", "  D  ", "  E  ", "  F  ", "  G  ", "  H  "]]

# Dictionary to equate column to a numerical value, as integers are 
# easier to manipulate than strings
# File (as in rank and file)
chess_moves_col = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# Dictionary to equate input to actual location on chessboard
# Rank (as in rank and file)
chess_moves_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

# List for pawn moves as they are different to other pieces (need to take
# into consideration if first move, or if piece has reached furthest rank
# and must be promoted)

# TODO: Find out why pawn_moves[x][1] is a 2 and comment accordingly
# DONE: pawn_moves[x][1] refers to current position of pawn on the
# board. As originally written to work the same going up (white pawns)
# and going down (black pawns), the 2 denotes that the piece is on the
# second column
# 
# whilst this made perfect sense at the time, I'm not sure this is still
# the best way to process pawn movement?
pawn_moves = [["bP1",2,0], ["bP2",2,0], ["bP3",2,0], ["bP4",2,0], 
              ["bP5",2,0], ["bP6",2,0], ["bP7",2,0], ["bP8",2,0],
       	      ["wP1",2,0], ["wP2",2,0], ["wP3",2,0], ["wP4",2,0], 
	      ["wP5",2,0], ["wP6",2,0], ["wP7",2,0], ["wP8",2,0]]


# Constant(s)
EMPTY_SPACE = ("(   )","{___}")


# Variables that need instantiating before the program runs

valid_move = False
turn_counter = 10
turn = "White's"
# Agreed that this is needed (currently) but why? Can this be removed
# and replaced with, for example, turn[0].lower()?
piece_colour = "w"

# Again, this may not be needed with some better coding
playing = True
onwards = False

# Castling variables
white_king_moved = False
black_king_moved = False
wR1_moved = False
wR2_moved = False
bR1_moved = False
bR2_moved = False

# Variables for check
white_king_check = False
black_king_check = False


# Instantiate classes - all blank instances as each
# variable needs to be passed every time a method is
# called

drawBoardFunc = Mechanics.DrawBoard()
checkCheck = Mechanics.CheckForCheck()
pawnMoves = Mechanics.PawnMovement()
pieceMoves = Mechanics.PieceMovement()
castling = Mechanics.Castling()
rules = Mechanics.Gameplay()


drawBoardFunc.print_board(chess_board)


#def play_game():
while playing == True:
    while onwards == False:
        valid_move = False

        var_list = [turn, white_king_moved, black_king_moved, wR1_moved, wR2_moved, bR1_moved, bR2_moved]

        move1, move2 = rules.move_selection(turn, var_list)
        
        # There are lots of ways that input for move1 and move2 can
        # break things. User could try to use blank input, or a letter
        # that's further than the 8 columns, or a number that isn't
        # 1-8. Try/except below attempts to catch any errors that
        # would otherwise cause CLIc to fail
        try:
            chess_moves_col[move1[0]] != ""
            chess_moves_row[move1[1]] != ""
            (move1[0].lower() and move2[0].lower()) in chess_moves_col
            (move1[1] and move2[1]) in range(9)
        except (IndexError, KeyError):
            print "Not a valid move"
            drawBoardFunc.print_board(chess_board)
            move1 = move2 = "zz"
    
        finally:
            # Measuring length returns true or false, not any errors
            # Below code checks that move is exactly 2 characters long
            # and changes move1 + move2 to "zz" so that the loop fails
            # and input is requested again
            if len(move1) != 2 or len(move2) !=2:
                print "Sorry, I didn't quite catch that move (did it have the right number of characters?)"
                print move1 + "-" + move2
                move1 = move2 = "zz"

        if move1 != "zz" and move2 != "zz":
            column = chess_moves_col[move1[0]]
            row = chess_moves_row[move1[1]]
            onwards = True
        else:
            onwards = False
    
    # Map on the chess board where the end destination is (piece moving TO)
    new_column = chess_moves_col[move2[0]]
    new_row = chess_moves_row[move2[1]]


    turn, valid_move, turn_counter = rules.move_valid(chess_board, row, column, valid_move, turn, turn_counter)

    # Redraw the board - this might want to go at the top of the loop, to be
    # picked up before a new move is requested
    #
    # I'm sure it will become apparent where it needs to go as I proceed
    #turn, valid_move, turn_counter = rules.change_turn(valid_move, turn_counter)

    #drawBoardFunc.print_board(chess_board)
    # Test

    drawBoardFunc.redraw_board(chess_board, row, column, new_row, new_column)

    onwards = False
