# Minimax visualizer
A Minimax score visualization tool on the game of TicTacToe

## Problem Statement
**Context**: This version of the TicTacToe game is aimed to be a visualisation aid that illustrates how the minimax algorithm works. Algorithms are not as intuitive or easy to grasp especially for people newer to such processes. Many are taught about decision trees but unsure how this helps lead an AI to play the best possible move each time. Hence, this programme calculates the score for all subsequent moves and shows the scores accordingly. The user can then observe how a minimax algorithm scores the possible moves and make the next best possible move.

**Description of the game:** In this version of TicTacToe, players take turns clicking the spaces in a three-by-three grid with 'X' or 'O'. As every move is made, a score is calculated by the Minimax Algorithm to visually show what is the best possible move the player can make next to win the game.

## Running Locally
### TicTacToe
1. Clone this repo into a local directory and navigate to the directory.
2. Run in terminal.
    ```
    python game.py
    ```
3. Have fun!

## Minimax Algorithm

The Minimax algorithm is a recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that the opponent is also playing optimally. It uses recursion to search through the game tree and computes the minimax decision for the current state.

### How it Works
One player is the maximising player and the other is the minimising player. Every turn, the maximising player chooses the move with the highest score, while the minimising player chooses the move with the lower score. 

The minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree and proceeds all the way down to the terminal node of the tree, then backtracks to determine the other sibling terminal nodes while assigning the scores to the respective possible next moves.

## Minimax Score Calculation
The score for each possible move is calculated with the following formula:
```
if player wins:
    score = 1 * (number of empty squares left + 1)
elif player loses:
    score = -1 * (number of empty squares left + 1)
else: #in the case of a draw
    score = 0
```

## Documentation
### `game.py` module
A class, `TicTacToe`, is created as the object of the game. The key attributes it initializes are the initial state of the `board`, and the current winner, which is set to None.

The game starts when the `play` function is called. While there are still empty squares in the `board`, the function does the following:
1. Update the `MainBoard`, the player's board on the left side of the tkinter window, which displays the current state of `board`
2. Get move from respective player.
3. Make move on `board`.
4. Check if there is a winner after the move was made. If yes, the `play` function returns.
5. Create list of possible next moves and their respective scores using the `minimax` function from `display.py` module.
6. Update the `BoardFrames`, all the boards on the right side of tkinter window showing the possible next moves and their respective scores.

### `dPlayer.py` module
A class is also created for the player, `HumanPlayer`, where it is assigned a letter, either 'X' or 'O'. 

The function `get_move` gets the user to input their next move. It also checks whether the move is valid.

The function `minimax` calculates the score for every possible next move that the player can make. The function is recursive, where the base cases are when a player wins or there are no more empty squares left. 


### `display.py` module
The display module generates UI elements displayed on the GUI using the ttk widgets provided by Tk.

The 2 main elements in the UI are the current position of the tic tac toe game which displays of the left and the list of possible future states on the right.

#### **Functions**
All functions except `funcClearContainer` and `funcFirstDiffIndex` take as inputs a `root`, the ttk container that the frame is to be generated in and a `style` dictionary defining the appearance of the ttk widgets in addition to the others detailed below.

- `funcFirstDiffIndex` takes in 2 lists of equal length and returns the index of the first item between both lists that differ. It is used exclusively by `funcGenBoard` to identify where the next position is.

- `funcGenBoard` generates a tic tac toe board as a ttk frame and attaches the move     number of the next position and the associated minimax score of the position. As input, the function takes in
  - a dictionary containing the `'position'` and `'score'` of the position
  - a list of the current game position
  - The function returns the `ttk` frame which can then be assgined to a grid position using `.grid()` or `.pack()`.

- `funcBoardFrames` generates a ttk frame containing all possible next moves of the tic tac toe game. Individual boards are generated using funcGenBoard. The boards are dynamically arranged in columns of 4. As input, the function takes in
  - a list containing the possible future positions as dictionaries, used by funcGenBoard
  - a list of the current game position, used by `funcGenBoard`
  - The function returns the `ttk` frame which can be arranged the same way as `funcGenBoard`.

- `funcMainBoard` generates a tic tac toe board as a ttk frame similar to `funcGenBoard`. This board represents the current position of the game. As input, the function takes in
  - a list containing the position of the game
  - The function returns the `ttk` frame which can be arranged the same way as `funcGenBoard`.

- `funcVictoryLabel` generates a `ttk.Label` when the game reaches an end state. As input, the function takes in
  - a string containing either the final draw state or victor's game marker
  - The function returns the `ttk.Label` which can be assigned to a grid position.

- `funcClearContainer` destroys all items in a ttk container such as a window or frame. This function only takes in the container as input does not return anything.
