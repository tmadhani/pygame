
import pygame
import math
import random


brick_red = (255, 0, 0)
brick_blue = (0,0,255)
ball_white = (255,255,255)
paddle_green = (50, 205, 50)
background_black = (0,0,0)

#set brick sprite height/wdith
brick_width = 50
brick_height = 10


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
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("media/vote.bmp")
		self.width = 46
		self.height = 53
		# self.image.fill(paddle_green)
		self.rect = self.image.get_rect()
		self.screenheight = pygame.display.get_surface().get_height()
		self.screenwidth = pygame.display.get_surface().get_width()
		self.rect.x = 0
		self.rect.y = self.screenheight-self.height

	def update(self):
		p = pygame.mouse.get_pos()
		self.rect.x = p[0]
		if self.rect.x > self.screenwidth - self.width:
			self.rect.x = self.screenwidth - self.width
	
class Ball(pygame.sprite.Sprite):
	speed = 10.0

	direction = random.randint(180,200)

	x = 275
	y = 200

	width = 10
	height = 10
	def __init__(self):
		super().__init__()
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(ball_white)
		self.rect = self.image.get_rect()
		
		self.screenheight = pygame.display.get_surface().get_height()
		self.screenwidth = pygame.display.get_surface().get_width()

	def deflect(self,ball_presence):
		self.direction = (180 - self.direction) % 360
		self.direction -= ball_presence

	def update(self):
		ball_move = math.radians(self.direction)
		self.x += self.speed * math.sin(ball_move)
		self.y -= self.speed * math.cos(ball_move)

		self.rect.x = self.x
		self.rect.y = self.y

		if self.y <= 0:
			self.deflect(0)
			self.y = 1

		if self.x <= 0:
			self.direction = (360-self.direction) % 360
			self.x = 1

		if self.x > self.screenwidth - self.width:
			self.direction = (360-self.direction)%360
			self.x = self.screenwidth-self.width -1

		if self.y > 400:
			return True
		else:
			return False

pygame.init()
screen_pic = pygame.image.load("media/capitol_hill.bmp")
gameDisplay = pygame.display.set_mode((600,400))
pygame.display.set_caption("Political Breakout")

pygame.mouse.set_visible(False)

f = pygame.font.Font(None,45)
l = pygame.font.Font(None, 35)
bg = pygame.Surface(gameDisplay.get_size())

democrats = pygame.sprite.Group()
republicans = pygame.sprite.Group()
balls = pygame.sprite.Group()
two_party_system = pygame.sprite.Group()
total_sprites = pygame.sprite.Group()

p = Paddle()
total_sprites.add(p)

ball = Ball()
balls.add(ball)
total_sprites.add(ball)

y_pos = 10
y_pos_red = 55
num_blocks = 10

for row in range(4):
	for column in range(0,num_blocks):
		dems = Blue_Party(column * (brick_width + 2) + 1, y_pos)
		democrats.add(dems)
		two_party_system.add(dems)
	y_pos += brick_height + 2
for row in range(4):
	for column in range(0, num_blocks):
		reps = Red_Party(column*(brick_width+2)+1,y_pos_red)
		republicans.add(reps)
		two_party_system.add(reps)
	y_pos_red+=brick_height+2

timer = pygame.time.Clock()

finish_game = False
close_game = False

total_sprites.add(two_party_system)

hits = 0

while not close_game:
	timer.tick(30)
	# gameDisplay.fill(background_black)
	gameDisplay.blit(screen_pic,(0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			close_game = True

	if not finish_game:
		p.update()
		finish_game = ball.update()

	if finish_game:
		pygame.mixer.Sound("media/national-anthem.wav").play()
		if len(two_party_system) == 0:
			text = l.render("You were successfully able to break the two party system!", True, ball_white)
			text_loc = text.get_rect(centerx=bg.get_width()/2)
			text_loc.top = 200
			gameDisplay.blit(text,text_loc)
		else:
			text = l.render("You were not able to break the two party system.", True, ball_white)
			text_loc = text.get_rect(centerx=bg.get_width()/2)
			text_loc.top = 200
			gameDisplay.blit(text, text_loc)

	if pygame.sprite.spritecollide(ball, two_party_system, False):
		pygame.mixer.Sound("media/bloop.wav").play()
		ball.speed+=5

	if pygame.sprite.spritecollide(p,balls,False):
		ball_presence = (p.rect.x + p.width/2) - (ball.rect.x+ball.width/2)
		ball.rect.y = gameDisplay.get_height() - p.rect.height - ball.rect.height -1
		ball.deflect(ball_presence)

	dissolve_blocks = pygame.sprite.spritecollide(ball,two_party_system,True)
	for block in dissolve_blocks:
		hits +=1
	new_t = f.render('Hits: ' + str(hits), False, ball_white)
	text_loc = new_t.get_rect(centerx=bg.get_width()/2)
	text_loc.top = 300
	gameDisplay.blit(new_t, text_loc)

	if len(dissolve_blocks) > 0:
		ball.deflect(0)

	total_sprites.draw(gameDisplay)
	pygame.display.flip()

pygame.quit()
