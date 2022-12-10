import math
import random
import time
from tkinter import *
from tkinter import messagebox

# Player class
class Player:
    def __init__(self,letter):
        self.letter = letter
    
    def get_move(self,game):
        pass

# Human player class
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
        self.nextMove = IntVar
        self.previousMoves = []

    # Get move from CLI input
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8).")
            try: 
                val=int(square)
                # Check if input is an available move
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            # runs if input is not valid
            except ValueError:
                print('Invalid square. Try Again.')
                messagebox.showerror("TicTacToe Game", "Choose another box")
                
        return val

    def minimax(self,state,player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # base cases
        # 1. The previous move made by the other player wins.
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1*(state.num_empty_squares()+1) if other_player == max_player
                            else -1*(state.num_empty_squares()+1)
                    },[]
        # 2. There are no more moves to be made.
        elif not state.empty_squares():
            return {'position': None,
                    'score': 0},[]
        
        # Define worst case so that subsequent moves can be better
        if player == max_player:
            best = {'position':None,
                    'score':-math.inf}
        else: 
            best = {'position':None,
                    'score':math.inf}
        state_list = []
        # Try out every possible move and return the best position and score
        for possible_move in state.available_moves():
            # 1. simulate a state
            state.make_move(possible_move, player)
            # 2. get sim_state from minimax
            sim_state,_ = self.minimax(state, other_player)
            # 3. Undo the move
            state.board[possible_move] = ' ' 
            sim_state['position'] = possible_move
            state.current_winner = None
            # 4. Update the best move possible
            if player == max_player:
                if sim_state['score'] > best['score']:
                    best = sim_state
            else:
                if sim_state['score'] < best['score']:
                    best = sim_state
            # 5. Append sim_state to state_dict
            state_list.append(sim_state)
        return best,state_list
    
    