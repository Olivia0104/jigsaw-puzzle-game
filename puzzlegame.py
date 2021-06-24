# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:12:56 2021

@author: DELL
"""

import pygame
import pygame.font
import game_function as gf
from settings import Settings
from title import Title
def run_game():
    pygame.init()
    game_setting = Settings('./images')
    screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
    game_title = Title(game_setting,screen)
    pygame.display.set_caption('拼图游戏')
    size = gf.ShowStartPage(screen, game_setting, game_title)
    if isinstance(size,int):
        #如果size是int型
        row = size
        columns = size
        Num_Cell = size * size
    cellWidth = game_setting.screen_width // columns
    cellHeight = game_setting.screen_height // row
    #计算Cell的大小
    finish = False
    #避免初始化为原图
    while True:
        gameBoard, blankCell = gf.DisturbBoard(row,columns,Num_Cell)
        if not gf.isFinished(gameBoard,blankCell,size):
            break
    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gf.Exit()
             
             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 #左鼠标点击
                x,y = pygame.mouse.get_pos()
                x_pos = x // cellWidth
                #向下取整数
                y_pos = y // cellHeight
                idx = x_pos + y_pos * columns
                if idx==blankCell-1 or idx==blankCell+1 or idx==blankCell+columns or idx==blankCell-columns:
                    gameBoard[blankCell],gameBoard[idx] = gameBoard[idx],gameBoard[blankCell]
                    blankCell = idx
                #移动拼图
        if gf.isFinished(gameBoard, blankCell, size):
            gameBoard[blankCell] = Num_Cell - 1
            finish = True
        if finish:
            gf.ShowFinishPage(screen, game_setting, game_title)
        screen.fill(game_setting.bg_color)
        for i in range(Num_Cell):
            if gameBoard[i] == -1:
                continue
            x_pos = i%columns
            y_pos = i//columns
            rect = pygame.Rect(x_pos*cellWidth, y_pos*cellHeight,cellWidth,cellHeight)
            PuzzleArea = pygame.Rect((gameBoard[i]%columns)*cellWidth,(gameBoard[i]//columns)*cellHeight,cellWidth,cellHeight)
            #(left,top,width,height)
            screen.blit(game_setting.image,rect,PuzzleArea)
            #图像，绘制的位置，绘制的图片
        pygame.display.update()
run_game()








