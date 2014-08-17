class DrawBoard(object):
    def __init__(self):
        #self.chess_board = chess_board
	#self.valid_move = valid_move
        pass

    def print_board(self, chess_board):
        """Prints the chess board as it is"""
        for i in range(len(chess_board)):
            print "".join(chess_board[i])





class CheckForCheck(object):
    """Currently requires the following arguments:
    white_king_check, black_king_check, piece_colour
    In order to keep all classes blank in main file,
    have removed from __init__ and will be added as
    args to functions"""

    def __init__(self):
        pass

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
    def checkmate(self, turn):
        print turn + " wins!"
        quitting = raw_input("Press any key to quit")
        exit()

    def check_for_check(self, turn):
        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        self.checkmate(turn)


class PawnMovement(object):
    def __init__(self):
        pass

    def pawn_move(self):
        pass

    def pawn_capture(self):
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

    def turn_picker(self, turn_counter, valid_move):
        if turn_counter % 2 == 0:
            turn = "White's"
        else:
            turn = "Black's"
        return turn, valid_move


    def move_selection(self, turn):
        move1 = raw_input(turn + " turn. Pick which piece to move: ")
        if len(move1) == 0:
            move1 = "zz"
        if move1[0].lower() == "q":
            rules.end_game()
        else:
            move2 = raw_input("Where would you like to move to: ")
            if len(move2) == 0:
                move2 = "zz"
                if move2[0].lower() == "q":
                    rules.end_game()
    
        if move1 == "o-o" or move1 == "o-o-o":
            pass


        if move1 == "zz" or move2 == "zz":
            pass

        return move1, move2


    def collision_detection(self):
        return 0

    def do_not_proceed(self,turn_counter, valid_move):
        """You shall not pass!"""

        print "Not a valid move"

        turn_counter -=1

        self.turn_picker(turn_counter)



    def move_valid(self, chess_board, row, column, valid_move, turn):
        """Check that the proposed move is a valid chess move"""

        # If I make most of these functions evaluate for false,
        # rather than true, I should be able to streamline

        if (column in range(1,9)) and (row in range(0,8)):
            pass
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

        return valid_move

        
    def change_turn(self, valid_move, turn_counter):
        if valid_move == True:
            turn_counter +=1
            self.turn_picker(turn_counter, valid_move)
        else:
            self.do_not_proceed(turn_counter, valid_move)



    def end_game(self):
        print "Quitting"
        exit()
