import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((230, 230, 230))

circle(screen, (255, 255, 0), (300, 300), 100)
circle(screen, (0, 0, 0), (300, 300), 100, 2)

circle(screen, (255, 0, 0), (250, 270), 20)
circle(screen, (0, 0, 0), (250, 270), 20, 2)

circle(screen, (255, 0, 0), (350, 270), 15)
circle(screen, (0, 0, 0), (350, 270), 15, 2)

circle(screen, (0, 0, 0), (350, 270), 8)
circle(screen, (0, 0, 0), (250, 270), 12)

rect(screen, (0, 0, 0), (250, 340, 100, 15))

polygon(screen, (0, 0, 0), ((196, 202), (190, 212), (280, 264), (286, 254)))
polygon(screen, (0, 0, 0), ((327, 252), (330, 261), (400, 237), (397, 228)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
