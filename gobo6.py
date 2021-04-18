#this is the cource code of my gobo dash 6 python version

import pygame
import random



randomspeed = random.randint(2,4)
randomspeed2 = random.randint(3,6)
randomspeed3 = random.randint(1,3)
randomspeed4 = random.randint(2,4)
# print(randomspeed)
# print(randomspeed2)
# print(randomspeed3)
print(randomspeed4)
pygame.mixer.init()

pygame.mixer.music.load('so long.mp3')



pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen_width = 1200
screen_height = 600
game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Gobo Dash (6)")

stage = 0
clock = pygame.time.Clock()

# game specfic variables
player_x = 36
player_y = 583
player_width = 15
player_height = 15
vel_y = 15
upd_x = 221
upd_y = 100
jump = False
upd_y_2 = 120
upd_y_3 = -200
upd_y_4 = -310
upd_y_5 = -340
upd_y_6 = -297
upd_y_7 = -360
upd_y_8 = -200
speed = 5


font = pygame.font.SysFont(None,55)
def text_screen(text,clolor,x,y):
    screen_text = font.render(text,None,clolor)
    game_window.blit(screen_text,[x,y])

def collide(to_colide):
    if p.colliderect(to_colide):
            reset()
    




run = True
jump = False


def reset():
    global player_y
    global player_x
    global vel_y
    vel_y = 15
    jump = False
    player_x = 36
    player_y = 583    


   
            

    

    
    


clock = pygame.time.Clock()

