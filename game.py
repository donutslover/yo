from pygame import*
import pygame
from random import*

clock = pygame.time.Clock

run = True
width = 500
height = width

donut = image.load('Donut1.png')
fenetre = display.set_mode((width,height))

x = randint(5,width - 109)
y = -108
fenetre.blit(donut,(x,y))

def chute():
    global x,y
    if y < height:
        y += 0.2
    else:
        y = -108
        x = randint(5,width - 109)
    fenetre.blit(donut,(x,y))

while run:
    for events in event.get():
        if events.type == QUIT:
            quit()
    chute()
    display.flip()
clock.tick(25)

