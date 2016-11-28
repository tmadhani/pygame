#TANYA'S BREAKOUT GAME

import pygame
import random
import math
pygame.init()

#colors for game sprites
brick_red = (255, 0, 0)
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

#positions
x = 0
y = 0

gameExit = False
while not gameExit:
	game.Display.fill(background_black)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			x_delta = 0
			y_delta = 0
			if event.key == pygame.K_LEFT:
				x_delta -= 5
			if event.key == pygame.K_RIGHT:
				x_delta += 5
			if event.key == pygame.K_UP:
				y_delta -= 5
			if event.key == pygame.K_DOWN:
				y_delta += 5
		x += x_delta
		y += y_delta

class Brick(pygame.sprite.Sprite):
	def __init__(self, color = brick_red, x = 0, y = 0):
		self.image()






