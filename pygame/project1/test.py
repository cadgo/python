import pygame
import sys
HERO_STATE="walking"
MAIN_DIR='/home/carlos/git/UltimatePygameIntro'
GRAVITY=-20
game_gravity=GRAVITY
snail_speed = 5
background = pygame.image.load('Sky.png')
width, height = background.get_size()
print(f'width {width} heigth {height}')
floor = pygame.image.load('ground.png')
screen = pygame.display.set_mode((width, height + floor.get_height()))
s = floor.get_height()

clock = pygame.time.Clock()

floor_surface=floor.convert_alpha()
background_surface=background.convert_alpha()
main_char=pygame.image.load(MAIN_DIR+'/graphics/Player/player_walk_1.png').convert_alpha()
rect_gamer = main_char.get_rect(midbottom=(100,height))

snail=pygame.image.load(MAIN_DIR+'/graphics/snail/snail1.png').convert_alpha()
rect_snail = snail.get_rect(midbottom=(width-100, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                HERO_STATE="jumping"

    rect_snail.x -=snail_speed
    if HERO_STATE == "jumping":
        rect_gamer.y += game_gravity
        game_gravity+=1
        print(f"jumping {game_gravity}")
        _,s = main_char.get_size()
        if rect_gamer.y > height-s:
            rect_gamer.y = height-s
            game_gravity= GRAVITY
            HERO_STATE="walking"
    screen.blit(background_surface, (0,0))
    screen.blit(floor_surface,(0,height))
    screen.blit(main_char,rect_gamer )
    screen.blit(snail, rect_snail)
    pygame.display.flip()
    clock.tick(60)
