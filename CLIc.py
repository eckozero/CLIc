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
# with - sorry.
#
# Eventually there be will the option to play this over a network so you
# can play with your friends who are likewise procrastinating


				#rows down the side (1-8)
chess_board = [["  8  ","(bR1)", "{bN1}", "(bB1)", "{bQ }", "(bK )", "{bB2}", "(bN2)", "{bR2}"],
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

# dictionary to equate column to a numerical value, as integers are 
# easier to manipulate than strings
chess_moves_col = {"a" or "A": 1, "b" or "B": 2, "c" or "C": 3, "d" or "D": 4,
		   "e" or "E": 5, "f" or "F": 6, "g" or "G": 7, "h" or "H": 8}

#dictionary to equate input to actual location on chessboard
chess_moves_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

# specific to white pawns - manipulation of numbers is easier working forwards
# not backwars
white_pawn_row = [0,1,2,3,4,5,6,7,8,9]


# Instantiate some variables
pawn = ""
quit_game = False
turn_counter = 10
valid_move = True
turn = "White's"

# Magic variables. A.K.A. lazy code to facilitate complex rules
empty_space = ("(   )" ,"{___}")
white_king_moved = False
black_king_moved = False
wR1_moved = False
wR2_moved = False
bR1_moved = False
bR2_moved = False
white_king_check = False
black_king_check = False


# Special list for pawn moves, as rules for pawns are vastly different
# to other pieces
pawn_moves = [["bP1",2,0], ["bP2",2,0], ["bP3",2,0], ["bP4",2,0], 
              ["bP5",2,0], ["bP6",2,0], ["bP7",2,0], ["bP8",2,0],
       	      ["wP1",2,0], ["wP2",2,0], ["wP3",2,0], ["wP4",2,0], 
	      ["wP5",2,0], ["wP6",2,0], ["wP7",2,0], ["wP8",2,0]]


class DrawBoard(object):
	def __init__(self, valid_move):
		self.valid_move = valid_move
		
	def print_board(self):
		"""Prints chess board"""
		counter1 = 0
		for i in chess_dim:
			print "".join(chess_board[counter1])
			counter1 +=1
	
	# FIXME: Redraw doesn't work for anything other than pawns
	# FIXED: 20/10/13 - ^^ yes it does
	def redraw_valid(self, valid_move):
		"""Checks that move is valid, then redraws piece on board"""
		if piece_colour != chess_board[row][column][1]:
			return 0
		else:
			if valid_move is True:
				if chess_board[row][column][2] == "P":
#				if pawn_capture(row, column, new_row, new_column) == 0:
					redraw_valid_for_pawns(valid_move)
				else:
					old_piece = chess_board[row][column][0] 
					new_piece = chess_board[row][column][1:4] 
					redraw_piece = chess_board[new_row][new_column][0] #curly brace
					if redraw_piece == "{": 
						chess_board[new_row][new_column] = "{" + new_piece + "}"
					
					else:
						chess_board[new_row][new_column] = "(" + new_piece + ")"
					if old_piece == "{": 
						chess_board[row][column] = "{___}" 
					else:
						chess_board[row][column] = "(   )"
				

class GameMechanics(object):
	def __init__(self, turn_counter):
		self.turn_counter = turn_counter

	def turn_picker(self, turn_counter):
		if (turn_counter % 2 == 0):
			turn = "White's"
		else:
			turn = "Black's"
		return turn


class Check(object):
	def __init__(self, white_king_check, black_king_check):
		self.white_king_check = white_king_check
		self.black_king_check = black_king_check
	
	def find_king(self):
		for pieces in range(9):
			for columns in range(9):
				if chess_board[pieces][columns][2] == "K":
					if chess_board[pieces][columns][1] == piece_colour:
						# successfully found King. Assign location to
						# a variable
#						print "Test hit"
						check_row = pieces
						check_column = columns
						break
		return check_row, check_column

	def check_h(self):
		"""Checks horizontal moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king()
		col_range1 = range(1, check_column+1)
		col_range2 = range(((8 - check_column)*-1), 0)
		col_range2.reverse()
		super_list = [col_range1, col_range2]
#		print col_range1, col_range2
		for each in super_list:
			for every in range(0, len(each)):
				check_space = chess_board[check_row][check_column - (each[every])]
#				print check_space
				if check_space in empty_space:
				# space is empty - move on
					pass
				else:
					# is it a piece space?
					if check_space[0] != "{" and check_space[0] != "(":
						pass
					# space not empty. is it your piece?
					if check_space[1] != piece_colour:
					# Not your piece. is it attacking piece with a
					# vaid attack on king?
						if check_space[2] == "Q" or check_space[2] == "R":
						# Yes to above. King is in check
							local_check = True
							break
					else:
						# Your piece is blocking
						local_check = False
						break
						
		return local_check
		
	def check_v(self):
		"""Checks horizontal moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king()
		row_range1 = range(1, check_row+1)
		row_range2 = range(((8 - check_row) * -1), 0)
		row_range2.reverse()
		super_list = [row_range1, row_range2]
#		print row_range1, row_range2
		for each in super_list:
			for every in range(0, len(each)):
				check_space = chess_board[check_row - (each[every])][check_column]
#				print check_space
				if check_space in empty_space:
				# space is empty - move on
					pass
				else:
					# is it a piece space?
					if check_space[0] != "{" or check_space[0] != "(":
						pass
					# space not empty. is it your piece?
					if check_space[1] != piece_colour:
					# Not your piece. is it attacking piece with a
					# vaid attack on king?
						if check_space[2] == "Q" or check_space[2] == "R":
						# Yes to above. King is in check
							local_check = True
							break
					else:
						# Your piece is blocking
						local_check = False
						break
						
		return local_check
	
	def check_d(self):
		"""Checks horizontal moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king()
		row_range1 = range(1, check_row+1)
		row_range2 = range(((8 - check_row) * -1), 0)
		row_range2.reverse()
		col_range1 = range(1, check_column+1)
		col_range2 = range(((8 - check_column)*-1), 0)
		col_range2.reverse()
		super_list = [row_range1, row_range2, col_range1, col_range2]
#		print super_list
#		"""Issue below is that there is no difference in the row/col ranges
#		it is running the same validation as it moves through the 4 iterable
#		items in the list. Need to make it run each of 4 possible validations
#		separately (+/+, +/-, -/+, -/- for row/column)"""
		counter = 0
		for each in super_list:
#			print local_check
			if local_check == True:
				break
			for every in range(0, len(each)):
				if counter == 0:
					check_space = chess_board[check_row - (each[every])][check_column - (each[every])]
				elif counter == 1:
					check_space = chess_board[check_row - (each[every])][check_column - (each[every])]
				elif counter == 2:
					check_space = chess_board[check_row - (each[every])][check_column + (each[every])]
				elif counter == 3:
					check_space = chess_board[check_row - (each[every])][check_column + (each[every])]


#				print check_space

				if check_space in empty_space:
				# space is empty - move on
					pass
				else:
					# is it a piece space?
					if check_space[0] == "{" or check_space[0] == "(":
					# space not empty. is it your piece?
						if check_space[1] != piece_colour:
					# Not your piece. is it attacking piece with a
					# vaid attack on king?
							if check_space[2] == "Q" or check_space[2] == "B":
							# Yes to above. King is in check
								local_check = True
								break
						else:
							# your piece - no threat
							break
					else:
					# not a piece space
						break
			counter += 1	
		return local_check
		
	def check_k(self):
		"""Checks if King is in check from Knight"""
		local_check = False
		check_row, check_column = self.find_king()
		# knight check positions are:
		# row+2 column+1, row+2 column-1, row-2 column+1, row-2 column-1
		# row+1 column+2, row+1 column-2, row-1 column+2, row-1 column-2
		super_list = [[2,1],[-2,1],[-2,1],[2,1],[1,2],[-1,2],[1,-2],[1,2]]
		counter = 0
		for each in super_list:
			check_space = ""
#			print each, check_row, check_column, (check_row + each[0])
			if local_check == True:
				break
			for every in range(0,len(super_list)):
				if counter % 2 == 0:
					if (check_row + each[0]) <= 8 and (check_row + each[0]) >= 0:
						if (check_column + each[1]) <= 8 and (check_column + each[1]) >= 0:
							check_space = chess_board[check_row+(each[0])][check_column+(each[1])]
				else:
					if (check_row - each[0]) <= 8 and (check_row - each[0]) >= 0:
						if (check_column - each[1]) <= 8 and (check_column - each[1]) >= 0:
							check_space = chess_board[check_row-(each[0])][check_column-(each[1])]

#				print check_space
				
				if check_space != "":
				
					if check_space in empty_space:
				# space is empty - move on
						pass
					else:
				# is it a piece space?
						if check_space[0] == "{" or check_space[0] == "(":
				# space not empty. is it your piece?
							if check_space[1] != piece_colour:
				# Not your piece. is it attacking piece with a
				# vaid attack on king?
								if check_space[2] == "N":
					# Yes to above. King is in check
									local_check = True
#									print "big brain am winning again"
									break
							else:
						# your piece in the way
								break
				counter += 1	
		return local_check


checkCheck = Check(white_king_check, black_king_check)


def pawn_promotion(piece_colour):
	"""Determine whether or not pawn has reached furthest rank from start point"""
	global pawn
	promotion = False
	# Check if piece moved is a pawn
	for every in range(len(pawn_moves)):
		check_pawn = pawn_moves[every][0]
		if chess_board[row][column] == check_pawn:
			# replace number value from list with new location of pawn
			pawn_moves[super_x][1] = chess_moves_row[chess_board[new_row][0][2]]
	# iterate through pawn_moves list to find and replace the pawn's 
	# position on the chess board
	for each2 in range(len(pawn_moves)):
		if pawn_moves[each2][1] == 7 or pawn_moves[each2][1] == 0:
			# pawn has reach furthest rank and is to be promoted
			# Enable selection of promotion piece
			pieces = ["Q", "B", "R", "N"] 
			while promotion == False:
				new_piece = str(raw_input("\nPlease select which piece pawn is to be promoted to: \n"))
				if new_piece.upper() in pieces:
					promotion = True
				else:
					print "\nSorry, I don't think that's a real piece."
					print "Just use the first letter of the piece you want"
			# Check whether Pawn is promoted on a white square or black square
			if chess_board[new_row][new_column][0] == "{":
				pawn_moves[each2][0] = "{" + piece_colour + new_piece.upper() + " }"
			else:
				pawn_moves[each2][0] = "(" + piece_colour + new_piece.upper() + " )"
			pawn = str(pawn_moves[each2][0])
#	if chess_board[row][column][0] == "{":
#		chess_board[row][column] = "{   }"
#	else:
#		chess_board[row][column] = "(   )" 
	return pawn




 
# FIXME: Cannot move knight from g to h as this overspills last
# column in list
# FIXED: 20/07/13 @ 21:29
# FIXME: Knight moves are acceptabl at (column+1 & row+1)

def knight_move_valid():
	"""Determine whether Knight can move in that manner"""
	row_valid = False
	column_valid = False
	# Knight moves are (column+2 & row+1) or (column+1 & row+1)
	# Run validation on each move individually, and combine
	if chess_board[new_column-2] == chess_board[column] or chess_board[new_column] == chess_board[column-2]:
		if chess_board[new_row-1] == chess_board[row] or chess_board[new_row+1] == chess_board[row]:
			column_valid = True
	elif chess_board[new_column-1] == chess_board[column] or chess_board[new_column] == chess_board[column-1]:
		if chess_board[new_row-2] == chess_board[row] or chess_board[new_row+2] == chess_board[row]:
			column_valid = True
	else:
		column_valid = False
	
	if column_valid is True:
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



# Bishop and rook moves
# Started 20/07/13 @ 16:40
# Completed 20/07/13 @ 17:30
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
	"""Bishops move row+n and column+n"""
	move_valid = False
	if (chess_board[new_row][new_column][0] == chess_board[row][column][0]) is False:
		move_valid = False
#		print "debug in bishop"
#		print (chess_board[new_row][new_column][0] == chess_board[row][column][0])
	else:
		# n - n for x and y movement must be equal if move is valid
		x = new_row - row
		y = new_column - column
		if x**2 == y**2:
			move_valid = True
			
	if move_valid is True:
			return 1
	else:
		return 0

def rook_move(piece_colour):
	"""Check rook's move is valid"""
	global rook, wR1_moved, wR2_moved, bR1_moved, bR2_moved
	rook = ""
	is_it_correct_r = rook_move_valid()
	if is_it_correct_r == 1:
		if chess_board[new_row][new_column][0] == "{":
			rook = "{" + piece_colour + "R" + chess_board[row][column][3] + "}"
		else:
			rook = "(" + piece_colour + "R" + chess_board[row][column][3] + ")"
		valid_move = True
		if rook == "(wR1)" or rook == "{wR1}":
			wR1_moved = True
		elif rook == "(wR2)" or rook == "{wR2}":
			wR2_moved = True
		elif rook == "(bR2)" or rook == "{bR2}":
			bR2_moved = True
		else:
			bR1_moved = True
		return 1
	else:
		print "Rooks can't move like that =( "
		valid_move = False
		return 0

def rook_move_valid():
	"""Rook move is (row+-n & column+-0) or (row+-0 & column+-n)"""
	move_valid = False
	x = new_column - column
	y = new_row - row
	if (x == 0 or y == 0) and (x != 0 or y != 0):
		move_valid = True
#		print "rook debug"
	if move_valid is True:
			return 1
	else:
		return 0

# Queen moves ahead.

def queen_move(piece_colour):
	global queen, valid_move
	queen = ""
	is_it_correct_q = queen_move_valid()
	if is_it_correct_q == 1:
		if chess_board[new_row][new_column][0] == "{":
			queen = "{" + piece_colour + "Q }"
		else:
			queen = "(" + piece_colour + "Q )"
		valid_move = True
		return 1
	else:
		print "Queens can't move like that =( "
		valid_move = False
		return 0


def queen_move_valid():
	"""Valid queen moves commented below"""
	#row +/- n & column = 0, column +/- n & row = 0 (rook moves)
	#row +/- n & column +/- n (bishop moves)
	# assume move is wrong - get corrected later
	queen_move = rook_move_valid()
	if queen_move == 1:
		return 1
	queen_move = bishop_move_valid()
	if queen_move == 1:
		return 1
	else:
		return 0

# Take this, it's dangerous to go alone!
# You received "King Moves"!

def king_move_valid():
	"""Kings move like queens, except one space at a time"""
	global move_valid
	move_valid = False
	x = new_column - column
	y = new_row - row
#	Debugging line
#	print x**2, y**2, x, y
	if (x == 0 or y == 0) and (x == 1 or y == 1):
		move_valid = True
		return 1
	if (x**2 == 1 or y**2 == 1) and (x <= 0 or y <= 0):
		move_valid = True
		return 1
	else:
		return 0

def king_move(piece_colour):
	global king, valid_move, white_king_moved, black_king_moved
	king = ""
	is_it_correct_k = king_move_valid()
	if is_it_correct_k == 1:
		if chess_board[new_row][new_column][0] == "{":
			king = "{" + piece_colour + "K }"
		else:
			king = "(" + piece_colour + "K )"
		valid_move = True
		if king == "(wK )":
			white_king_moved = True
		elif king == "{wK }":
			white_king_moved = True
		else:
			black_king_moved = True
#		print king
		return 1
	else:
		print "Kings can't move like that =( "
		valid_move = False
		return 0



# New stuff - pawn movement excepting promotion as separate function
# Updated new stuff for pawn captures

def pawn_capture(row, column, new_row, new_column):
	x = row - new_row
	y = column - new_column
#	print "pawn capture", chess_board[new_row][new_column] in empty_space
	if chess_board[new_row][new_column] not in empty_space:
		if (x**2 == 1) and (y**2 == 1):
			return 1
		else:
#			print "nailed it"
			return 0
#		if chess_board[row][column][1] == "b":
#			if (x == 1) and (y == 1 or y == -1):
#				return 1
#			else:
#				return 0
	else:
		return 0

def pawn_move_valid():
	"""Check pawn's move is valid"""
	y = new_row
	global x, each, super_x, pawn, valid_move, other_y
	other_y = new_column - column
	valid_move = True
	pawn = ""
	super_x = 0
	x = 0
	while super_x == 0:
		for each in range(len(pawn_moves)):
			# iterate through pawn_moves to find the piece in question
			if pawn_moves[each][0] == chess_board[row][column][1:4]:
				# assign iteration to a fixed variable to call later
				super_x = each
				if pawn_moves[each][0][0] == "w":
					# white moves
					x = int(move2[1]) - int(move1[1])
				elif pawn_moves[each][0][0] == "b":
					# black moves
					x = int(move1[1]) - int(move2[1])
				break
		break
#	print other_y
	if other_y == 0:
	
		if ((x == 1 or x == 2) and pawn_moves[each][2] == 0):
			pawn_moves[each][1] = y
			pawn_moves[each][2] += 1
		elif x == 1 and pawn_moves[each][2] != 0:
			pawn_moves[each][1] = y
			pawn_moves[each][2] += 1
		else:
			pawn = "invalid"
	else:
		pawn = "invalid"
#	print other_y, pawn_capture(row, column, new_row, new_column)
#	
	if other_y != 0:
		if pawn_capture(row, column, new_row, new_column) == 1:
			pawn_moves[each][1] = y
			pawn_moves[each][2] += 1
			pawn = ""
		else:
			pawn = "invalid"
	
	if pawn == "":
		if x == 1:
			valid_move = True
		elif x == 2:
			valid_move = True
	else:
		print "Pawns can't move like that =( "
		valid_move = False
	
	if valid_move is True:
		return 1
	else:
		return 0


def redraw_valid_for_pawns(valid_move):
	"""Special function for pawn movement""" 
	#Bug report:
	# Black move a7-a(x) causes a crash
	# FIXED: No it doesn't
	if chess_board[row][column][1] != (turn[0]).lower():
		return 0
	global pawn, x, super_x, other_y
	if collision_detection(row, column, new_row, new_column) == 1:
		if valid_move is True:
			if pawn == "":
				if x == 1 and other_y == 0:
					if chess_board[row][column][0] == "{":
						pawn = "(" + pawn_moves[super_x][0] + ")"
						chess_board[row][column] = "{___}"
					elif chess_board[row][column][0] == "(":
						pawn = "{" + pawn_moves[super_x][0] + "}"
						chess_board[row][column] = "(   )"
				elif x == 2 and other_y == 0:
					if chess_board[row][column][0] == "{":
						pawn = "{" + pawn_moves[super_x][0] + "}"
						chess_board[row][column] = "{___}"
					elif chess_board[row][column][0] == "(":
						pawn = "(" + pawn_moves[super_x][0] + ")"
						chess_board[row][column] = "(   )"
				else:
					pawn_front = chess_board[new_row][new_column][0]
					pawn_back = chess_board[new_row][new_column][4]
					pawn_middle = pawn_moves[super_x][0]
					pawn = pawn_front + pawn_middle + pawn_back
					if chess_board[row][column][0] == "(":
						chess_board[row][column] = "(   )"
					else:
						chess_board[row][column] = "{___}"
		chess_board[new_row][new_column] = pawn


# Castling rules complete apart from collision detection and not castling
# out of, through, or into check. It seemed like a good idea to do everything
# for castling in one function, rather than passing god knows what to god knows
# which other functions

def castling(move):
	"""Very sloppily completes all aspects of castling"""
	global king, turn, white_king_moved, black_king_moved
	global wR1_moved, wR2_moved, bR1_moved, bR2_moved
	if move == "o-o":
		if (turn[0]).lower() == "w":
			if white_king_moved == True or wR2_moved == True:
				print "Your king and/or rook has moved!"
				return 0
			elif white_king_moved == False and wR2_moved == False:
				white_king_moved = True
				wR2_moved = True
				chess_board[7][8] = "(   )" 
				king =  "{wK }"
				chess_board[7][7] = king 
				rook = "(wR2)"
				chess_board[7][6] = rook
				chess_board[7][5] = "{___}"
		else:
			if black_king_moved == True or bR2_moved == True:
				print "Your king and/or rook has moved!"
				return 0
			else:
				black_king_moved = True
				bR2_moved = True
				chess_board[0][8] = "{___}"
				king = "(bK )"
				chess_board[0][7] = king
				rook = "{bR2}"
				chess_board[0][6] = rook
				chess_board[0][5] = "(   )"

	elif move == "o-o-o":
		if (turn[0]).lower() == "w":
			if white_king_moved == True or wR1_moved == True:
				print "Your king and/or rook has moved"
				return 0
			elif white_king_moved == False and wR1_moved == False:
				white_king_moved = True
				wR1_moved = True
				chess_board[7][1] = "{___}"
				king = "{wK }"
				chess_board[7][3] = king
				rook = "(wR1)"
				chess_board[7][4] = rook
				chess_board[7][5] = "{___}"
		else:
			if black_king_moved == True or bR1_moved == True:
				print "Your king and/or rook has moved!"
				return 0
			else:
				black_king_moved = True
				bR1_moved = True
				chess_board[0][1] = "(   )"
				king = "(bK )"
				chess_board[0][3] = king
				rook = "{bR1}"
				chess_board[0][4] = rook
				chess_board[0][5] = "(   )"
	drawBoard.print_board()
#	pass
	

def collision_detection(row, column, new_row, new_column):
	"""Checks that all spaces between start and finish pos are blank"""
	if chess_board[row][column][2] != "N":
		x = row - new_row
		y = column - new_column
#		print x, y
		if x < 0:
			range1 = range(x, 0)
			range1.reverse()
		else:
			range1 = range(1,x+1)
		if y < 0:
			range2 = range(y, 0)
			range2.reverse()
#				range2.sort()
		else:
			range2 = range(1,y+1)
		counter2 = 0
#		print range1, range2
		
		if x == 0:
			"""Deals with straightforward left and right movements"""
			while counter2 != len(range2):
				list_index = (int((range2[counter2]**2)**0.5) - 1)
#				print list_index, range2, column, range2[list_index]
				# returns a value of one on a single (0) length list;
				# outside of list range. Corrects for this
				if y < 0:
					list_index -= 1
				empty_check = chess_board[row][column-(range2[list_index])]
				if list_index > 0:
#					print empty_check
					if empty_check in empty_space:
						pass
					else:
#						print empty_check
#						print "hit it"
						return 0
				# not very pretty: corrects for disparity in list lengths
				# by forcing first evaluation to read position 0 in the
				# relevant list, instead of position 1
				if y < 0 and list_index == 0:
					if chess_board[row][column-(range1[0])][1] == " " or chess_board[row][column-(range1[0])][1] == "_":
						pass
					else:
#						print empty_check
#						print "hit it hack x"
						return 0
				if counter2+1 == len(range1):
					if chess_board[new_row][new_column][1] == chess_board[row][column][1]:
						print "You can't take your own pieces"
						return 0
					else:
						if chess_board[new_row][new_column][1] != chess_board[row][column][1] and chess_board[new_row][new_column][2] != "K":
							return 1

				counter2 += 1
				
		# need to include something for minus numbers
		
		
		if y == 0:
			"""Deals with straightforward up and down moves"""
			while counter2 != len(range1):
				list_index = (int((range1[counter2]**2)**0.5)-1)
#				print list_index, range1
				# returns a value of one on a single (0) length list;
				# outside of list range. Corrects for this
				if x < 0:
					list_index -= 1

				empty_check = chess_board[row-(range1[list_index])][column]
				if list_index > 0:
#					print empty_check
					if empty_check in empty_space:
						pass
					else:
#						print "hit it 2"
						return 0

				# not very pretty: corrects for disparity in list lengths
				# by forcing first evaluation to read position 0 in the
				# relevant list, instead of position 1
				if x < 0 and list_index == 0:
					if chess_board[row-(range1[0])][column][1] == " " or chess_board[row-(range1[0])][column][1] == "_":
						pass
					else:
#						print "hit it hack"
						return 0 

				if counter2+1 == len(range1):
					if chess_board[new_row][new_column][1] == chess_board[row][column][1]:
						print "You can't take your own pieces"
						return 0
					else:
						if chess_board[new_row][new_column][1] != chess_board[row][column][1] and chess_board[new_row][new_column][2] != "K":
							return 1

				counter2 += 1

		counter2 = 0
		if (x**2) == (y**2):
			"""Deals with diagonal moves"""
			while counter2+1 < len(range1):
				list_index1 = int(((range1[counter2])**2)**0.5)
				list_index2 = int(((range2[counter2])**2)**0.5)

						
#				print list_index1, list_index2
				if counter2 == 0:
					list_index1 = 0
					list_index2 = 0
				empty_check = chess_board[row-(range1[list_index1])][column-(range2[list_index2])]
#				print empty_check
#				if list_index1 > 0 and list_index2 > 0:
				if empty_check in empty_space:
					pass
				else:
#					print empty_check
#					print "hit it"
					return 0
				
				if counter2+1 == len(range1) or counter2+1 == len(range2):
					if chess_board[new_row][new_column][1] == chess_board[row][column][1]:
						print "You can't take your own pieces"
						return 0
					else:
						if chess_board[new_row][new_column][1] != chess_board[row][column][1] and chess_board[new_row][new_column][2] != "K":
							return 1
				
				counter2 += 1
				
			
		"""Checks that last position is of different colour and allows capture"""	
		if counter2+1 == len(range1) or counter2+1 == len(range2):
			if chess_board[new_row][new_column][1] == chess_board[row][column][1]:
#				print "hit it 4"
				print "You can't take your own pieces"
				return 0
			else:
				# cannot capture kings
				if chess_board[new_row][new_column][2] != "K":
					return 1
				else:
					return 0
	# evaluates knight moves and ensures that you are not taking your
	# own pieces or a King
	else:
		if chess_board[new_row][new_column][1] == chess_board[row][column][1]:
			return 0
		else:
			if chess_board[new_row][new_column][2] == "K":
				return 0
			else:
				return 1



def check_for_check():
	"""Woo. Code here"""
	localCheck = None
	check_row = 0
	check_column = 0
	king_found = False
	kingFound = checkCheck.find_king()
	print kingFound
	check_list = ["w", "b"]
	# check whose turn it is to look for check on that turn
	for colours in check_list:
		localCheck = None
		if colours == "w":
			localCheck = white_king_check
			piece_turn = "White's "
			print "hello"
		else:
			localCheck = black_king_check
			piece_turn = "Black's "
			print "world"
		check_row, check_column = kingFound
		
		print colours, piece_turn
	
		localCheck = checkCheck.check_h()
		
		if localCheck == False:
			localCheck = checkCheck.check_v()
	
		if localCheck == False:
			localCheck = checkCheck.check_d()
		
		if localCheck == False:
			localCheck = checkCheck.check_k()

		print localCheck

		if localCheck == True:
			print piece_turn + "is in Check"

drawBoard = DrawBoard(valid_move)
turn_spec = GameMechanics(turn_counter)


while quit_game == False:
	# print board for the first time
	drawBoard.print_board()
	# assume input will be a valid move
	real_move = True
	# lazy code. Seriously
	onwards = False
	# check whose turn it is
	turn = turn_spec.turn_picker(turn_counter)
	# apparently this is causing problems so...
	valid_move = True
	# take a starting piece and where to move it to
	# also checks that player does not wish to quit
	move1 = raw_input(turn + " turn. Pick which piece to move: ")
	if move1 in ("q","Q"):
		quit_game = True
		break
	else:
		move2 = raw_input("Where would you like to move to: ")
		if move2 in ("q","Q"):
			quit_game = True
			break

	# Below prompt for castling
	if move1 == "o-o" or move1 == "o-o-o":
		castling(move1)
		castling_attempt = True
		real_move = False
		onwards = False
	# Exception handler for non-valid moves
	while real_move == True:
		try:
			chess_moves_col[move1[0]] != ""
			chess_moves_row[move1[1]] != ""
			len(move1) == 2
			len(move2) == 2
			move1[0] in chess_moves_col
			move2[0] in chess_moves_col
			move1[1] in range(9)
			move2[1] in range(9)
		except (IndexError, KeyError):
			print "Not a valid move"
			real_move = False
			turn_counter -= 1
			break
		else:
			onwards = True
		break


	if onwards == True:
	# assign move a value to check against relevant dictionary
		column = chess_moves_col[move1[0]]
		row = chess_moves_row[move1[1]]
	
	# check that move (not move input) is valid

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
		if collision_detection(row, column, new_row, new_column) == 1:
			pass
		else:
			print "There seems to be a piece in the way..."
			turn_counter -= 1
			valid_move = False
		piece_colour = turn[0].lower()
	# check that player has picked their own piece
		if valid_move != False:
			if chess_board[row][column][1] != (turn[0]).lower():
				print "That's not your piece! Try again!"
				turn_counter -= 1
	# check that piece can move in that manner, piece by piece
	# if so, redraw board with piece at its new location
#			pawn_move_checking = PawnMovement(piece_colour)
			else:
				if chess_board[row][column][2] == "P" and (new_row == 0 or new_row == 8):
#				if pawn_promotion(piece_colour) == 1:
						if pawn_move_valid() == 1:
							pawn = pawn_promotion(piece_colour)
							chess_board[new_row][new_column] = pawn
							if chess_board[row][column][0] == "{":
								chess_board[row][column] = "{___}"
							else:
								chess_board[row][column] = "(   )" 

							print "\nPawn promoted!\n"
#				if drawBoard.redraw_valid(valid_move) == 0:
#					pass

#					chess_board[new_row][new_column] = pawn
				elif chess_board[row][column][2] == "P":
					if pawn_move_valid() != 1:
						turn_counter -= 1
				elif chess_board[row][column][2] == "N":
					if knight_move(piece_colour) == 1:
						chess_board[new_row][new_column] = knight
#					drawBoard.redraw_valid(valid_move)
					else:
						turn_counter -= 1
				elif chess_board[row][column][2] == "B":
					if bishop_move(piece_colour) == 1:
						chess_board[new_row][new_column] = bishop
#					drawBoard.redraw_valid(valid_move)
					else:
						turn_counter -=1
				elif chess_board[row][column][2] == "R":
					if rook_move(piece_colour) == 1:
						chess_board[new_row][new_column] = rook
#					drawBoard.redraw_valid(valid_move)
					else:
						turn_counter -=1
				elif chess_board[row][column][2] == "Q":
					if queen_move(piece_colour) == 1:
						chess_board[new_row][new_column] = queen
					else:
						turn_counter -=1
				elif chess_board[row][column][2] == "K":
					if king_move(piece_colour) == 1:
						chess_board[new_row][new_column] = king
#					drawBoard.redraw_valid(valid_move)
					else:
						turn_counter -=1
			drawBoard.redraw_valid(valid_move)
		onwards = False
	# change player
	turn_counter += 1
	check_for_check()
