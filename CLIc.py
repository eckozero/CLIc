#!/usr/bin/env python
# Program written by Paul Lenton (EckoZero) - <"lentonp" at "gmail" dot "com">
# Copyright 2013
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the 
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, 
# Boston, MA  02110-1301, USA.
#
#
# CLIc stands for "Command Line Interface chess" given that this is
# written in Python, and I'm still a n00blet by hacker standards, there
# is no computer opponent, instead you'll have to find a friend to play
# with - sorry. Maybe if I ever get REALLY good at coding, I'll write
# a chess engine so you can play against the computer. Don't hold your
# breath though.
#
# Seriously though, it took 2 hours of coding to deal with pawn promotion
# so please don't get your hopes up
# 
#
# I think it's fair to say that this is now a v0.2 jobby what with pawn
# promotion and valid knight input included...



				#rows down the side (1-8)
chess_board = [["  8  ","(bR1)", "{bN1}", "(bB1)", "{bK }", "(bQ )", "{bB2}", "(bN2)", "{bR2}"],
			   ["  7  ","{bP1}", "(bP2)", "{bP3}", "(bP4)", "{bP5}", "(bP6)", "{bP7}", "(bP8)"],
			   ["  6  ","(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}"],
			   ["  5  ","{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )"],
			   ["  4  ","(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}"],
               ["  3  ","{___}", "(   )", "{___}", "(   )", "{___}", "(   )", "{___}", "(   )"],
			   ["  2  ","(wP1)", "{wP2}", "(wP3)", "{wP4}", "(wP5)", "{wP6}", "(wP7)", "{wP8}"],
			   ["  1  ","{wR1}", "(wN1)", "{wB1}", "(wQ )", "{wK }", "(wB2)", "{wN2}", "(wR2)"],
			   ["     ","  A  ", "  B  ", "  C  ", "  D  ", "  E  ", "  F  ", "  G  ", "  H  "]]
				#columns along the bottom (A-H)
				
chess_dim = range(len(chess_board))

chess_moves_col = {"a" or "A": 1, "b" or "B": 2, "c" or "C": 3, "d" or "D": 4,
				   "e" or "E": 5, "f" or "F": 6, "g" or "G": 7, "h" or "H": 8}

chess_moves_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
white_pawn_row = [0,1,2,3,4,5,6,7,8,9]
# Some variables
pawn = ""
quit_game = False
turn_counter = 10
valid_move = True

# Experimental crap start
# Increment hours when playing around
# Time spent == 2 hours
# COMPLETE
# Note to future me:
# This section is magic, 2am, caffeine induced, sleep deprived code
# unless you are really sure what you're changing... DON'T!


pawn_moves = [["bP1",2,0], ["bP2",2,0], ["bP3",2,0], ["bP4",2,0], 
			  ["bP5",2,0], ["bP6",2,0], ["bP7",2,0], ["bP8",2,0],
			  ["wP1",2,0], ["wP2",2,0], ["wP3",2,0], ["wP4",2,0], 
			  ["wP5",2,0], ["wP6",2,0], ["wP7",2,0], ["wP8",2,0]]

def pawn_promotion(piece_colour):
	promotion = False
	# Check if piece moved is a pawn
	for every in range(len(pawn_moves)):
		check_pawn = pawn_moves[every][0]
		if chess_board[row][column] == check_pawn:
			# replace number value from list with new location of pawn
			pawn_moves[each][1] = chess_moves_row[chess_board[new_row][0][2]]
	# iterate through pawn_moves list to find and replace the pawns 
	# position on the chess board
	for each in range(len(pawn_moves)):
		if pawn_moves[each][1] == 7 or pawn_moves[each][1] == 0:
			# pawn has reach furthest rank and is to be promoted
			# TODO: Enable selection of promotion piece
			# Fixed: 13/07/13 02.15
			pieces = ["Q", "B", "R", "N"] 
			while promotion == False:
				new_piece = str(raw_input("\nPlease select which piece pawn is to be promoted to: \n"))
				if new_piece.upper() in pieces:
					promotion = True
				else:
					print "\nSorry, I don't think that's a real piece."
					print "Just use the first letter of the piece you want"
			if chess_board[new_row][new_column][0] == "{":
				pawn_moves[each][0] = "{" + piece_colour + new_piece.upper() + " }"
			else:
				pawn_moves[each][0] = "(" + piece_colour + new_piece.upper() + " )"
			pawn = str(pawn_moves[each][0])

# End of experimental crap

