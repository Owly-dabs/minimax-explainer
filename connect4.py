#! /usr/bin/env python3

import math
import random
from player2 import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class Connect4:
    def __init__(self):
        self.board = ['.' for _ in range(42)]
        self.current_winner = None

    def print_board(self):
        print("  0 1 2 3 4 5 6  ")
        for row in [self.board[i*7:(i+1)*7] for i in range(6)]:
            print("| " + ' '.join(row) + " |")
    
    @staticmethod
    def print_board_nums():
        num_board = ['0'+str(i) if (i//10)<1 else str(i) for i in range(42)]
        for row in [num_board[i*7:(i+1)*7] for i in range(6)]:
            print("| " + ' '.join(row) + " |")
    
    def available_spots(self):
        return [i for (i,spot) in enumerate(self.board) if spot == '.']

    def available_moves(self):
        return [i for i in range(7) if i in [int(n%7) for n in self.available_spots()]]

    def empty_spots(self):
        return '.' in self.board
    
    def empty_spots_num(self):
        return self.board.count('.')

    def make_move(self, selected_col, letter):
        spot = max([n for n in self.available_spots() if n%7==selected_col])
        self.board[spot] = letter
        if self.winner(spot,letter):
            self.current_winner = letter
    
    def undo_move(self,selected_col, letter):
        taken_spots = [i for (i,spot) in enumerate(self.board) if spot != '.']
        spot = max([n for n in taken_spots if n%7==selected_col])
        self.board[spot] = '.'
        
    def winner(self,spot,letter):
        row_i = spot//7
        column_i = spot%7
        # Check row
        
        row = self.board[row_i*7:(row_i+1)*7]
        if column_i//4 == 0:
            possible_row_wins = [row[i:i+4] if i!=0 else row[:4] for i in range(column_i+1)]
        else:
            possible_row_wins = [row[-i-4:-i] if i!=0 else row[-4:] for i in range(7-column_i)]

        for poss in possible_row_wins:
            if all([space == letter for space in poss]): return True
               
        # Check column
        column = [self.board[column_i + k*7] for k in range(6)]
        if row_i//3 == 0:
            possible_col_wins = [column[i:i+4] if i!=0 else column[:4] for i in range(row_i+1)]
        else:
            possible_col_wins = [column[-i-4:-i] if i!=0 else column[-4:] for i in range(6-row_i)]

        for poss in possible_col_wins:
            if all([space == letter for space in poss]): return True

        # Check left diagonal (NOT WORKING)
        if row_i-column_i<3 and column_i-row_i<4:
            Ldiag_i = spot%8
            l_dict = {0:[0,8,16,24,32,40],
                        1:[1,9,17,25,33,41],
                        2:[2,10,18,26,34],
                        3:[3,11,19,27],
                        6:[14,22,30,38],
                        7:[7,15,23,31,39]}
            if Ldiag_i in l_dict:
                possible_Ldiag_wins = [[self.board[i] for i in ls] for ls in [l_dict[Ldiag_i][i:i+4] for i in range(len(l_dict[Ldiag_i])-3)]]
                for poss in possible_Ldiag_wins:
                    if all([space == letter for space in poss]): return True

        # Check right diagonal (NOT WORKING)
        if spot not in [0,1,2,7,8,14,27,33,34,39,40,41]:
            Rdiag_i = spot%6
            r_dict = {1:[13,19,25,31,37],
                        2:[20,26,32,38],
                        3:[3,9,15,21],
                        4:[4,10,16,22,28],
                        5:[5,11,17,23,29,35],
                        0:[6,12,18,24,30,36]}            
            possible_Rdiag_wins = [[self.board[i] for i in ls] for ls in [r_dict[Rdiag_i][i:i+4] for i in range(len(r_dict[Rdiag_i])-3)]]
            for poss in possible_Rdiag_wins:
                if all([space == letter for space in poss]): return True     

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_spots():
        game.print_board()
        # Get move
        if letter == 'X': spot = x_player.get_move(game) 
        else: spot = o_player.get_move(game)
        # Make move
        game.make_move(spot,letter)
        # Check if there's a winner
        if game.current_winner:
            game.print_board()
            print(f"{letter} wins!")
            return letter
        
        # Alternate player
        letter = 'O' if letter == 'X' else 'X'
        
        # tiny break
        time.sleep(0.1)
    print(f"It's a draw.")

if __name__ == '__main__':
    print("Welcome to Connect 4!")
    print("Who will play as player 1?\na\tYou\nb\tRandom Computer\nc\tGenius Computer which take eternity ")
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
    t = Connect4()
    play(t, x_player, o_player)