import pygame
pygame.init()

screen_width = 1200
screen_height = 600
white = (255,255,255)
black = (0,0,0)
game_window = pygame.display.set_mode((screen_width,screen_height))

player_x = 36
player_y = 583

vel_y = 15
jump = False

def update():
	pygame.display.update()


def draw():
	global player_x
	global player_y
	game_window.fill(white)
	pygame.draw.rect(game_window,black,[player_x,player_y,15,15])

def sleep(time):
	pygame.time.delay(time)

run = True
character = 0
while run:
	for event in pygame.event.get():
		key = pygame.key.get_pressed()

	draw()

	if key[pygame.K_n]:
		character = 'nano'
		jump = False
		vel_y = 20
		print(character)

	if event.type == pygame.QUIT:
		run = False

	if key[pygame.K_RIGHT]:
		if character == 'nano':
			player_x = player_x+1

	if key[pygame.K_RIGHT]:
		if character != 'nano':
			player_x = player_x+6
		
		

	if key[pygame.K_LEFT]:
		if character == 'nano':
			player_x = player_x-1

	if key[pygame.K_LEFT]:
		if character != 'nano':
			player_x = player_x-6


	if jump == False:
		if key[pygame.K_UP]:
			jump = True

	if jump == True:
		if character == 'nano':
			player_y = player_y-vel_y
			vel_y = vel_y-1
			if vel_y <-20:
				jump = False
				vel_y = 20

	if jump == True:
		if character != 'nano':
			player_y = player_y-vel_y
			vel_y = vel_y-1
			if vel_y <-15:
				jump = False
				vel_y = 15

	if key[pygame.K_g]:
		vel_y = 15
		character = 'gobo'


	sleep(15)		
	update()	
