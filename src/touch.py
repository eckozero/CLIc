#!/usr/bin/env python

from DrawBoard import DrawBoard
print DrawBoard
valid_move = True
chess_board = 0

drawBoard = DrawBoard(valid_move, chess_board)
drawBoard.printy()

def debug(*args):
	print args

x = 5
y = 3

debug([x*y, "Hello", 1, 2, 3, 4, 5])
