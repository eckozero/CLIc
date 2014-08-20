class DrawBoard(object):
    """This deals with actually displaying the chess board.

    I can't shake the feeling that I need to return the
    chess board variable from this class. If I do, then
    the chess_board variable is changed, and the new
    variable can be amended moving forward. But it seems to
    be working fine at the moment so I'm loathed to change
    it. If it ain't broke and all that... """


    def print_board(self, chess_board):
        """Prints the chess board as it is."""
        for i in range(len(chess_board)):
            print "".join(chess_board[i])


    def redraw_board(self, chess_board, row, column,
                     new_row, new_column):
        """Redraws the board once moves updated.
        
        All other methods should do the validation of
        whether or not the move is valid. This method should
        just redraw the new board."""
        # Stuff goes here to change the chess_board variable
        
        # Has the piece come from a white or black square?
        old_square_bw = chess_board[row][column][0]
        # Create variable as just the piece
        new_square_piece = chess_board[row][column][1:4]


        if chess_board[new_row][new_column][0] == "(":
            # Piece is going to white square
            redraw_square = "(" + new_square_piece + ")"
        else:
            # Piece is going to black square
            redraw_square = "{" + new_square_piece + "}"
            
        # Populate new_row/new_column with the piece that
        # was originally selected
        chess_board[new_row][new_column] = redraw_square
        
        if old_square_bw == "(":
            # Do you see what I did there? By assigning whether
            # old piece was black or white square, I created a
            # comparison to decide what the (now empty) space
            # should look like on the board
            redraw_old_piece = "(   )"
        else:
            redraw_old_piece = "{___}"

        # Make the space that the piece came from blank again
        chess_board[row][column] = redraw_old_piece
        # Redraw the board now it has been amended
        self.print_board(chess_board)


class CheckForCheck(object):
    """Runs checks for check in all directions.
    
    Currently requires the following arguments:
    white_king_check, black_king_check, piece_colour
    In order to keep all classes blank in main file,
    have removed from __init__ and will be added as
    args to functions"""

    def find_king():
        pass

    def check_horizontal(self):
        pass

    def check_vertical(self):
        pass

    def check_diagonal(self):
        pass

    def checkmate(self, turn):
        # Checkmate stuff here
        # If checkmate = True: etc
        print turn[0:5] + " wins!"
        quitting = raw_input("Press any key to quit")
        exit()

    def check_for_check(self, turn):
        self.check_horizontal()
        self.check_vertical()
        self.check_diagonal()
        self.checkmate(turn)


class PawnMovement(object):
    def pawn_move(self):
        pass

    def pawn_capture(self):
        pass

    def pawn_promotion(self):
        pass



