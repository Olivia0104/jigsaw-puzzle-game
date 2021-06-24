# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:33:10 2021

@author: DELL
"""
import os
import random
import pygame
import sys
import move_puzzle as mp
num = 200
#退出
def Exit():
    pygame.quit()
    sys.exit()
#获得打乱的拼图
def DisturbBoard(row,columns,Num_Cell):
    board = []
    for i in range(Num_Cell):
        board.append(i)
    blankCell = Num_Cell - 1
    board[blankCell] = -1
    for i in range(num):
        #0:left
        #1:right
        #2:down
        #3:up
        direction = random.randint(0,3)
        if direction == 0:
            blankCell = mp.moveL(board,blankCell,columns)
        elif direction == 1:
            blankCell = mp.moveR(board,blankCell,columns)
        elif direction == 2:
            blankCell = mp.moveD(board,blankCell,columns)
        elif direction == 3:
            blankCell = mp.moveU(board,blankCell,columns,row)
    return board, blankCell
def GetImagePath(filepath):
    imgs = os.listdir(filepath)
    #返回指定文件夹中的文件
    if len(imgs) == 0:
        print('文件内没有图片')
    return os.path.join(filepath,random.choice(imgs))
    #连接两个路径名
#点击事件
def check_events(game_setting,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit()
        elif event.type == pygame.KEYDOWN:
            size = None
            if event.key == ord('c'):
                    #ord返回字符的ASCLL码
                size = 2
            elif event.key == ord('b'):
                size = 3
            elif event.key == ord('a'):
                size = 4
            return size
                
#结束页面
def ShowFinishPage(screen,game_setting,game_title):
    screen.fill(game_setting.bg_color)
    screen.blit(game_title.finish,game_title.frect)
    pygame.display.update()
    while True:
        check_events(game_setting,screen)

#开始页面
def ShowStartPage(screen,game_setting,game_title):
    screen.fill(game_setting.bg_color)
    screen.blit(game_title.stitle,game_title.trect)
    screen.blit(game_title.mode,game_title.mrect)
    pygame.display.update()
    while True:
        size = None
        size = check_events(game_setting, screen)
        if size:
            return size
#判断游戏是否结束
def isFinished(board,blankCell,size):
    Num_Cell = size * size
    for i in range(Num_Cell - 1):
        #剩下的拼图都在自己的位置
        if board[i] != i:
            return False
    return True