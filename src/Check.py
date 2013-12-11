#!/usr/bin/env python

class Check(object):
	def __init__(self, white_king_check, black_king_check, piece_colour):
		self.white_king_check = white_king_check
		self.black_king_check = black_king_check
		self.piece_colour = piece_colour
	
	def find_king(self, piece_colour):
		#kingFound = False
		#while kingFound == False:
		for pieces in range(9):
			for columns in range(9):
				if chess_board[pieces][columns][2] == "K":
					if chess_board[pieces][columns][1] == piece_colour:
						# successfully found King. Assign location to
						# a variable
#						print "Test hit"
						check_row = pieces
						check_column = columns
		#				kingFound = True
#						print chess_board[check_row][check_column]
						return check_row, check_column
							
#	check_row, check_column = find_king(self, piece_colour)

	def check_h(self, piece_colour):
		"""Checks horizontal moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king(piece_colour)
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
							return local_check
						else:
							# non attacking piece in the way
							local_check = False
							return local_check
					else:
						# Your piece is blocking
						local_check = False
						return local_check
						
		
	def check_v(self, piece_colour):
		"""Checks vertical moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king(piece_colour)
		row_range1 = range(1, check_row+1)
		row_range2 = range(((8 - check_row) * -1), 0)
		row_range2.reverse()
		super_list = [row_range1, row_range2]
#		print row_range1, row_range2
		for each in super_list:
			for every in range(0, len(each)):
				check_space = chess_board[check_row - (each[every])][check_column]
#				print check_space, piece_colour, check_space[1]
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
							return local_check
						else:
							# non attacking piece is in the way
							local_check = False
							return local_check
					else:
						# Your piece is blocking
						local_check = False
						return local_check
						
		return local_check
	
	def check_d(self, piece_colour):
		"""Checks horizontal moves + and - from King pos"""
		local_check = False
		check_row, check_column = self.find_king(piece_colour)
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
								return local_check
							else:
								new_list = [[1,1],[-1,1],[-1,-1],[1,-1]]
								for each in new_list:
									pawn_check = chess_board[check_column + each[0]][check_row + each[1]]
									if pawn_check[2] == "P":
										local_check = True
										return local_check
							
								# non attacking piece is in the way
								local_check = False
								return local_check
						else:
							# your piece - no threat
							break
					else:
					# not a piece space
						break
			counter += 1	
		return local_check
		
	def check_k(self, piece_colour):
		"""Checks if King is in check from Knight"""
		local_check = False
		check_row, check_column = self.find_king(piece_colour)
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
									return local_check
							else:
						# your piece occupying Knight space
								break
				counter += 1	
		return local_check

