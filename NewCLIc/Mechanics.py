class DrawBoard(object):
    def __init__(self, chess_board, valid_move):
        self.chess_board = chess_board
	self.valid_move = valid_move

    def print_board(self):
        """Prints the chess board as it is"""
        for i in range(len(self.chess_board)):
            print "".join(self.chess_board[i])





class CheckForCheck(object):
    def __init__(self):
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
