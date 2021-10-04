import pygame
from pygame.draw import *
from random import randint

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))    

def hair():
    x = randint(1, 5)
    if x == 1 :
        haircolor = (210, 150, 220)
    if x ==2 :
        haircolor = (230, 230, 150)
    if x ==3 :
        haircolor = (180, 240, 220)
    if x==4 :
        haircolor = (210, 70, 230)
    if x==5 :
        haircolor = (210, 220, 80)
    return(haircolor)
    

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill((50, 210, 250))


circle(screen, (255, 255, 0), (490, 60), 100)

rect(screen, (50, 255, 50), (0, 300, 500, 400))
rect(screen, (255, 255, 255), (65, 300, 20, 200))
ellipse(screen, (0, 110, 0), (-50, 200, 250, 130))
ellipse(screen, (0, 110, 0), (10, 300, 130, 100))
ellipse(screen, (0, 110, 0), (30, 80, 90, 150))

ellipse(screen, (220, 150, 255), (150, 260, 40, 30))
ellipse(screen, (220, 150, 255), (-15, 250, 40, 35))
ellipse(screen, (220, 150, 255), (90, 350, 35, 40))
ellipse(screen, (220, 150, 255), (60, 110, 45, 40))

ellipse(screen, (255, 255, 255), (200, 500, 200, 100))
rect(screen, (255, 255, 255), (340, 450, 50, 100))
ellipse(screen, (255, 255, 255), (340, 430, 60, 40))
ellipse(screen, (255, 255, 255), (350, 445, 80, 30))

rect(screen, (255, 255, 255), (220, 550, 13, 110))
rect(screen, (255, 255, 255), (250, 550, 16, 100))
rect(screen, (255, 255, 255), (335, 560, 18, 110))
rect(screen, (255, 255, 255), (360, 550, 14, 105))


circle(screen, (160, 90, 180), (380, 450), 10)
circle(screen, (0, 0, 0), (382, 450), 4)
draw_ellipse_angle(screen, (255, 255, 255), [372, 443, 10, 4], -30, 0)

polygon(screen, (220, 150, 255), ((370, 432), (378, 434), (382, 370)))



for i in range(17):
    ellipse(screen, hair(), (randint(320, 340), randint(420, 500), randint(20, 40), randint(10, 20)))
for i in range(17):
    ellipse(screen, hair(), (randint(270, 340), randint(490, 510), randint(40, 50), randint(10, 15)))
for i in range(10):
    ellipse(screen, hair(), (randint(190, 200), randint(530, 570), randint(25, 35), randint(10, 15)))
for i in range(10):
    ellipse(screen, hair(), (randint(180, 195), randint(565, 600), randint(30, 35), randint(10, 15)))
for i in range(10):
    ellipse(screen, hair(), (randint(190, 200), randint(600, 630), randint(30, 35), randint(10, 15)))
for i in range(10):
    ellipse(screen, hair(), (randint(170, 190), randint(600, 630), randint(20, 35), randint(10, 15)))
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
