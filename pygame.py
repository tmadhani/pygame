#TANYA'S BREAKOUT GAME

import pygame
import random
import math
import sys
pygame.init()

#colors for game sprites
brick_red = (255, 0, 0)
brick_blue = (0,255,0)
ball_white = (255,255,255)
paddle_green = (50, 205, 50)
background_black = (0,0,0)
#setting display width/height and caption
gameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("Breakout")
pygame.display.update()

#set brick sprite height/wdith
brick_width = 50
brick_height = 10

#paddle height and width
paddle_height = 50
paddle_width = 10


#positions
x = 0
y = 0

#creating a class

class Red_Party(pygame.sprite.Sprite):
 
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([brick_width, brick_height])
        self.image.fill(brick_red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Blue_Party(pygame.sprite.Sprite):
	def __init__(self, color, x, y):
		super().__init__()
		self.image = pygame.Surface([brick_width,brick_height])
		self.image.fill(brick_blue)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Paddle(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()

class Ball(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()




