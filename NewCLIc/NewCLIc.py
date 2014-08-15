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
chess_moves_col = {"a" or "A": 1, "b" or "B": 2, "c" or "C": 3, "d" or "D": 4,
		   "e" or "E": 5, "f" or "F": 6, "g" or "G": 7, "h" or "H": 8}

# Dictionary to equate input to actual location on chessboard
chess_moves_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

# Variables that need instantiating before the program runs

valid_move = True
turn_counter = 10
turn = "White's"


drawBoardFunc = Mechanics.DrawBoard(chess_board, valid_move)

drawBoardFunc.print_board()

def move_selection(turn):
    move1 = raw_input(turn + " turn. Pick which piece to move: ")
    if len(move1) == 0:
        move1 = "zz"
    if move1[0].lower() == "q":
        end_game()
    else:
        move2 = raw_input("Where would you like to move to: ")
        if len(move2) == 0:
            move2 = "zz"
        if move2[0].lower() == "q":
            end_game()
    
    if move1 == "o-o" or move1 == "o-o-o":
        pass

    return move1, move2

def end_game():
    print "Quitting."
    exit()




def play_game():
    move1, move2 = move_selection(turn)

    try:
        chess_moves_col[move1[0]] != ""
        chess_moves_row[move1[1]] != ""
        (move1[0] and move2[0]) in chess_moves_col
        (move1[1] and move2[1]) in range(9)
        len(move1) >=2 and len(move2) >=2
    except (IndexError, KeyError):
        print "Not a valid move"
        pass
    
    else:
        if len(move1) != 2 or len(move2) !=2:
            print "Sorry, I didn't quite catch that move (maybe it had too many numbers?)"
            print move1 + "-" + move2



    drawBoardFunc.print_board()





play_game()
