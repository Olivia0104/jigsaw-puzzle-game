# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:46:47 2021

@author: DELL
"""
import pygame
import game_function as gf
class Settings():
    def __init__(self,filepath):
        self.image = pygame.image.load(gf.GetImagePath(filepath))
        #加载图片
        self.rect = self.image.get_rect()
        self.screen_width = self.rect.width
        self.screen_height = self.rect.height
        self.bg_color = (191, 239, 255)
    