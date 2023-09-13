import pygame
import sys
FPS=30
WIDTH, HEIGHT = 1600, 1200
PIC_FOLDER='/home/carlos/git/python/pygame/craftpix-net-612081-free-scrolling-city-backgrounds-pixel-art/1back/1/Night/'
BACKGROUNDS=[PIC_FOLDER+'2.png', PIC_FOLDER+'3.png', PIC_FOLDER+'5.png']

class bc_picture():
    def __init__(self, picture):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.width=self.picture.get_size()[0]
        self.height=self.picture.get_size()[1]
    
class App():
    def __init__(self):
        self.isRunning=True
        pygame.display.init()
        self.game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.Clock = pygame.time.Clock()
        self.background=self.set_background(PIC_FOLDER+'1.png')
        self.movingfg = self.set_moving_fg(BACKGROUNDS)
        self.start=False

    def set_background(self,b_image):
        b=pygame.image.load(b_image).convert_alpha()
        background=pygame.transform.smoothscale(b, self.game_screen.get_size())
        return background

    def set_moving_fg(self, list_pictures):
        bcs = []
        for pics in list_pictures:
            bcs.append(bc_picture(pics))    
            print(f'large {bcs[0].width}, heigth {bcs[0].height}')
        return bcs

    def update(self):
        self.Clock.tick(FPS)
        c_fps = self.Clock.get_fps()
        pygame.display.set_caption(f'FPS: {c_fps : .1f}')
        
    def start_buildings(self):
        padding=30
        mid=HEIGHT//2
        prev='' 
        for index, pic in enumerate(self.movingfg):
            if index == 0:
                rect=pygame.Rect(pic.width*index,mid-pic.height, pic.width,pic.height)
                prev = rect
                self.game_screen.blit(pic.picture,rect)
                print(f'{rect.left} {rect.right}')
            else:
                rect=pygame.Rect(prev.right+padding, mid-pic.height,
                                 pic.width, pic.height)
                self.game_screen.blit(pic.picture, rect)
                prev = rect

    def draw(self):
        #self.game_screen.blit(self.background,(0,0))
        self.start_buildings()
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print('key down')
                self.update()
                self.draw()

if __name__ == "__main__":
    game = App()
    game.run()
