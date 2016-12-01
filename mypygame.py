#TANYA'S BREAKOUT GAME
#gold game from Colleen's repo
import pygame
import random
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

		x = 0.0
		y = 180.0

		direction = random.randint(200,300)

		height = 10
		width = 10

		self.rect.x = x
		self.rect.y = y
	
	# def hit(self, target)
	# 	return self.rect.colliderect(target)

# def increment_hit(self):
# 		self.hit_count = self.hit_count + 1
# 		if self.hit_count % 1 == 0:
# 			for ball in self.balls:
# 				ball.velocity = ball.velocity + 10
# #class Game(game):
# 	#def __init__(self):
# 		#super().__init__()


# dems = pygame.sprite.Group()
# reps = pygame.sprite.Group()
# two_party_system = pygame.sprite.Group()
# y_pos = 80
# for row in range(3):
# 	for column in range(30):
# 		blue_parties = Blue_Party(brick_blue, column * (brick_width+2)+1, y_pos)
# 		dems.add(blue_parties)
# 		two_party_system.add(blue_parties)
		
# for rown in range(3):
# 	for column in range(30):
# 		red_parties = Red_Party(brick_red, column * (brick_width+2)+1, y_pos)
# 		reps.add(red_parties)
# 		two_party_system.add(red_parties)
# # lost_game = False
# # while not lost_game:
# #     two_party_system.draw(gameDisplay)

# pygame.init()

b = Blue_Party(100, 100)
r = Red_Party(50, 50)
p = Paddle(275, 390)
bl = Ball(275, 380)
sprites = RenderPlain(b, r, p, bl)

while True:
	e = event.poll()
	if e.type == QUIT:
		quit()
		break
	# elif:
	# 	e.type == 
	gameDisplay.fill(background_black)
	p.move()
	sprites.update()
	sprites.draw(gameDisplay)
	display.update()

