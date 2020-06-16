import pygame
import pygame as pg

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Draw")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('cursor.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    pg.display.update()
    screen.blit(playerImg, (pos))

    pygame.display.update()
