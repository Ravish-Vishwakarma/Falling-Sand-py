import pygame
import sys

HEIGHT,WIDTH = (500,500)
pygame.init()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Here we go again!!")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((255,255,255))


    mclick = pygame.mouse.get_pressed()
    print(mclick)
    if mclick[0] == True:
        running = False


    pygame.display.update()
