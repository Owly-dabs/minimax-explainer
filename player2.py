#! /usr/bin/env python3

import math
import random
import time

class Player():
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        while not valid_square:
            try:
                player_input = int(input("Enter a column from 0 to 6: "))
                if player_input not in game.available_moves():
                    raise ValueError
                #spot = player_input + 7*(game.available_moves().count(player_input)-1)
                valid_square = True
            except:
                print("Invalid move. Try again.")
        return player_input

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self, game):
        selected_col = random.choice(game.available_moves())

        return selected_col

class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def minimax(self, state, player,alpha=-math.inf,beta=math.inf):
        # Define max player and other player
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        # Base case: Other player, aka previous player wins.
        if state.current_winner == other_player:
            return {
                'position':None,
                'score':1*(state.empty_spots_num() + 1) if max_player == other_player else (-1)*(state.empty_spots_num()+1)
                }
        elif not state.empty_spots():
            return {
                'position': None,
                'score': 0
            }
        # Set the best dictionaries
        if player == max_player:
            best = {
                'position':None,
                'score': -math.inf
            } 
        else: 
            best = {
                'position': None,
                'score': math.inf
            }
        # Set Alpha Beta pruning conditions
        

        # make move
        for possible_move in state.available_moves():
            # 0. Alpha-beta prune
            if alpha>=beta: 
                print("PRUNED")
                continue
            # 1. Make Move
            state.make_move(possible_move, player)
            # 2. Recurse with minimax (go on to next move and switch player)
            ### Debugging testing
            print("Simulated Board")
            state.print_board()
            time.sleep(0.001)
            sim_score = self.minimax(state,other_player,alpha,beta)
            # 3. Undo Move, undo current winner and set the state in dictionary
            state.undo_move(possible_move,player)
            state.current_winner = None
            sim_score['position'] = possible_move
            # 4. Update dictionary if needed
            if player == max_player:
                if sim_score['score']>best['score']:
                    best = sim_score
                alpha = max(alpha,sim_score['score'])
            else:
                if sim_score['score']<best['score']:
                    best = sim_score
                beta = min(beta,sim_score['score'])

        # return score
        return best

        # undo move
    def get_move(self, game):
        spot = self.minimax(game,self.letter)['position']
        return spot
