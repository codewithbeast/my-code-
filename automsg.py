import pygame 
from threading import *
pygame.init()

red = (255,0,0)
game_window = pygame.display.set_mode((1200,600))

run = True

class game(Thread):
    
    player_x = 10
    player_y = 10

    def draw_elements(self):
        player = pygame.draw.rect(game_window,red,[game.player_x,game.player_y,15,15])



    def move(self):
        if key[pygame.K_RIGHT]:
            game.player_x +=1

        if key[pygame.K_LEFT]:
            game.player_x -=1

game = game()


while run:
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
    game_window.fill((255,255,255))
    
    pygame.display.update()