import pygame

d_width, d_heigh = 600, 600
map_size=8
w_tile = d_width / map_size
h_tile = d_heigh / map_size
tile_size = int(d_width / map_size)
matrix = [["#","#","#","#","#","#","#","#"],
          ["#","","#","","","","","#"],
          ["#","","#","","","#","#","#"],
          ["#","","","","","","","#"],
          ["#","","","","","","","#"],
          ["#","","","","","#","#","#"],
          ["#","","","","","","","#"],
          ["#","#","#","#","#","#","#","#"]]

pygame.init()

screen = pygame.display.set_mode((d_width, d_heigh))
clock = pygame.time.Clock()
pygame.display.set_caption("test1")

def draw_map():
    print("drawing map")
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            pygame.draw.rect(screen,(0,255,0) if matrix[row][col] == '#'
                             else (100,100,100), (col * tile_size, row *
                                                     tile_size, tile_size-2,
                                                     tile_size-2))

def draw_player(player_size=8,pos_x=d_width/2, pos_y=d_heigh/2):
    player = pygame.draw.circle(screen, (255,255,0), (pos_x, pos_y),player_size)
    return player


p_pos_x, p_pos_y = draw_player().x, draw_player().y
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print("pressing key")
            if event.key == pygame.K_a:
                p_pos_x = p_pos_x-1
            if event.key == pygame.K_s:
                p_pos_y = p_pos_y+1
            if event.key == pygame.K_d:
                p_pos_x = p_pos_x+1
            if event.key == pygame.K_w:
                p_pos_y = p_pos_y-1
    draw_map()
    draw_player(8,p_pos_x, p_pos_y)
    print(p_pos_x, p_pos_y)
    pygame.display.flip()
    clock.tick(30)
