#!/usr/bin/env python3
import time
from random import Random
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # List of 9 variables to create 3x3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # prints a board of sequential numbers
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        
    def available_moves(self):
        return [i for (i,spot) in enumerate(self.board) if spot == ' ']
        #moves = []
        #for (i,spot) in enumerate(self.board):
        #    if spot == ' ':
        #        moves.append(i)
        #return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        # winner if 3 in a row anywhere
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

        """
        indexes = []
        # Get index of letters from board
        for ind,spot in enumerate(self.board):
            if spot == letter:
                indexes.append(ind)

        winning_combi = [[0,1,2],[3,4,5],[6,7,8],
                        [0,3,6],[1,4,7],[2,5,8],
                        [0,4,8],[2,4,6]]
        for winning_ind in winning_combi:
            if winning_ind in indexes:
                return True
        return False
        """


def play(game,x_player,o_player,print_game=True):
    # returns the winner of the game or returns None (tie)
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter

    while game.empty_squares():
        # get the move from the correct player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # function to make a move
        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
        
        # Check if theres a current winner
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter

        # alternate player
        letter = 'O' if letter == 'X' else 'X'

        # tiny break
        if print_game:
            time.sleep(0.8)
    
    if print_game:
        print('It\'s a tie!')
        
if __name__ == '__main__':
    print("Welcome to TicTacToe!")
    print("Who will play as player 1?\na\tYou\nb\tRandom Computer\nc\tGenius Computer")
    player_choice=''
    while player_choice!='a' and player_choice!='b' and player_choice!='c':
        player_choice = input("Please enter a, b, or c.\n")
    if player_choice == 'a':x_player = HumanPlayer('X')
    elif player_choice == 'b':x_player = RandomComputerPlayer('X')
    elif player_choice == 'c':x_player = GeniusComputerPlayer('X')

    print("Who will play as player 2?")
    player_choice=''
    while player_choice!='a' and player_choice!='b' and player_choice!='c':
        player_choice = input("Please enter a, b, or c.\n")
    if player_choice == 'a':o_player = HumanPlayer('X')
    elif player_choice == 'b':o_player = RandomComputerPlayer('X')
    elif player_choice == 'c':o_player = GeniusComputerPlayer('X')
    t = TicTacToe()
    play(t,x_player,o_player,print_game=True)