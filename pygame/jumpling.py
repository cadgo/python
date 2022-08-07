import pygame, sys
pygame.init()

clock = pygame.time.Clock()
screen_width,screen_high = 800,800
floor_position = screen_high - 200
faling=False
main_char_size=50
main_char_speed=15
isJumping=False
main_char_size = 50
main_char = pygame.Rect(screen_width/2,\
        floor_position-main_char_size,\
        main_char_size,main_char_size)
screen = pygame.display.set_mode((screen_width, screen_high))
surf = pygame.Surface((100,100))
surf.fill('Red')
isRunning=True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == ord('a')) and main_char.x > 0:
                print("moviendo izq x", main_char.x)
                main_char.x -= main_char_speed
            if (event.key == pygame.K_RIGHT or event.key == ord('d')) and main_char.x+main_char_size < screen_width:
                print("Moviendo derecha", main_char.x)
                main_char.x += main_char_speed
            if event.key == pygame.K_SPACE:
                isJumping=True

    if isJumping:
        if faling == False:
            main_char.y -= main_char_speed
            print(main_char.y)
            if main_char.y <= 100: faling=True; print("Faling")
        else:
            main_char.y += main_char_speed
            if main_char.y >= floor_position: faling=False; isJumping=False; main_char.y = floor_position - main_char_size
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),main_char)
    pygame.draw.line(screen, (64,64,64),
            (0,floor_position),(screen_width,floor_position),10)
    screen.blit(surf, (0,0))
    pygame.display.flip()
    clock.tick(60)