pygame.mixer.music.play()
while run:
    clock.tick(60)



    for event in pygame.event.get():
        key = pygame.key.get_pressed()


    game_window.fill(white)
    text_screen('level ' + str(stage),red,0,0)
    p = pygame.draw.rect(game_window,black,[player_x,player_y,player_width,player_height])
    ob = pygame.draw.rect(game_window, red, [241, 570, 9, 40])
    gate = pygame.draw.rect(game_window,red,[1189,550, 10,50])

    pygame.time.delay(15)




    if key[pygame.K_RIGHT]:
        if not player_x>=1200:
            player_x = player_x+speed


    if key[pygame.K_LEFT]:
        if not player_x<=0:
            player_x = player_x-speed



    if jump is False and key[pygame.K_UP]:
        jump = True

    if jump:
        player_y = player_y - vel_y
        vel_y = vel_y-1
        if vel_y <-15:
            jump = False
            vel_y = 15

    if p.colliderect(gate):

        player_x = 31
        player_y = 583
        stage = stage+1

    if player_y == 600 or player_y > 600:
        player_x = 31
        player_y = 583

    if key[pygame.K_t]:
        stage = stage+1

    if p.colliderect(ob):
        player_x = 31
        player_y = 583

    if key[pygame.K_END]:
        break

    if stage == 1 or stage>1:
        ob2 = pygame.draw.rect(game_window, red, [200, 570, 10, 40])

    if not jump:
        if key[pygame.K_r]:
            player_y = 583

    if event.type == pygame.QUIT:
        break

    if key[pygame.K_SPACE]:
        print(f"x is",{player_x},'y is',{player_y})

    if stage>=1:
        if p.colliderect(ob2):
            player_x = 31
            player_y = 583

    if stage == 2 or stage>2:
        ob3 = pygame.draw.rect(game_window,red,[152,570,10,40])

    if stage>=2:
        if p.colliderect(ob3):
            player_x = 31
            player_y = 583

    if stage == 3 or stage>3:
        ob4 = pygame.draw.rect(game_window,red,[282,570,10,40])

    if stage>=3:
        if p.colliderect(ob4):
            player_x=31
            player_y=583

    if stage == 4 or stage>4:
        ob5 = pygame.draw.rect(game_window,red,[322,570,10,40])

    if stage>=4:
        if p.colliderect(ob5):
            player_x = 31
            player_y = 583



    if stage>=5:
        ob6 = pygame.draw.rect(game_window,red,[360,570,10,40])

    if stage>=5:
        if p.colliderect(ob6):
            player_x = 36
            player_y = 583

    if stage>=6:
        ob7 = pygame.draw.rect(game_window,red,[397,570,10,40])

    if stage>=6:
        if p.colliderect(ob7):
            player_x = 36
            player_y = 583



    if stage>=7:
       ob8 = pygame.draw.rect(game_window,red,[437,570,10,40])

    if stage>=7:
        if p.colliderect(ob8):
            player_x = 36
            player_y = 583

    if stage>=8:
        ob9 = pygame.draw.rect(game_window,red,[472,570,10,40])

    if stage>=8:
        if p.colliderect(ob9):
            player_x = 36
            player_y = 583

    if stage>=9:
       ob10 = pygame.draw.rect(game_window,red,[512,570,10,40])

    if stage>=9:
        if p.colliderect(ob10):
            player_x = 36
            player_y = 583




    if stage>=10:
        ob11 = pygame.draw.rect(game_window,red,[547,570,10,40])


    if stage>=10:
        if p.colliderect(ob11):
            player_x = 36
            player_y = 583

    if stage>=11:
        ob12 = pygame.draw.rect(game_window,red,[586,570,10,40])


    if stage>=11:
        if p.colliderect(ob12):
            player_x = 36
            player_y = 583

    if stage>=12:
        ob13 = pygame.draw.rect(game_window,red,[626,570,10,40])

    if stage>12:
        if p.colliderect(ob13):
            player_x = 36
            player_y = 583


    if stage>=13:
        ob14 = pygame.draw.rect(game_window,red,[668,570,10,40])

    if stage>=13:
        if p.colliderect(ob14):
            player_x = 36
            player_y = 583

    if stage>=14:
        ob15 = pygame.draw.rect(game_window,red,[706,570,10,40])

    if stage>=14:
        if p.colliderect(ob15):
            player_x = 36
            player_y = 583

    if stage>=15:
        ob16 = pygame.draw.rect(game_window,red,[741,570,10,40])

    if stage>=15:
        if p.colliderect(ob16):
            player_x = 36
            player_y = 583

    if stage>=16:
        ob17 = pygame.draw.rect(game_window,red,[776,570,10,40])

    if stage>=16:
        if p.colliderect(ob17):
            player_x = 36
            player_y = 583

    if stage>=17:
        ob18 = pygame.draw.rect(game_window,red,[816,570,10,40])

    if stage>=17:
        if p.colliderect(ob18):
            player_x = 36
            player_y = 583

    if stage>=18:
        # pass
        ob19 = pygame.draw.rect(game_window,red,[857,570,10,40])

    if stage>=18:
        if p.colliderect(ob19):
            player_x = 36
            player_y = 583

    if stage>=19:
        # pass
        ob20 = pygame.draw.rect(game_window,red,[899,570,10,40])
        # print('19')

    if stage>=19:
        if p.colliderect(ob20):
            player_x = 36
            player_y = 583

    if stage>=20:
        # pass
        ob21 = pygame.draw.rect(game_window,red,[940,570,10,40])

    if stage>=20:
        if p.colliderect(ob21):
            player_x = 36
            player_y = 583

    if stage>=21:
        # pass
        ob22 = pygame.draw.rect(game_window,red,[985,570,10,40])
        if p.colliderect(ob22):
            player_x = 36
            player_y = 583

    if stage>=22:
        ob23 = pygame.draw.rect(game_window,red,[1030,570,10,40])
        if p.colliderect(ob23):
            player_x = 36
            player_y = 583

    if stage>=23:
        upd_ob = pygame.draw.rect(game_window,red,[upd_x,upd_y,13,400])
        upd_y = upd_y+6

    if upd_y>=203:
        upd_y = -300


    if stage>=23:
        if p.colliderect(upd_ob):
            reset()

    if stage>=24:
        upd_ob1 = pygame.draw.rect(game_window,red,[171,upd_y_2,13,400])
        upd_y_2 = upd_y_2 + 4
            # print(upd_y_2)

    if upd_y_2>=200:
        upd_y_2 = -300

    if stage>=24:
        if p.colliderect(upd_ob1):
            reset()
       
    if stage>=25:
        upd_ob2 = pygame.draw.rect(game_window, red,[261,upd_y_3,13,400])
        upd_y_3 = upd_y_3+2.5
        if upd_y_3>200:
            upd_y_3 = -300
        
        
    if stage>=26:
        upd_ob3 = pygame.draw.rect(game_window,red,[300,upd_y_4,13,400])
        upd_y_4 +=3.4
        if upd_y_4 >=200:
            upd_y_4 = -306

        collide(upd_ob3)



    if stage>=27:
        upd_ob4 = pygame.draw.rect(game_window,red,[340,upd_y_5,13,400])
        upd_y_5 = upd_y_5+randomspeed

        if upd_y_5>=200:
            upd_y_5 = -340

        collide(upd_ob4)

    if stage>=28:
        upd_ob5 = pygame.draw.rect(game_window,red,[379,upd_y_6,13,400])
        upd_y_6+=randomspeed2

        if upd_y_6>=200:
            upd_y_6 = -297

        collide(upd_ob5)


    if stage>=29:
        upd_ob_6 = pygame.draw.rect(game_window,red,[412,upd_y_7,13,400])
        upd_y_7 += randomspeed3

        if upd_y_7 >=200:
            upd_y_7 = -360

        collide(upd_ob_6)

    if stage>=30:
        upd_ob_7 = pygame.draw.rect(game_window,red,[462,upd_y_8,13,400])
        upd_y_8 += randomspeed4

        if upd_y_8>=200:
            upd_y_8 = -230

        collide(upd_ob_7)



        


    if key[pygame.K_d]:
        player_x = 376            
        
    if stage>=25:    
        if p.colliderect(upd_ob2):
            reset()
            
            
            
    

        


    pygame.display.update()


print('exited the game')
