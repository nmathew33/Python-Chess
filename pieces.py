# Copyright 2012 Nixon Thekkethil
#
# This file is part of Python Chess.
#
# Python Chess is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Python Chess is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Python Chess.  If not, see <http://www.gnu.org/licenses/>.

######## Begin class ChessPiece ########
class ChessPiece(object):
    """Superclass for all chess pieces"""

    my_pos = ()
    was_enemy = False
    
    def __init__(self, position, color):
        """
        position must be a tuple in the format (row, col)
        color must be a String that is either 'White' or 'Black'
        """
        self.my_pos = position
        self.color = color

    def get_my_pos(self):
        return self.my_pos

    def get_color(self):
        return self.color

    def make_move(self, board, move):
        """
        board must be a 8*8 matrix.
        move must be a tuple in the format (row, column)
        """
        board[move[0]][move[1]] = self
        board[self.my_pos[0]][self.my_pos[1]] = None
        self.my_pos = move
        if self.my_pos == move:
            print 'changed'
        

    def in_bounds(self, board, new_pos):
        """
        board must be a matrix containing the chess pieces.
        new_pos must be the position that needs to be checked.
        Returns a boolean value
        """
        # if the previous area was an enemy, we can no longer advance
        if self.was_enemy:
            self.was_enemy = False
            return False
        
        if new_pos[0] < 0 or new_pos[1] < 0:
            return False
        try:
            item = board[new_pos[0]][new_pos[1]]
            if item == None:
                return True
            elif item.get_color() == self.get_color():
                return False
            elif item.get_color() != self.get_color:
                self.was_enemy = True
                return True
            else:
                return True
        except:
            return False
    
    def __str__(self):
        return self.color
######## End of class ChessPiece ########

######## Begin class Pawn ########
class Pawn(ChessPiece):
    """Class for pawns"""

    is_first_move = True
    color = ''
    
    def __init__(self, position, color):
        """
        Color must be a string either 'Black' or 'White.
        Position must be a tuple in the format (row, col)
        """
        super(Pawn, self).__init__(position, color)
        self.color = color
        self.pos = position

    def get_possible_moves(self, board):
        """
        board must be a matrix with the pieces in it.
        Returns a list of tuples in the format (row, column) for the
        possible moves.
        """
        moves = []
        my_pos = super(Pawn, self).get_my_pos()
        if self.color == 'White':
            if self.is_first_move:
                self.is_first_move = False
                new_pos = (my_pos[0]-2, my_pos[1])
                if super(Pawn, self).in_bounds(board, new_pos):
                    moves.append(new_pos)            
            new_pos = (my_pos[0]-1, my_pos[1])
            if super(Pawn, self).in_bounds(board, new_pos):
                moves.append(new_pos)

        else:
            if self.is_first_move:
                self.is_first_move = False
                new_pos = (my_pos[0]+2, my_pos[1])
                if super(Pawn, self).in_bounds(board, new_pos):
                    moves.append(new_pos)
            new_pos = (my_pos[0]+1, my_pos[1])
            if super(Pawn, self).in_bounds(board, new_pos):
                moves.append(new_pos)

        return moves

    def __str__(self):
        return 'Pawn' + super(Pawn, self).__str__()
######## End class Pawn ########

######## Begin class Rook ########
class Rook(ChessPiece):
    """Class for Rook."""

    def __init__(self, position, color):
        super(Rook, self).__init__(position, color)

    def get_possible_moves(self, board):
        moves = []
        forward = True
        back = True
        left = True
        right = True
        my_pos = super(Rook, self).get_my_pos()

        while forward:
            next_pos = (my_pos[0]-1, my_pos[1])
            if super(Rook, self).in_bounds(board, next_pos):
                moves.append(next_pos)
