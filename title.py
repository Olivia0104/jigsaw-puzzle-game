# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:05:18 2021

@author: DELL
"""
import pygame
import pygame.font

class Title():
    def __init__(self,game_setting,screen):
        self.screen = screen
        font = pygame.font.SysFont(None, 48)
        #设置为默认字体
        self.screen_rect = self.screen.get_rect()
        self.stitle = font.render("Press 'A,B,C' to choose the mode", True, (100, 149, 237))
        self.trect = self.stitle.get_rect()
        self.trect.midtop = (self.screen_rect.width/2,self.screen_rect.height/4)
        self.mode = font.render("A:4*4   B:3*3   C:2*2", True, (255, 255, 255))
        self.mrect = self.mode.get_rect()
        self.mrect.midtop = (self.screen_rect.width/2,self.screen_rect.height/2)
        self.finish = font.render("Great!", True, (255, 192, 203))
        self.frect = self.finish.get_rect()
        self.frect.midtop = (self.screen_rect.width/2,self.screen_rect.height/2)
        
        
        
        
        
        
        
        