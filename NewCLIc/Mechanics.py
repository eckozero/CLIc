class DrawBoard(object):
    def __init__(self, chess_board, valid_move):
        self.chess_board = chess_board
	self.valid_move = valid_move

    def print_board(self):
        """Prints the chess board as it is"""
        for i in range(len(self.chess_board)):
            print "".join(self.chess_board[i])





class CheckForCheck(object):
    def __init__(self, white_king_check, black_king_check, piece_colour):
        self.white_king_check = white_king_check
        self.black_king_check = black_king_check
        self.piece_colour = piece_colour

    def find_king():
        pass

    def check_horizontal(self):
#        print "H"
        pass
    def check_vertical(self):
#        print "V"
        pass
    def check_diagonal(self):
#        print "D"
        pass
    def checkmate(self):
#        print "checkmate"
        pass
    def check_for_check(self):
        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        self.checkmate()


class PawnMovement(object):
    def __init__(self):
        pass

    def pawn_move(self):
        pass

    def pawn_promotion(self):
        pass



class PieceMovement(object):
    def __init__(self):
        pass

    def king_move(self):
        pass

    def queen_move(self):
        pass

    def bishop_move(self):
        pass

    def knight_move(self):
        pass

    def rook_move(self):
        pass


class Castling(object):
    def __init__(self):
        pass


class Gameplay(object):
    def __init__(self):
        pass

    def collision_detection(self):
        return 0

    def do_not_proceed(self,turn_counter, valid_move):
        """You shall not pass!"""
        turn_counter -=1
        valid_move = False
        return turn_counter, valid_move

    def move_valid(self, chess_board, row, column, move2, valid_move):
        if (column in range(1,9)) and (row in range(0,8)):
            new_column = chess_moves_col[move2[0]]
            new_row = chess_moves_row[move2[1]]
        else:
            print "\nThat's not a valid move. Try again\n"
            self.do_not_proceed()
        
        if chess_board[row][column][1] == " ":
            print "\nThat's not a valid move. Try again\n"
            self.do_not_proceed()

        if self.collision_detection() == 1:
            print "There seems to be a piece in the way"
            self.do_not_proceed()

        if chess_board[row][column][1] != turn[0].lower():
            print "That's not your piece. Try again"
            self.do_not_proceed()

        valid_move = True

        
    def end_game(self):
        print "Quitting"
        exit()
