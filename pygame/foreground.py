import pygame
import sys
FPS=30
WIDTH, HEIGHT = 1600, 1200
PIC_FOLDER='/home/carlos/Downloads/backs/1/Night/'
BACKGROUNDS=[PIC_FOLDER+'2.png', PIC_FOLDER+'3.png', PIC_FOLDER+'5.png']

class bc_picture():
    def __init__(self, picture):
        self.picture = pygame.image.load(picture).convert_alpha()
        self.width=self.picture.get_size()[0]
        self.height=self.picture.get_size()[1]
        self.bc_rect = self.picture.get_rect(topleft=(self.width, self.height))
    
    def print_position(self,width, height):
        rect = self.picture.get_rect(topleft=(width, height))
        print(f'{rect.left} {rect.right} {rect.top} {rect.bottom}')

class App():
    def __init__(self):
        self.isRunning=True
        pygame.display.init()
        self.game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.Clock = pygame.time.Clock()
        self.background=self.set_background(PIC_FOLDER+'1.png')
        self.movingfg = self.set_moving_fg(BACKGROUNDS)

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
        
    def draw_floor_buildings2(self):
        padding=30
        mid = HEIGHT/2
        for index,pic in enumerate(self.movingfg):
            if index == 0:
                self.game_screen.blit(pic.picture, (pic.width*index,mid-pic.height))
            else:
                self.game_screen.blit(pic.picture,(pic.width*index+padding,mid-pic.height))
            pic.print_position(padding+pic.width*index,mid-pic.height)

    def draw_floor_buildings3(self):
        padding=30
        mid=HEIGHT//2
        
        for index, pic in enumerate(self.movingfg):
            rect = pic.picture.get_rect()
            print(f'{rect.left} {rect.right} {rect.top} {rect.bottom}')
            if index == 0:
                self.game_screen.blit(pic.picture, (0,mid-pic.height))
            else:
                self.game_screen.blit(pic.picture,(self.movingfg[index-1].width*index+padding*index,mid-pic.height))

    def draw_floor_buildings(self):
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
        self.game_screen.blit(self.background,(0,0))
        self.draw_floor_buildings()
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.update()
                self.draw()

if __name__ == "__main__":
    game = App()
    game.run()
