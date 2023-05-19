import pygame
import math

d_width, d_heigh = 600, 600
map_size=8
w_tile = d_width / map_size
h_tile = d_heigh / map_size
char_speed = 5
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
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            pygame.draw.rect(screen,(0,255,0) if matrix[row][col] == '#'
                             else (100,100,100), (col * tile_size, row *
                                                     tile_size, tile_size-2,
                                                     tile_size-2))

def draw_player(player_size=8,pos_x=d_width/2, pos_y=d_heigh/2):
    player = pygame.draw.circle(screen, (255,255,0), (pos_x, pos_y),player_size)
    return player

def CM_Position(pos_y, pos_x):
    col = int(pos_x / tile_size)
    line = int(pos_y / tile_size)
    print(f"line {line} columna {col}")
    return line, col

p_pos_x, p_pos_y = draw_player().x, draw_player().y
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                cml, cmc = CM_Position(p_pos_y, p_pos_x-10)
                if not matrix[cml][cmc] == "#":
                    p_pos_x = p_pos_x-char_speed
            if event.key == pygame.K_s:
                cml, cmc = CM_Position(p_pos_y+10, p_pos_x)
                if not matrix[cml][cmc] == "#":
                    p_pos_y = p_pos_y+char_speed
            if event.key == pygame.K_d:
                cml, cmc = CM_Position(p_pos_y, p_pos_x+10)
                if not matrix[cml][cmc] == "#":
                    p_pos_x = p_pos_x+char_speed
            if event.key == pygame.K_w:
                cml, cmc = CM_Position(p_pos_y-10, p_pos_x)
                if not matrix[cml][cmc] == "#":
                    p_pos_y = p_pos_y-char_speed
    draw_map()
    draw_player(8,p_pos_x, p_pos_y)
    pygame.display.flip()
    clock.tick(30)
