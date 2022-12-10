from tkinter import font, Tk, constants, Canvas
from tkinter.ttk import *
import time

#function identifying the first differing index between 2 lists of equal length
def funcFirstDiffIndex(lsOne, lsTwo):
    for i in range(len(lsOne)):
        if lsOne[i] != lsTwo[i]:
            return str(i)
    return str(-1)

#function generating future boards along with the associated minimax score
def funcGenBoard(root, style, dictState, lsCurrent):
    frameState = Frame(root, style = style['Frame'])
    frameBoard = Frame(frameState, padding = 5, style = style['Frame'])
    lsButtonStore = []
    for item in dictState['position']:
        lsButtonStore.append(Button(frameBoard, width = 2, text = item, style = style['Button']))
    #button position assignment
    num = 0
    for i in range(3):
        for j in range(3):
            lsButtonStore[num].grid(row = i, column = j)
            num += 1
    #identify new position to retrieve 
    strNext = funcFirstDiffIndex(dictState['position'], lsCurrent) 
    frameBoard.grid(row = 0, column = 0)
    Label(frameState, text = 'P:' + strNext + '\n'+ str(dictState['score']), width = 3, style = style['Label'], padding = 3).grid(row = 0, column = 1)
    return frameState
 
#function generating the right panel of possible next moves
def funcBoardFrames(root, style, lsStates, lsCurrent):
    frameDisplay = Frame(root)
    i = 0
    j = 0
    for dictState in lsStates: #placing each possible future board in columns of 4
        if i < 4:
            i += 1
            funcGenBoard(frameDisplay, style, dictState, lsCurrent).grid(row = i, column = j)
        else:
            i = 1
            j += 1
            funcGenBoard(frameDisplay, style, dictState, lsCurrent).grid(row = i, column = j)
    Label(frameDisplay, text = 'Possible Moves', style = style['Label']).grid(row = 0, column = 0, columnspan = j+1)
    return frameDisplay

def updateNextMove(player, move):
    player.nextMove = move

#function generating the left panel of the current state of the game
def funcMainBoard(root,style,lsBoard,player):
    frameMain = Frame(root, style = style['Frame'])
    frameBoard = Frame(frameMain, style = style['Frame'])
    Label(frameMain, text = 'Current Move:', style = style['Label']).grid(row = 0, column = 0)
    lsButtonStore = []
    for move,item in enumerate(lsBoard):
        lsButtonStore.append(Button(frameBoard, width = 2, text = item, command=lambda:updateNextMove(player,move), style = style['Button']))
    num = 0
    for i in range(3):
        for j in range(3):
            lsButtonStore[num].grid(row = i, column = j)
            num += 1
    frameBoard.grid(row = 1, column = 0)
    return frameMain

#function generates a statement after a player wins
def funcVictoryLabel(root, style, victor):
    return Label(root, style = style['Label'], text = victor + ' wins!')

#function clears previous display
def funcClearContainer(root):
    for child in root.winfo_children():
        child.destroy()

if __name__ == '__main__':
    pass