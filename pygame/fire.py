import pygame
import sys

WIDTH, HEIGHT = 1600, 600
FPS = 60
PIXEL_SIZE=4
COLORS = ['black', 'red', 'orange', 'yellow', 'white']
COLOR_STEPS=9
FIRE_SIZE=10
FIRE_WIDTH=WIDTH/FIRE_SIZE
FIRE_HEIGHT=HEIGHT/FIRE_SIZE

class Fire:
    def __init__(self, app):
        self.app = app
        self.palette = self.get_palette()

    def draw_fire(self):
        for i in range(len(FIRE_WIDTH)):
            print(i)

    def draw_square(self):
        pygame.draw.rect(self.app.screen, COLORS[2], (10,10, PIXEL_SIZE,\
                                                      PIXEL_SIZE))

    def get_palette(self):
        palette = [(0,0,0)]
        for i, color in enumerate(COLORS[:-1]):
            c1, c2 = color, COLORS[i + 1]
            for step in range(COLOR_STEPS):
                c = pygame.Color(c1).lerp(c2, (step + 0.5)/COLOR_STEPS)
                palette.append(c)
        return palette

    def draw_palette(self):
        pal_size=10
        for i in range(len(self.palette)):
            pygame.draw.rect(self.app.screen, self.palette[i],
                             (i*pal_size,HEIGHT/2,pal_size,pal_size))

class App:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fire = Fire(self)
        
    def update(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS {self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        #self.fire.draw_palette()
        self.fire.draw_fire()
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
    
