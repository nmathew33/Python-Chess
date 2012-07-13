# Filename: chess.py
# Contains the main method for chess

import pygame
from pygame.locals import *
import sys
import peices

FPSCLOCK = 30
WH = 50
YELLOW = (255, 255, 0)
BROWN = (84, 24, 24)
CYAN = pygame.Color(0, 255, 255, 100)


def main():
    # global variables to be declared in main
    global DISPLAYSURF, FPSCLOCK, WH, B_SQUARE, W_SQUARE, B_PAWN, B_ROOK
    global B_KNIGHT, B_BISHOP, B_QUEEN, B_KING, W_PAWN, W_ROOK, W_KNIGHT
    global W_BISHOP, W_QUEEN, W_KING
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WH * 8, WH * 8))
    DISPLAYSURF.fill((0, 0, 0))
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

    start_game(board)
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
                peice = board[old_pos[0]][old_pos[1]]
                print peice.get_my_pos()
                need_move = False
                if (row, col) in peice.get_possible_moves(board):
                    peice.make_move(board, (row, col))
                display_board(board)
            elif board[row][col]:
                display_move_areas(board[row][col], board)
                need_move = True
                old_pos = (row, col)
            mouseClicked = False

        pygame.display.update()
        
    
def start_game(board):
    '''Instantiates the peices on the board'''
    # instantiate main black peices
    board[0][0] = peices.Rook((0, 0), 'Black')
    board[0][1] = peices.Knight((0, 1), 'Black')
    board[0][2] = peices.Bishop((0, 2), 'Black')
    board[0][3] = peices.Queen((0, 3), 'Black')
    board[0][4] = peices.King((0, 4), 'Black')
    board[0][5] = peices.Bishop((0, 5), 'Black')
    board[0][6] = peices.Knight((0, 6), 'Black')
    board[0][7] = peices.Rook((0, 7), 'Black')

    # instantiate main white peices
    board[7][0] = peices.Rook((7, 0), 'White')
    board[7][1] = peices.Knight((7, 1), 'White')
    board[7][2] = peices.Bishop((7, 2), 'White')
    board[7][3] = peices.Queen((7, 3), 'White')
    board[7][4] = peices.King((7, 4), 'White')
    board[7][5] = peices.Bishop((7, 5), 'White')
    board[7][6] = peices.Knight((7, 6), 'White')
    board[7][7] = peices.Rook((7, 7), 'White')

    # instantiate pawns
    for col in range(8):
        board[1][col] = peices.Pawn((1, col), 'Black')
        board[6][col] = peices.Pawn((6, col), 'White')
# end start_game(board)

def display_board(board):
    '''Updates the display of the board'''
    # draw the squares
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row + col) % 2 == 0:
               pygame.draw.rect(DISPLAYSURF, BROWN, (row*WH, col*WH, WH,
                                                     WH))
            else:
                pygame.draw.rect(DISPLAYSURF, YELLOW, (row*WH, col*WH, WH,
                                                      WH))

    # draw the peices
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col]:
                peice = board[row][col]
                name = peice.__str__()
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
# end display_board(board)

def get_row_col(mousex, mousey):
    '''Get a row and column in the board for mouse coordinates'''
    row = mousey // 50
    col = mousex // 50
    return (row, col)
# end get_row_col(mousex, mousey)

def display_move_areas(peice, board):
    '''Highlight areas to which the peice can move'''
    moves = peice.get_possible_moves(board)
    for move in moves:
        x = move[1]*WH
        y = move[0]*WH
        pygame.draw.rect(DISPLAYSURF, CYAN, (x, y, WH, WH))
        

main()
