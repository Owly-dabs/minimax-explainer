# Minimax visualizer
An intuitive minimax decision tree visualization tool on the games of TicTacToe and Connect4.

## Outlining the stages
1. (Completed) Build a TicTacToe game and a computer player with a minimax algorithm. (Done. Credits to [Kylie Ying](https://github.com/kying18/tic-tac-toe)
2. (Completed) Build a Connect4 game and a computer player with minimax algorithm. (Done. However, it takes too long to make a decision due to the exponential increase in number of possible outcomes.)
3. (Done for TicTacToe) Build a python GUI using tkinter to visualize the possible next moves the computer sees and the respective scores for each move.
4. (Completed) Implement alpha-beta pruning algorithm. (However, it still takes too long to make a decision.)
5. (To Do) Consider Deep Reinforcement Learning for [Connect4](https://codebox.net/pages/connect4) and pit both algorithms against each other. (excites!)
6. (To Do) Consider using a web-based application for easier accessibility.

## Running Locally
### TicTacToe Visualizer
1. Clone this repo into a local directory and navigate to `./tictactoe-minimax-visualizer`.
2. Run in terminal.
    ```
    python game.py
    ```
3. Have fun!


### TicTacToe
1. Clone this repo into a local directory and navigate to the directory.
2. Run in terminal.
    ```
    python tictactoe.py
    ```
3. Choose players.
4. Have fun!
   
### Connect 4
1. Clone this repo into a local directory and navigate to the directory.
2. Run in terminal.
    ```
    python connect4.py
    ```
3. Choose players.
4. Have fun!

## Minimax Algorithm

The Minimax algorithm is an algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that the opponent is also playing optimally. It uses recursion to search through the game tree and computes the minimax decision for the current state.

The Minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree and proceeds all the way down to the terminal node of the tree, then backtracks to determine the other sibling terminal nodes while assigning the scores to the respective possible next moves.

