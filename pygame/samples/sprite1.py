import pygame

pygame.init()

WIDTH, HEIGTH = 800, 800 
clock=pygame.time.Clock()
isRunning = True
screen=pygame.display.set_mode((WIDTH, HEIGTH))

class Square(pygame.sprite.Sprite):
    def __init__(self, color,pos_x, pos_y):
        super().__init__()
        self.surface = pygame.Surface((pos_x, pos_y))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.center = (pos_x, pos_y)
        

sqg = pygame.sprite.Group()

sqg.add(Square("crimson", 500,500))

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    screen.fill("cyan")

    sqg.update()
    sqg.draw(screen)

    pygame.display.flip()

pygame.quit()
