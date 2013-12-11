#!/usr/bin/env python

class DrawBoard(object):
        def __init__(self, valid_move):
                self.valid_move = valid_move
        
        def printy(self):
			print "This works"
#			print self.chess_board
        
        
        def print_board(self):
                """Prints chess board"""
                chess_board = self.chess_board
                counter1 = 0
                for i in range(len(chess_board)):
				#for i in chess_dim:
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
#                                if pawn_capture(row, column, new_row, new_column) == 0:
                                        redraw_valid_for_pawns(valid_move)
                                else:
                                        old_piece = chess_board[row][column][0] 
                                        new_piece = chess_board[row][column][1:4] 
                                        redraw_piece = chess_board[new_row][new_column][0]
                                        if redraw_piece == "{": 
                                                chess_board[new_row][new_column] = "{" + new_piece + "}"
                                        
                                        else:
                                                chess_board[new_row][new_column] = "(" + new_piece + ")"
                                        if old_piece == "{": 
                                                chess_board[row][column] = "{___}" 
                                        else:
                                                chess_board[row][column] = "(   )"