class PieceMovement(object):

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
    def __init__(self, chess_board):
        self.chess_board = chess_board

    def castling(self, move, *args):
        """Deals with castling (obviously).

        I hate castling right now. """

        args_list = args[0]
        turn = args_list[0][0]
        turn_counter = args_list[9]

        in_check_list = args_list[7:9]

        chess_board = self.chess_board


        if turn == "W":
            in_check = in_check_list[0]
            king_moved = args_list[1]
            rooks_moved = args_list[2:4]
            king_row = 7
        else:
            in_check = in_check_list[1]
            king_moved = args_list[2]
            rooks_moved = args_list[4:6]
            king_row = 0
        # Needs castling code here

        if move == "o-o":
            # Kingside rook (R2)
            rook_moved = rooks_moved[1]
        else:
            # Queenside rook (R1)
            rook_moved = rooks_moved[0]

        for each in (in_check, rook_moved):
            if each == True:
                print ("Not a legal castling move, " +
                       "you can't castle into, out of or through " + 
                       "check or if your king or castle has moved")
                valid_move = False
                Gameplay().do_not_proceed(valid_move, turn_counter)
                break

        # King not in check and relevant rook not moved
        # Are there pieces between King and Rook?

        self.castling_collision(chess_board, turn, move, king_row)

        if move == "o-o":
            # Kingside
            if chess_board[king_row][8][1:4] != (turn.lower() + "R2"):
                return 0
            else:
                # TODO: Castling logic
                pass
        if move == "o-o-o":
            # Queenside
            if chess_board[king_row][1][1:4] != (turn.lower() + "R1"):
                # TODO: Castling logic
                pass


    def castling_collision(self, chess_board, turn, move, king_row):
        """Determines if pieces between King and Rook."""

        EMPTY_SPACE = ("(   )", "{___}")

        if move == "o-o":
            collision_range = range(6,8)
            rook_space = 8
            dest_space_k = 7
            dest_space_r = 6

        else:
            collision_range = range(2,5)
            rook_space = 1
            dest_space_k = 3
            dest_space_r = 4

        # Store whether King/Rook squares are Black or White
        # Left and right side of square
        b_w_square_k_l = chess_board[king_row][5][0]
        b_w_square_k_r = chess_board[king_row][5][4]

        b_w_square_r = chess_board[king_row][rook_space][0]
        b_w_square_l = chess_board[king_row][rook_space][4]

        king = chess_board[king_row][5]
        rook = chess_board[king_row][rook_space]

        for each in range(6, 8):
            if chess_board[king_row][each] not in EMPTY_SPACE:
                # Can't castle though check
                # Should be a method for checking this
                if CheckForCheck().check_for_check(turn) == 1:
                    print ("Not a legal castling move, " +
                       "you can't castle into, out of or through " + 
                       "check or if your king or castle has moved")
                    return 0
                # Pieces in the way
                print "There are pieces in the way"
                pass
                #return 0

        if chess_board[king_row][rook_space][0] == "(":
            chess_board[king_row][rook_space] = "(   )"
            chess_board[king_row][5] = "{___}"
        else:
            chess_board[king_row][rook_space] = "{___}"
            chess_board[king_row][5] = "(   )"

        chess_board[king_row][dest_space_k] = king        
        chess_board[king_row][dest_space_r] = rook

        DrawBoard().print_board(chess_board)        


    def through_check(self):
        """Checks that king is not moving through check."""
        pass



class Gameplay(object):

    def turn_picker(self, turn_counter, valid_move):
        if turn_counter % 2 == 0:
            turn = "White's"
        else:
            turn = "Black's"
        return turn, valid_move, turn_counter


    def move_selection(self, chess_board, turn, args):
        castling_moves = ["o-o", "o-o-o"]
        move1 = raw_input(turn + " turn. Pick which piece to move: ")
        if len(move1) == 0:
            move1 = "zz"
        if move1[0].lower() == "q":
            self.end_game()
        else:
            move2 = raw_input("Where would you like to move to: ")
            if len(move2) == 0 and move1 not in castling_moves:
                move2 = "zz"
                if move2[0].lower() == "q":
                    self.end_game()

        if move1 == "o-o" or move1 == "o-o-o":
            Castling(chess_board).castling(move1, args)
            # Needs real code below here
            pass

        return move1, move2


    def collision_detection(self):
        return 0


    def do_not_proceed(self,turn_counter, valid_move):
        """You shall not pass!"""

        print "That's not a valid move\n"

        turn_counter -=1
        
        return self.turn_picker(turn_counter, valid_move)



    def move_valid(self, chess_board, row, column, valid_move, turn, turn_counter):
        """Check that the proposed move is a valid chess move."""
        if chess_board[row][column][1] != turn[0].lower():
            return self.change_turn(valid_move, turn_counter, turn)
        elif self.collision_detection() == 0:
            pass
        else:
            return self.change_turn(valid_move, turn_counter, turn)

        # Method for piece moves are in another class so I  can call
        # the methods from PieceMovement like ClassName().methodName()

        # This data wont be here for too much longer as it gets 
        # replaced by method calls for piece movement
        valid_move = True
        return self.change_turn(valid_move, turn_counter, turn)

        
    def change_turn(self, valid_move, turn_counter, turn):
        # Always add 1, do_not_proceed() will remove if
        # required
        turn_counter +=1
        if valid_move == True:
            return self.turn_picker(turn_counter, valid_move)
        else:
            return self.do_not_proceed(turn_counter, valid_move)



    def end_game(self):
        print "Quitting"
        exit()
