import pygame
import sys

WIDTH, HEIGHT = 600, 1200
FPS = 60
PIXEL_SIZE=4
COLORS = ['black', 'red', 'orange', 'yellow', 'white']

class Fire:
    def __init__(self, app):
        self.app = app

    def draw_square(self):
        pygame.draw.rect(self.app.screen, COLORS[2], (10,10, PIXEL_SIZE,\
                                                      PIXEL_SIZE))


class App:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        self.clock = pygame.time.Clock()
        self.fire = Fire(self)
        
    def update(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS {self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.fire.draw_square()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()

if __name__ == "__main__":
    fire = App()
    fire.run() 
    
