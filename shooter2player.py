import pygame
import os

pygame.init()
os.chdir("D:\\sublime projects\\assets")


white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0) 

width = 1200
height = 600

game_window = pygame.display.set_mode((width,height),pygame.FULLSCREEN)


run = True




class game:
	def __init__(self):
		self.player_x = 36
		self.player_y = 519
		self.player_width = 80
		self.player_height = 80
		self.state = False
		self.vel_y = 15
		self.jump = False
		self.health = 5
		self.charatcer = pygame.image.load('player.JPG')
		self.player2_x = 1000
		self.player2_y = 519
		self.player2_width = 80
		self.player2_height = 80
		self.player2_state = False
		self.player2_vel_y = 15
		self.player2_jump = False
		self.player2_health = 5
		self.character2 = pygame.image.load('player2.jpg')
		self.health5 = pygame.image.load('5.png')
		self.health4 = pygame.image.load('4.png')
		self.health3 = pygame.image.load('3.png')
		self.health2 = pygame.image.load('2.png')
		self.health1 = pygame.image.load('1.png')
		self.player2_health5 = pygame.image.load('5 player2.png')
		self.player2_health4 = pygame.image.load('4 player2.png')
		self.player2_health3 = pygame.image.load('3 player2.png')
		self.player2_health2 = pygame.image.load('2 player2.png')
		self.player2_health1 = pygame.image.load('1 player2.png')
		self.player1_wins = pygame.image.load('player1 wins.png')
		self.player2_wins = pygame.image.load('player2 wins.png')
		self.display_heath = True

	def draw_elements(self):
		game_window.fill(white)
		self.player = pygame.draw.rect(game_window,red,[self.player_x,self.player_y,self.player_width,self.player_height])
		self.player2 = pygame.draw.rect(game_window, red, [self.player2_x,self.player2_y,self.player2_height,self.player2_width])
		game_window.blit(self.character2,(self.player2_x,self.player2_y))
		game_window.blit(self.charatcer,(self.player_x,self.player_y))



	def shoot(self):
		if not self.state:
			if key[pygame.K_SPACE]:
				self.state = True
				self.bullet_x = self.player_x+89
				self.bullet_y = self.player_y+40

		if not self.player2_state:
			if key[pygame.K_r]:
				self.player2_state = True
				self.bullet_2x = self.player2_x-19
				self.bullet_2y = self.player2_y+40

		if self.state:
			self.bullet = pygame.draw.rect(game_window,red,[self.bullet_x,self.bullet_y,15,15])
			self.bullet_x +=30
			if self.bullet_x>=1180:
				self.state = False

			

			if self.bullet.colliderect(self.player2):
				self.state = False
				self.player2_health -=1


		if self.player2_state:
				self.bullet2 = pygame.draw.rect(game_window, red, [self.bullet_2x,self.bullet_2y,15,15])
				self.bullet_2x -=30
				if self.bullet_2x<=-309:
					self.player2_state = False

				if self.bullet2.colliderect(self.player):
					self.player2_state = False
					self.health -=1



	def move(self):
		if key[pygame.K_RIGHT]:
			self.player_x +=6

		if key[pygame.K_LEFT]:
			self.player_x -=6

		if not self.jump:
			if key[pygame.K_UP]:
				self.jump = True

		if self.jump:
			self.player_y -= self.vel_y
			self.vel_y -=1
			if self.vel_y<-15:
				self.vel_y = 15
				self.jump  = False

	
	
		if key[pygame.K_d]:
			self.player2_x +=6

		if key[pygame.K_a]:
			self.player2_x -=6

		if not self.player2_jump:
			if key[pygame.K_w]:
				self.player2_jump = True


		if self.player2_jump:
			self.player2_y -= self.player2_vel_y
			self.player2_vel_y -=1

			if self.player2_vel_y<-15:
				self.player2_vel_y = 15
				self.player2_jump = False

	def manage_health(self):
		if self.health == 5:
			game_window.blit(self.health5,(10,10))

		if self.health == 4:
			game_window.blit(self.health4,(10,10))

		if self.health == 3:
			game_window.blit(self.health3,(10,10))

		if self.health == 2:
			game_window.blit(self.health2,(10,10))

		if self.health == 1:
			game_window.blit(self.health1,(10,10))



		if self.health<=0:
			game_window.fill(black)
			self.player2_health = 100
			game_window.blit(self.player2_wins,(500,300))

			







		if self.player2_health == 5:
			game_window.blit(self.player2_health5,(1030,10))

		if self.player2_health == 4:
			game_window.blit(self.player2_health4,(1030,10))

		if self.player2_health == 3:
			game_window.blit(self.player2_health3,(1030,10))

		if self.player2_health == 2:
			game_window.blit(self.player2_health2,(1030,10))

		if self.player2_health == 1:
			game_window.blit(self.player2_health1,(1030,10))



		if self.player2_health<=0:
			game_window.fill(black)
			game_window.blit(self.player1_wins,(500,300))
	

game = game()
clock = pygame.time.Clock()

while run:
	for event in pygame.event.get():
		key = pygame.key.get_pressed()

	clock.tick(60)

	
	game.draw_elements()
	game.shoot()
	game.move()
	game.manage_health()
	






	if event.type == pygame.QUIT:
		run = False

	pygame.time.delay(15)
	pygame.display.update()
