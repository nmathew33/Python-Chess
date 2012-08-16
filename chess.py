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

import pygame
from pygame.locals import *
import sys
import pieces

FPSCLOCK = 30
WH = 50 # Width and Height of each square
YELLOW = (255, 255, 0) # color of 'white' squares
BROWN = (84, 24, 24) # color or 'black' squares
CYAN = pygame.Color(0, 255, 255, 150) # color for highlighting

def main():
    # global variables to be declared in main
    global DISPLAYSURF, FPSCLOCK, WH, B_SQUARE, W_SQUARE, B_PAWN, B_ROOK
    global B_KNIGHT, B_BISHOP, B_QUEEN, B_KING, W_PAWN, W_ROOK, W_KNIGHT
    global W_BISHOP, W_QUEEN, W_KING

    # pygame init stuff
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WH * 8, WH * 8))
    DISPLAYSURF.fill((0, 0, 0))

    # load the images of the pieces
    B_PAWN = pygame.image.load('black_pawn.png').convert()
    B_ROOK = pygame.image.load('black_rook.png').convert()
    B_KNIGHT = pygame.image.load('black_knight.png').convert()
    B_BISHOP = pygame.image.load('black_bishop.png').convert()
    B_QUEEN = pygame.image.load('black_queen.png').convert()
    B_KING = pygame.image.load('black_king.png').convert()
    W_PAWN = pygame.image.load('white_pawn.png').convert()
    W_ROOK = pygame.image.load('white_rook.png').convert()
    W_KNIGHT = pygame.image.load('white_knight.png').convert()
    W_BISHOP = pygame.image.load('white_bishop.png').convert()
    W_QUEEN = pygame.image.load('white_queen.png').convert()
    W_KING = pygame.image.load('white_king.png').convert()
    
    # instantiate matrix board
    board = []
    for row in range(8):
        board.append([])
        for col in range(8):
            board[row].append(None)

    # place the pieces
    start_game(board)
    # display the 
    display_board(board)
    
    mousex = 0
    mousey = 0
    row = 0
    col = 0
    mouseClicked = False
    need_move = False
    old_pos = (0, 0)
    
    pygame.display.set_caption('Chess')

    while True: # main loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        if mouseClicked:
            print 'clicked one'
            row, col = get_row_col(mousex, mousey)
            if need_move:
                print 'clicked two'
                piece = board[old_pos[0]][old_pos[1]]
                print piece.get_my_pos()
                need_move = False
                if (row, col) in moves:
                    piece.make_move(board, (row, col))
                display_board(board)
            elif board[row][col]:
                moves = display_move_areas(board[row][col], board)
                need_move = True
                old_pos = (row, col)
            mouseClicked = False

        pygame.display.update()
        
    
def start_game(board):
    '''Instantiates the pieces on the board'''
    # instantiate main black pieces
    board[0][0] = pieces.Rook((0, 0), 'Black')
    board[0][1] = pieces.Knight((0, 1), 'Black')
    board[0][2] = pieces.Bishop((0, 2), 'Black')
    board[0][3] = pieces.Queen((0, 3), 'Black')
    board[0][4] = pieces.King((0, 4), 'Black')
    board[0][5] = pieces.Bishop((0, 5), 'Black')
    board[0][6] = pieces.Knight((0, 6), 'Black')
    board[0][7] = pieces.Rook((0, 7), 'Black')

    # instantiate main white pieces
    board[7][0] = pieces.Rook((7, 0), 'White')
    board[7][1] = pieces.Knight((7, 1), 'White')
    board[7][2] = pieces.Bishop((7, 2), 'White')
    board[7][3] = pieces.Queen((7, 3), 'White')
    board[7][4] = pieces.King((7, 4), 'White')
    board[7][5] = pieces.Bishop((7, 5), 'White')
    board[7][6] = pieces.Knight((7, 6), 'White')
    board[7][7] = pieces.Rook((7, 7), 'White')

    # instantiate pawns
    for col in range(8):
        board[1][col] = pieces.Pawn((1, col), 'Black')
        board[6][col] = pieces.Pawn((6, col), 'White')
# end start_game(board)

def display_board(board):
    '''Updates the display of the board'''
    # draw the squares
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row + col) % 2 == 0:
                pygame.draw.rect(DISPLAYSURF, BROWN, (row*WH, col*WH,
                                                      WH, WH))
            else:
                pygame.draw.rect(DISPLAYSURF, YELLOW, (row*WH, col*WH,
                                                       WH, WH))

    # draw the pieces
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                piece = board[row][col]
                name = piece.__str__()
                if name == 'PawnBlack':
                    DISPLAYSURF.blit(B_PAWN, (col*WH, row*WH))
                elif name == 'RookBlack':
                    DISPLAYSURF.blit(B_ROOK, (col*WH, row*WH))
                elif name == 'KnightBlack':
                    DISPLAYSURF.blit(B_KNIGHT, (col*WH, row*WH))
                elif name == 'BishopBlack':
                    DISPLAYSURF.blit(B_BISHOP, (col*WH, row*WH))
                elif name == 'QueenBlack':
                    DISPLAYSURF.blit(B_QUEEN, (col*WH, row*WH))
                elif name == 'KingBlack':
                    DISPLAYSURF.blit(B_KING, (col*WH, row*WH))
                elif name == 'PawnWhite':
                    DISPLAYSURF.blit(W_PAWN, (col*WH, row*WH))
                elif name == 'RookWhite':
                    DISPLAYSURF.blit(W_ROOK, (col*WH, row*WH))
                elif name == 'KnightWhite':
                    DISPLAYSURF.blit(W_KNIGHT, (col*WH, row*WH))
                elif name == 'BishopWhite':
                    DISPLAYSURF.blit(W_BISHOP, (col*WH, row*WH))
                elif name == 'QueenWhite':
                    DISPLAYSURF.blit(W_QUEEN, (col*WH, row*WH))
                elif name == 'KingWhite':
                    DISPLAYSURF.blit(W_KING, (col*WH, row*WH))

def get_row_col(mousex, mousey):
    '''Get a row and column in the board for mouse coordinates'''
    row = mousey // 50
    col = mousex // 50
    return (row, col)

def display_move_areas(piece, board):
    '''Highlight areas to which the piece can move'''
    moves = piece.get_possible_moves(board)
    for move in moves:
        x = move[1]*WH
        y = move[0]*WH
        high = pygame.Surface((WH, WH)).convert_alpha()
        high.fill(CYAN)
        #pygame.draw.rect(DISPLAYSURF, CYAN, (x, y, WH, WH))
        DISPLAYSURF.blit(high, (x, y))
    return moves
        

main()
