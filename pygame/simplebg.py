import pygame
import sys

bgimage = '/home/carlos/backgronds/back1.jpg'
WIDTH, HEIGHT= 680,360
FPS = 30
pygame.display.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
clock.tick(FPS)
bg=pygame.image.load(bgimage).convert_alpha()
screen.blit(bg,(-5,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

            
