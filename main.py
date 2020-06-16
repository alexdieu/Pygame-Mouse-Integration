import pygame
import pygame as pg

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("World War III")
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('cursor.png')


pg.init()
screen = pg.display.set_mode((800, 600))
screen_rect = screen.get_rect()
print(screen_rect)
clock = pg.time.Clock()
running = True
while running:
    clock.tick(10)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    pos = pg.mouse.get_pos()
    print(pos)
    pg.display.update()
    screen.blit(playerImg, (pos))
    
running = True
while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False

    player()
    pygame.display.update()
