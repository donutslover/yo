from pygame import*
from random import*
import pygame
import time

height = 640
width = 800


fenetre = display.set_mode((width,height))
display.set_caption("Madela's Donuts")

init()
map = image.load('Ciel_bleu.jpg')

#les spritesheets
perso0 = image.load('3.png')
perso1 = image.load('4.png')
perso2 = image.load('1.png')
perso3 = image.load('2.png')
perso = [perso0,perso1,perso2,perso3]

#les objets etc
donut = [image.load('Donut1.png'),image.load('Donut2.png'),image.load('playbutton1.png')]
playbutton = [image.load('playbutton1.png'),image.load('playbutton2.png')]
title = image.load("Madea's Donut.png" )

#On associe les touches aux images
imageSprite = {K_UP:[perso[1]],
               K_LEFT:[perso[2]],
               K_DOWN:[perso[0]],
               K_RIGHT:[perso[3]],}
 
#paramètres de départ
jouer = True
engaged = False
index_img = 0
clock = pygame.time.Clock()
vitesse = 0.6
direction = K_UP
chance = 0

#sons
 #intro
pygame.mixer.music.load('Gaiety in the golden age.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(0,0,9000)

#title
titx,tity = 5,height/4

#bouton
size = pygame.Surface.get_size(playbutton[0])
button_l = size[0]
button_h = size[1]
xPb,yPb = (width/2) - button_l/2 ,height*(2/3) - 60 

#donut
size = pygame.Surface.get_size(donut[0])
donut_l = size[0]
donut_h = size[1]


#bandeau
beandeau_l = size[0]
beandeau_h = size[1]
xB,yB = 0, yPb + (button_h - beandeau_h)/2


#affichage de départ
def start_screen():
    fenetre.blit(map,(0,0))
    fenetre.blit(playbutton[0],(xPb,yPb))
    fenetre.blit(title,(titx,tity))
    display.flip()
start_screen()
#game screen
def game_screen():
    fenetre.blit(map,(0,0))
    fenetre.blit(imageSprite[direction][index_img],(xPlayer,yPlayer))

#donut
XDonut1,XDonut2,XDonut3 = randint(5,width - donut_l - 5),randint(5,width - donut_l - 5),randint(5,width - donut_l - 5) 
YDonut1,YDonut2,YDonut3 = -donut_h,-donut_h,-donut_h

#player
size = pygame.Surface.get_size(perso[0])
player_l = size[0]
player_h = size[1]

y_lim = (height - player_h) - 20

xPlayer,yPlayer = (width/2) - player_l/2,y_lim
 
#les fonctions du jeu
    #fonction pour déplacer le perso
def deplacementPerso():
    global xPlayer,yPlayer,direction,index_img
    if k[K_LEFT]: 
        direction = K_LEFT
        if xPlayer <= 5:
            xPlayer = xPlayer 
        else:
            xPlayer = xPlayer - vitesse
    elif k[K_RIGHT]:
        direction = K_RIGHT
        if xPlayer >= (width-55):
            xPlayer = xPlayer
        else:
            xPlayer = xPlayer + k[K_RIGHT]*vitesse
    elif k[K_DOWN]:
        direction = K_DOWN
        if yPlayer >= y_lim:
            yPlayer = yPlayer
        else:
            yPlayer = yPlayer + k[K_DOWN]*vitesse
    else:
        direction = K_UP

#fonction défilement
    #positions donut niveau 1 de difficulté
def positions_à_Lvl1():
    global YDonut1,YDonut2,XDonut1,XDonut2,chance
    c = 0.7
    if chance != 1:
        chance = randint(1,20)
    yellow_donut = chance == 1

    #Donut 1
    if YDonut1 < height:
        YDonut1 += c
    else:
        YDonut1 = -donut_h
        XDonut1 = randint(5,width - donut_l - 5)
        chance = 0

    #Donut 2
    if YDonut2 < height:
        YDonut2 += c
    else:
        YDonut2 = -donut_h
        XDonut2 = randint(5,width - donut_l - 5)
        chance = 0


    if yellow_donut:
        fenetre.blit(donut[0],(XDonut1,YDonut1))
        fenetre.blit(donut[2],(XDonut2,YDonut2))
    else:
        fenetre.blit(donut[0],(XDonut1,YDonut1))
        fenetre.blit(donut[1],(XDonut2,YDonut2))
    
    
#boucle jeu             
while jouer:
    for events in event.get():
        if events.type == QUIT:
            quit()

    if engaged:
        k = key.get_pressed()
        game_screen()
        positions_à_Lvl1()
        deplacementPerso()
        display.flip()

    else:
        if events.type == pygame.MOUSEMOTION:
            coordonnes = pygame.mouse.get_pos()
            if xPb < coordonnes[0] < (xPb + button_l):
                if yPb < coordonnes[1] < (yPb + button_h):
                    fenetre.blit(playbutton[1],(xPb,yPb))
            else:
                start_screen()
            display.flip()

        if events.type == pygame.MOUSEBUTTONDOWN:
            coordonnes = pygame.mouse.get_pos()
            if xPb < coordonnes[0] < (xPb + button_l):
                    if yPb < coordonnes[1] < (yPb + button_h):
                        engaged = True

clock.tick(25)
