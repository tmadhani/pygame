import math
import pygame
 
# Define some colors
brick_red = (255, 0, 0)
brick_blue = (0,0,255)
ball_white = (255,255,255)
paddle_green = (50, 205, 50)
background_black = (0,0,0)
 
# Size of break-out blocks
brick_width = 50
brick_height = 10

# paddle_height = 10
# paddle_width = 50
 
 
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
 
 
class Ball(pygame.sprite.Sprite):
    """ This class represents the ball
        It derives from the "Sprite" class in Pygame """
 
    # Speed in pixels per cycle
    speed = 10.0
 
    # Floating point representation of where the ball is
    x = 0.0
    y = 180.0
 
    # Direction of ball (in degrees)
    direction = 200
 
    width = 10
    height = 10
 
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create the image of the ball
        self.image = pygame.Surface([self.width, self.height])
 
        # Color the ball
        self.image.fill(ball_white)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
    def bounce(self, diff):
        """ This function will bounce the ball
            off a horizontal surface (not a vertical one) """
 
        self.direction = (180 - self.direction) % 360
        self.direction -= diff
 
    def update(self):
        """ Update the position of the ball. """
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the top of the screen?
        if self.y <= 0:
            self.bounce(0)
            self.y = 1
 
        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1
 
        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1
 
        # Did we fall off the bottom edge of the screen?
        if self.y > 600:
            return True
        else:
            return False
 
 
class Paddle(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.width = 50
		self.height = 10
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(paddle_green)
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
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Breakout')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 36)
 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Create sprite lists
democrats = pygame.sprite.Group()
republicans = pygame.sprite.Group()
balls = pygame.sprite.Group()
two_party_system = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
 
# Create the player paddle object
player = Paddle()
allsprites.add(player)
 
# Create the ball
ball = Ball()
allsprites.add(ball)
balls.add(ball)
 
y_pos = 10
y_pos_red = 55
num_blocks = 12

for row in range(0,4):
	for column in range(0,num_blocks):
		dems = Blue_Party(column * (brick_width + 2) + 1, y_pos)
		democrats.add(dems)
		two_party_system.add(dems)
	y_pos += brick_height + 2
for row in range(0,4):
	for column in range(0, num_blocks):
		reps = Red_Party(column*(brick_width+2)+1,y_pos_red)
		republicans.add(reps)
		two_party_system.add(reps)
	y_pos_red+=brick_height+2
allsprites.add(two_party_system)
 
# Clock to limit speed
clock = pygame.time.Clock()
 
# Is the game over?
game_over = False
 
# Exit the program?
exit_program = False
 
# Main program loop
while not exit_program:
 
    # Limit to 30 fps
    clock.tick(30)
 
    # Clear the screen
    screen.fill(background_black)
 
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
 
    # Update the ball and player position as long
    # as the game is not over.
    if not game_over:
        # Update the player and ball positions
        player.update()
        game_over = ball.update()
 
    # If we are done, print game over
    if game_over:
        text = font.render("You were unable to break the two party system", True, ball_white)
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        screen.blit(text, textpos)
 
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player, balls, False):
        # The 'diff' lets you try to bounce the ball left or right
        # depending where on the paddle you hit it
        diff = (player.rect.x + player.width/2) - (ball.rect.x+ball.width/2)
 
        # Set the ball's y position in case
        # we hit the ball on the edge of the paddle
        ball.rect.y = screen.get_height() - player.rect.height - ball.rect.height - 1
        ball.bounce(diff)
 
    # Check for collisions between the ball and the blocks
    deadblocks = pygame.sprite.spritecollide(ball, two_party_system, True)
 
    # If we actually hit a block, bounce the ball
    if len(deadblocks) > 0:
        ball.bounce(0)
 
        # Game ends if all the blocks are gone
        if len(two_party_system) == 0:
            game_over = True
 
    # Draw Everything
    allsprites.draw(screen)
 
    # Flip the screen and show what we've drawn
    pygame.display.flip()
 
pygame.quit()
