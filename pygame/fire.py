import pygame
from pygame import gfxdraw
import sys
from random import randint

WIDTH, HEIGHT = 1200, 600
FPS = 60
PIXEL_SIZE=4
COLORS = ['black', 'red', 'orange', 'yellow', 'white']
COLOR_STEPS=9
FIRE_WIDTH=WIDTH
FIRE_HEIGHT=HEIGHT//PIXEL_SIZE

class Fire:
    def __init__(self, app):
        self.app = app
        self.palette = self.get_palette()
        self.fire_array=self.get_fire_array()
        print(self.fire_array)


    def draw_fire(self):
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.palette[color_index]
                    gfxdraw.box(self.app.screen, (x*PIXEL_SIZE, y*PIXEL_SIZE,
                                                  PIXEL_SIZE-1,
                                                  PIXEL_SIZE-1),color)


    def do_fire(self):
        for x in range(FIRE_WIDTH):
            for y in range(1,FIRE_HEIGHT):
                color_index = self.fire_array[y][x]
                if color_index:
                    rnd = randint(0,3)
                    self.fire_array[y-1][(x - rnd + 1)%FIRE_WIDTH]= color_index - rnd % 2
                else:
                    self.fire_array[y - 1][x] = 0
    
    def update(self):
        self.do_fire()
        print(self.fire_array)

    def draw_square(self):
        pygame.draw.rect(self.app.screen, COLORS[2], (10,10, PIXEL_SIZE,\
                                                      PIXEL_SIZE))
    def get_fire_array(self):
        fire = [[0 for x in range(FIRE_WIDTH)] for i in range(FIRE_HEIGHT)]
        print(len(self.palette)-1)
        for i in range(FIRE_WIDTH):
            fire[FIRE_HEIGHT-1][i]=len(self.palette)-1
        return fire

    def init_fire1(self):
        factor  = randint(0,3)
        lenp = len(self.palette)
        for col in range(int(FIRE_WIDTH/PIXEL_SIZE)):
            for x in range(lenp):
                pygame.draw.rect(self.app.screen,(self.palette[lenp-1-x-factor
                                                               % FIRE_WIDTH]),\
                                (col*PIXEL_SIZE,HEIGHT-(PIXEL_SIZE*x)*factor,PIXEL_SIZE-1,PIXEL_SIZE*factor-1))

    def init_fire2(self):
        lenp = len(self.palette)
        for x in range(lenp):
                #print(self.palette[lenp-1-x])
            pygame.draw.rect(self.app.screen,(self.palette[lenp-1-x]),(0,HEIGHT-(PIXEL_SIZE*x),
                                                                 PIXEL_SIZE-1,PIXEL_SIZE-1))


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
                             (i*pal_size,HEIGHT/2-100,pal_size,pal_size))

class App:
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.fire = Fire(self)
        
    def update(self):
        self.clock.tick(FPS)
        pygame.display.set_caption(f'FPS {self.clock.get_fps() :.1f}')
        self.fire.update()

    def draw(self):
        self.screen.fill('black')
        self.fire.draw_palette()
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
    
