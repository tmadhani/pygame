#TANYA'S BREAKOUT GAME
#gold game from Colleen's repo
import pygame
import random
import math
from math import *
from pygame import *
from pygame.sprite import *
pygame.init()
#colors for game sprites
brick_red = (255, 0, 0)
brick_blue = (0,0,255)
ball_white = (255,255,255)
paddle_green = (50, 205, 50)
background_black = (0,0,0)


gameDisplay = pygame.display.set_mode((600,400))

pygame.display.set_caption("Breakout")
pygame.display.update()

mouse.set_visible(False)
#set brick sprite height/wdith
brick_width = 50
brick_height = 10

#paddle height and width
paddle_height = 10
paddle_width = 50

#ball height and width
ball_width = 10
ball_height = 10


#positions
x = 0
y = 0

#creating a class

class Red_Party(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([brick_width, brick_height])
        self.image.fill(brick_red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Blue_Party(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([brick_width,brick_height])
		self.image.fill(brick_blue)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Paddle(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([paddle_width, paddle_height])
		self.image.fill(paddle_green)
		self.rect = self.image.get_rect()
		self.screenheight = pygame.display.get_surface().get_height()
		self.screenwidth = pygame.display.get_surface().get_width()
		self.rect.x = x
		self.rect.y = y
	
	def move(self):
		p = pygame.mouse.get_pos()
		self.rect.x = p[0]
		#self.rect.y = p[1]

class Ball(pygame.sprite.Sprite):


	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface([ball_width, ball_height])
		self.image.fill(ball_white)
		self.rect = self.image.get_rect()
		
		hit_count = 0
		velocity = 4.0

		direction = random.randint(200,300)

		height = 10
		width = 10

		self.rect.x = x
		self.rect.y = y

		self.screenheight = pygame.display.get_surface().get_height()
		self.screenwidth = pygame.display.get_surface().get_width()

	def deflect(self):
		self.direction = (180 - self.direction) % 360
		self.direction = self.direction - ball_presence

	def ball_bounce(self):
		ball_move = math.radians(self.direction)
		self.x = self.x + (self.velocity * math.sin(ball_move))
		self.y -= (self.velocity & math.cos(ball_move))

	
	def hit(self, target):
		return self.rect.colliderect(target)


b = pygame.sprite.Group()
r = pygame.sprite.Group()
p = Paddle(275, 390)
bl = Ball(275,380)
y_pos = 10
y_pos_red = 55
num_blocks = 12

for row in range(0,4):
	for column in range(0,num_blocks):
		dems = Blue_Party(column * (brick_width + 2) + 1, y_pos)
		b.add(dems)
	y_pos += brick_height + 1
for rown in range(0,4):
	for column in range(0, num_blocks):
		reps = Red_Party(column*(brick_width+2)+1,y_pos_red)
		r.add(reps)
	y_pos_red+=brick_height+1

sprites = RenderPlain(b, r, p, bl)

finish_game = False

while True:
	e = event.poll()
	if e.type == QUIT:
		quit()
		break
	if not finish_game:
		p.move()
		finish_game = bl.ball_bounce()
	if pygame.sprite.spritecollide(p,bl,False):
		ball_presence = (p.rect.x + p.width/2) - (b.rect.x+bl.width/2)
		bl.rect.y = screen.get_height() - p.rect.heigth - bl.rect.heigth -1
		bl.deflect(ball_presence)
	dissolve_blocks = pygame.sprite.spritecollide(bl,r,True)
	if len(dissolve_blocks) > 0:
		finish_game = True
		if len(r) == 0:
			finish_game = True



	# else:
	# 	if pygame.sprite.spritecollide(p, bl, False):
	# 		ball_presence = (p.rect.x + p.width/2) - (b.rect.x+b.width/2)
	# 		b.rect.y = screen.get_height() - p.rect.height - b.rect.height - 1
	# 		b.bounce(ball_presence)
	gameDisplay.fill(background_black)
	# p.move()
	sprites.update()
	sprites.draw(gameDisplay)
	display.update()
pygame.quit()

