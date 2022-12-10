#!/usr/bin/env python3
import time
from random import Random
from dPlayer import HumanPlayer
from tkinter import font, Tk, constants, Canvas, IntVar
from tkinter.ttk import *
from display import *

# Our visualization tool of the minimax algorithm through a game of Tic Tac Toe
#  is an extension of the CLI Tic Tac Toe game found here: https://www.youtube.com/watch?v=8ext9G7xspg

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # List of 9 variables to create 3x3 board
        self.current_winner = None # keep track of winner

    # prints self.board in a grid in CLI
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')

    @staticmethod
    # prints a board of sequential numbers
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    # returns available moves in self.board
    def available_moves(self):
        return [i for (i,spot) in enumerate(self.board) if spot == ' ']
    
    # returns Boolean if there are still empty squares in board
    def empty_squares(self):
        return ' ' in self.board
    
    # returns number of empty squares in board
    def num_empty_squares(self):
        return self.board.count(' ')

    # Returns true if valid move has been made else return false
    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # Check if there's a winner after move has been made.
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    # Returns True if function has a winner
    def winner(self,square,letter):
        # Checking row
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True

        # Checking column
        col_ind = square%3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot==letter for spot in col]):
            return True
        
        # Checking diagonal
        if square%2==0:
            diag4 = [self.board[i] for i in [0,4,8]]
            diag2 = [self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diag4]) or all([spot==letter for spot in diag2]):
                return True

        return False

# main function
def play(game,x_player,o_player,print_game=True):

    # returns the winner of the game or returns None (tie)
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter

    while game.empty_squares():
        # Get the move from the correct player
        if letter == 'O':
            funcMainBoard(tkWindow,style,game.board,o_player).grid(row = 0, column = 0)
            square = o_player.get_move(game)
        else:
            funcMainBoard(tkWindow,style,game.board,x_player).grid(row = 0, column = 0)
            square = x_player.get_move(game)
        
        # function to make a move
        if game.make_move(square,letter):
            if print_game:
                print("\n"+letter + f' makes a move to square {square}')
                game.print_board()
                print('')
        
        # Check if theres a current winner
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
                funcMainBoard(tkWindow,style,game.board,x_player).grid(row = 0, column = 0)
                funcVictoryLabel(tkWindow,style,letter).grid(row = 1, column = 0)
                tkWindow.update_idletasks()
            return letter
        
        # Print possible next moves and scores
        if letter == 'O':
            _,state_list = x_player.minimax(game,"X")
            for state in state_list:
                temp = game.board[:]
                temp[state['position']] = 'X'
                state['position'] = temp

        else:
            _,state_list = o_player.minimax(game,"O")
            for state in state_list:
                temp = game.board[:]
                temp[state['position']] = 'O'
                state['position'] = temp
        
        funcClearContainer(tkWindow)
        funcBoardFrames(tkWindow,style,state_list,game.board).grid(row = 0, column = 1, columnspan = 2)
        tkWindow.update_idletasks()

        # alternate player
        letter = 'O' if letter == 'X' else 'X'

        # tiny break
        if print_game:
            time.sleep(0.01)
    
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    tkWindow = Tk()
    tkWindow.title('Tic Tac Toe?')

    #Colours & fonts for the UI
    style = {'Button' : 'Yee.TButton',
            'Button2' : 'Yee2.TButton',
            'Frame' : 'Yee.TFrame',
            'Label' : 'Yee.TLabel'}
    fontBoard = font.Font(font = ('Times', 30))
    fontMain = font.Font(font = ('Consolas', 90))
    styleGen = Style()
    styleGen.configure(style['Button'], foreground = 'Black', background = 'Grey', font = fontBoard)
    styleGen.configure(style['Frame'], foreground = 'Yellow', background = 'White')
    styleGen.configure(style['Label'], foreground = 'Black', background = 'White', font = fontBoard)

    # Defining starting grid for tkinter module
    a = [{'position' : ['','','','','','','','',''],
        'score' : 0}]

    print("Welcome to TicTacToe!")
    x_player = HumanPlayer('X')
    o_player = HumanPlayer('O')
    t=TicTacToe()
    funcBoardFrames(tkWindow,style,a,t.board).grid(row = 0, column = 1)
    funcMainBoard(tkWindow,style,a[0]['position'],x_player).grid(row = 0, column = 0, columnspan = 1)
    play(t, x_player,o_player,print_game=True)

    tkWindow.mainloop()