# More experimental crap
# Started 17/07/13 @ 18:20
# Time spent == 5 hours
# Completed 18/07/13 @ 20:45
# 
# FIXME: Cannot move knight from g to h as this overspills last
# column in list
# FIXED: 20/07/13 @ 21:29

def knight_move_valid():
	row_valid = False
	column_valid = False
	if chess_board[new_row-2] == chess_board[row] or chess_board[new_row+2] == chess_board[row]:
		row_valid = True
	elif chess_board[new_row-1] == chess_board[row] or chess_board[new_row+1] == chess_board[row]:
		row_valid = True
	else:
		row_valid = False

	if chess_board[new_column-2] == chess_board[column] or chess_board[new_column] == chess_board[column-2]:
		column_valid = True
	elif chess_board[new_column-1] == chess_board[column] or chess_board[new_column] == chess_board[column-1]:
		column_valid = True
	else:
		column_valid = False
	
	if row_valid is True and column_valid is True:
		return 1
	else:
		return 0
		
def knight_move(piece_colour):
	"""Check knight's move is valid"""
	global knight
	knight = ""
	is_it_correct = knight_move_valid()
	if is_it_correct == 1:
		if chess_board[new_row][new_column][0] == "{":
			knight = "{" + piece_colour + "N }"
		else:
			knight = "(" + piece_colour + "N )"
		valid_move = True
		return 1
	else:
		print "Knights can't move like that =( "
		valid_move = False
		return 0

def redraw_valid(valid_move):
	if valid_move is True:
		chess_board[new_row][new_column] = chess_board[row][column]
		if chess_board[row][column][0] == "{":
			chess_board[row][column] = "{___}"
		else:
			chess_board[row][column] = "(   )"

# End second set of experimental crap

# Introducing the third set of experimental crap
# Bishop and rook moves
# Started 20/07/13 @ 16:40
# Completed 20/07/13 @ 17:30
# Hey, check me out; I wrote 2 parent functions and 2 child
# functions in less than an hour!
# Now CLIc accepts only valid knight, bishop and rook moves

def bishop_move(piece_colour):
	"""Check bishop's move is valid"""
	global bishop
	bishop = ""
	is_it_correct_b = bishop_move_valid()
	if is_it_correct_b == 1:
		if chess_board[new_row][new_column][0] == "{":
			bishop = "{" + piece_colour + "B }"
		else:
			bishop = "(" + piece_colour + "B )"
		valid_move = True
		return 1
	else:
		print "Bishops can't move like that =( "
		valid_move = False
		return 0

def bishop_move_valid():
	move_valid = False
	if chess_board[new_column][new_row][0] != chess_board[row][column][0]:
		move_valid = False
	else:
		x = new_row - row
		y = new_column - column
		if x == y:
			move_valid = True
			
	if move_valid is True:
			return 1
	else:
		return 0

def rook_move(piece_colour):
	"""Check rook's move is valid"""
	global rook
	rook = ""
	is_it_correct_r = rook_move_valid()
	if is_it_correct_r == 1:
		if chess_board[new_row][new_column][0] == "{":
			rook = "{" + piece_colour + "R }"
		else:
			rook = "(" + piece_colour + "R )"
		valid_move = True
		return 1
	else:
		print "Rooks can't move like that =( "
		valid_move = False
		return 0

def rook_move_valid():
	move_valid = False
	x = new_column - column
	y = new_row - row
	if (x == 0 or y == 0) and (x != 0 or y != 0):
		move_valid = True
			
	if move_valid is True:
			return 1
	else:
		return 0

# End of experimental crap 3

# New stuff - pawn movement (excepting promotion) and eventually...
# en passant, maybe
def pawn_move_valid(piece_colour):
	"""Check pawn's move is valid"""
	valid_move = False
	pawn = ""
	y = new_row
	global x, each, super_x
	super_x = 0
	x = 0
