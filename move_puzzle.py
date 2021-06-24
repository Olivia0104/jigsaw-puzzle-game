# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:27:08 2021

@author: DELL
"""

#拼图右移
def moveR(board,blankCell,columns):
    if blankCell % columns == 0:
        return blankCell
    board[blankCell-1],board[blankCell] = board[blankCell],board[blankCell-1]
    return blankCell - 1
#拼图左移
def moveL(board,blankCell,columns):
    if (blankCell+1)%columns == 0:
        return blankCell
    board[blankCell + 1],board[blankCell]=board[blankCell],board[blankCell+1]
    return blankCell+1
#拼图下移
def moveD(board,blankCell,columns):
    if blankCell < columns:
        return blankCell
    board[blankCell-columns],board[blankCell]=board[blankCell],board[blankCell-columns]
    return blankCell-columns
#拼图上移
def moveU(board,blankCell,columns,row):
    if blankCell >= (row-1)*columns:
        return blankCell
    board[blankCell+columns],board[blankCell]=board[blankCell],board[blankCell+columns]
    return blankCell+columns