#                if super(Rook, self).is_enemy(board, next_pos):
#                    forward = False
                my_pos = next_pos
            else:
                forward = False
                my_pos = super(Rook, self).get_my_pos()

        my_pos = super(Rook, self).get_my_pos()
        while back:
            next_pos = (my_pos[0]+1, my_pos[1])
            if super(Rook, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                back = False
                my_pos = super(Rook, self).get_my_pos()

        my_pos = super(Rook, self).get_my_pos()
        while left:
            next_pos = (my_pos[0], my_pos[1]-1)
            if super(Rook, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left = False
                my_pos = super(Rook, self).get_my_pos()

        my_pos = super(Rook, self).get_my_pos()
        while right:
            next_pos = (my_pos[0], my_pos[1]+1)
            if super(Rook, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right = False
                my_pos = super(Rook, self).get_my_pos()

        return moves

    def __str__(self):
        return 'Rook' + super(Rook, self).get_color()
######## End class Rook ########

######## Begin class Knight ########    
class Knight(ChessPiece):
    """Class for Knights"""

    def __init__(self, position, color):
        """
        Color must be a string thats either 'Black or White'
        Position must be tuple in the format (row, col)
        """
        super(Knight, self).__init__(position, color)

    def get_possible_moves(self, board):
        """
        board must be a matrix with the pieces in it.
        Returns a list of tuples in the format (row, column) for the
        possible moves.
        """
        moves = []
        my_pos = super(Knight, self).get_my_pos()
        # for loop to find all move combinations
        for i in range(-2, 3, 1):
            for j in range(-2, 3, 1):
                if (abs(i) == 1 and abs(j) == 2) or (abs(i) == 2 and
                                                     abs(j) == 1):
                    new_pos = (my_pos[0]+i, my_pos[1]+j)
                    if super(Knight, self).in_bounds(board, new_pos):
                        moves.append(new_pos)
        return moves

    def __str__(self):
        return 'Knight' + super(Knight, self).__str__()
######## End class Knight ########

######## Begin class Bishop ########
class Bishop(ChessPiece):

    def __init__(self, position, color):
        super(Bishop, self).__init__(position, color)

    def get_possible_moves(self, board):
        moves = []
        my_pos = super(Bishop, self).get_my_pos()
        left_up = True
        left_down = True
        right_up = True
        right_down = True

        while left_up:
            next_pos = (my_pos[0]-1, my_pos[1]-1)
            if super(Bishop, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left_up = False
                my_pos = super(Bishop, self).get_my_pos()

        while left_down:
            next_pos = (my_pos[0]-1, my_pos[1]+1)
            if super(Bishop, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left_down = False
                my_pos = super(Bishop, self).get_my_pos()

        while right_up:
            next_pos = (my_pos[0]+1, my_pos[1]-1)
            if super(Bishop, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right_up = False
                my_pos = super(Bishop, self).get_my_pos()

        while right_down:
            next_pos = (my_pos[0]+1, my_pos[1]+1)
            if super(Bishop, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right_down = False
                my_pos = super(Bishop, self).get_my_pos()
                
        return moves

    def __str__(self):
        return 'Bishop' + super(Bishop, self).__str__()
######## End class Bishop ########
    
######## Begin class Queen ########
class Queen(ChessPiece):

    def __init__(self, position, color):
        super(Queen, self).__init__(position, color)

    def get_possible_moves(self, board):
        moves = []
        my_pos = super(Queen, self).get_my_pos()
        left_up = True
        left_down = True
        right_up = True
        right_down = True
        forward = True
        back = True
        left = True
        right = True
        
        # diagonal moves
        while left_up:
            next_pos = (my_pos[0]-1, my_pos[1]-1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left_up = False
                my_pos = super(Queen, self).get_my_pos()

        while left_down:
            next_pos = (my_pos[0]-1, my_pos[1]+1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left_down = False
                my_pos = super(Queen, self).get_my_pos()

        while right_up:
            next_pos = (my_pos[0]+1, my_pos[1]-1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right_up = False
                my_pos = super(Queen, self).get_my_pos()

        while right_down:
            next_pos = (my_pos[0]+1, my_pos[1]+1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right_down = False
                my_pos = super(Queen, self).get_my_pos()

        # vertical and horizontal lines
        while forward:
            next_pos = (my_pos[0]-1, my_pos[1])
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                forward = False
                my_pos = super(Queen, self).get_my_pos()

        while back:
            next_pos = (my_pos[0]+1, my_pos[1])
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                back = False
                my_pos = super(Queen, self).get_my_pos()

        while left:
            next_pos = (my_pos[0], my_pos[1]-1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                left = False
                my_pos = super(Queen, self).get_my_pos()

        while right:
            next_pos = (my_pos[0], my_pos[1]+1)
            if super(Queen, self).in_bounds(board, next_pos):
                moves.append(next_pos)
                my_pos = next_pos
            else:
                right = False
                my_pos = super(Queen, self).get_my_pos()
        
        return moves

    def __str__(self):
        return 'Queen' + super(Queen, self).__str__()
######## End class Queen ########
    
######## Begin King class ########
class King(ChessPiece):
    """Class for the King"""

    def __init__(self, position, color):
        super(King, self).__init__(position, color)

    def get_possible_moves(self, board):
        moves = []
        my_pos = super(King, self).get_my_pos()
        for r in range(-1, 2):
            for c in range(-1, 2):
                new_pos = (my_pos[0]+r, my_pos[1]+c)
                if super(King, self).in_bounds(board, new_pos):
                    moves.append(new_pos)
        print moves
        return moves

    def __str__(self):
        return 'King' + super(King, self).__str__()
######## End class King ########

######## Begin main ########
def test():
    """ Test the pieces class """
    board = []
    for row in range(8):
        board.append([])
        for col in range(8):
            board[row].append(None)

    #test = Pawn((6, 0), 'White')
    test = Rook((7, 1), 'White')
    #board[6][0] = test
    board[7][1] = test
    moves = test.get_possible_moves(board)
    for move in moves:
        board[move[0]][move[1]] = Knight(move, 'White')

    print_board(board)

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print str(board[i][j]) + '\t\t',
        print ''
    
######## End main ########