#	is_it_correct_p = pawn_move_valid()
	for each in range(len(pawn_moves)):
		if pawn_moves[each][0][0:4] == chess_board[row][column][1:4]:
			if pawn_moves[each][0][0] == "w":
				x = int(move2[1]) - int(move1[1])
				#x = pawn_moves[each][1] - new_column
			elif pawn_moves[each][0][0] == "b":
				x = new_column - pawn_moves[each][1]
				#x = pawn_moves[each][1] - chess_moves_row[str(y)]
			else:
				break
			super_x = each
			#debugging line
			print x, super_x
			if ((x == 1 or x == 2) and pawn_moves[each][2] == 0):
				pawn_moves[each][1] = y
				pawn_moves[each][2] += 1
			elif x == 1 and pawn_moves[each][2] > 0:
				pawn_moves[each][1] = y
				pawn_moves[each][2] += 1
			else:
				pawn = "invalid"
			#break
		#debugging line
		#print x
		#print pawn_moves[each][0][0:4], chess_board[row][column][1:4]
		#new_column = chess_moves_col[move2[0]]
		#new_row = chess_moves_row[move2[1]]

	if pawn == "":
		if x == 1:
			#if chess_board[new_row][new_column][0] == "{":
			#	pawn = "(" + piece_colour + pawn_moves[each][0] + ")"
			#else:
			#	pawn = "{" + piece_colour + pawn_moves[each][0] + "}"
			valid_move = True
		elif x == 2:
		#	if chess_board[row][column][0] == "{":
		#		pawn = "{" + piece_colour + pawn_moves[each][0] + "}"
		#	else:
		#		pawn = "(" + piece_colour + pawn_moves[each][0] + ")"
			valid_move = True
	else:
		print "Pawns can't move like that =( "
		valid_move = False
	
	if valid_move is True:
		return 1
	else:
		return 0


def redraw_valid_for_pawns(valid_move):
	global pawn, x, super_x
	if valid_move is True:
		if pawn == "":
			if x == 1:
				if chess_board[row][column][0] == "{":
					pawn = "(" + pawn_moves[super_x][0] + ")"
				else:
					pawn = "{" + pawn_moves[super_x][0] + "}"
			elif x == 2:
				if chess_board[row][column][0] == "{":
					pawn = "{" + pawn_moves[super_x][0] + "}"
				else:
					pawn = "(" + pawn_moves[super_x][0] + ")"
			chess_board[new_row][new_column] = pawn



def print_board():
	counter1 = 0
	for i in chess_dim:
		print "".join(chess_board[counter1])
		counter1 +=1

while quit_game == False:
	# print board for the first time
	print_board()
	# check whose turn it is
	if (turn_counter % 2 == 0):
		turn = "White's"
	else:
		turn = "Black's"
	#take a starting piece and where to move it to
	#also checks that player does not wish to quit
	move1 = raw_input(turn + " turn. Pick which piece to move: ")
	if move1 in ("q","Q"):
		quit_game = True
		break
	else:
		move2 = raw_input("Where would you like to move to: ")
		if move2 in ("q","Q"):
			quit_game = True
			break
	#assign it a value to check against dictionary
	column = chess_moves_col[move1[0]]
	row = chess_moves_row[move1[1]]
	
	#check that move input is valid
	if (column in range(1,9)) and (row in range(0,8)):
		new_column = chess_moves_col[move2[0]]
		new_row = chess_moves_row[move2[1]]
	else:
		print "\nThat's not a valid move! Try again \n"
		turn_counter -=1
		valid_move = False
	if chess_board[row][column][1] == " ":
		print "\nThat's not a valid move! Try again \n"
		turn_counter -=1
		valid_move = False



	#check that player has picked their own piece
	if valid_move != False:

		if chess_board[row][column][1] != (turn[0]).lower():
			print "That's not your piece! Try again!"
			turn_counter -= 1
	#check that piece can move in that manner
	
	
	#check if pawn has reached furthest rank and hence been promoted
		piece_colour = turn[0].lower()
		if chess_board[row][column][2] == "P" and (new_row == 0 or new_row == 8):
			if pawn_promotion(piece_colour) == 1:
				print "\nPawn promoted!\n"
				chess_board[new_row][new_column] = pawn
		elif chess_board[row][column][2] == "P":
			if pawn_move_valid(piece_colour) == 1:
				chess_board[new_row][new_column] = pawn
				redraw_valid(valid_move)
			else:
				turn_counter -= 1
		elif chess_board[row][column][2] == "N":
			if knight_move(piece_colour) == 1:
				chess_board[new_row][new_column] = knight
				redraw_valid(valid_move)
			else:
				turn_counter -= 1
		elif chess_board[row][column][2] == "B":
			if bishop_move(piece_colour) == 1:
				chess_board[new_row][new_column] = bishop
				redraw_valid(valid_move)
			else:
				turn_counter -=1
		elif chess_board[row][column][2] == "R":
			if rook_move(piece_colour) == 1:
				chess_board[new_row][new_column] = rook
				redraw_valid(valid_move)
			else:
				turn_counter -=1
	#redraw board, replacing the two items in list that have been moved
	#from and to
	
	#change player
		turn_counter += 1
