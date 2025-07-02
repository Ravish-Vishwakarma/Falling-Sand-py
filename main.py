import pygame
import sys

pygame.init()

window_s = (500,500)
screen = pygame.display.set_mode(window_s)
pygame.display.set_caption("Falling Sand Simulation")
matrix = [[0 for i in range(window_s[0])] for j in range(window_s[1])]

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))


    for y in range(window_s[1]-2,-1,-1):
         for x in range(window_s[0]):
              if(matrix[y][x] == 1):
                   if matrix[y+1][x] == 0:
                        matrix[y][x] = 0
                        matrix[y+1][x] = 1
                #    if matrix[y][x+1] == 0:
                #         matrix[y][x] = 0
                #         matrix[y][x+1] = 1
        


    for y in range(window_s[1]):
            for x in range(window_s[0]):
                if matrix[y][x] == 1:
                    screen.set_at((x, y), (0, 0, 0)) 


    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        if(0<= mx < window_s[0] and 0<= my < window_s[1]):
            matrix[my][mx] = 1

    # if pygame.mouse.get_pressed()[0]:
    #     mx, my = pygame.mouse.get_pos()
    #     brush_size = 2  # Makes a 5x5 area
    #     for dy in range(-brush_size, brush_size + 1):
    #         for dx in range(-brush_size, brush_size + 1):
    #             nx, ny = mx + dx, my + dy
    #             if 0 <= nx < window_s[0] and 0 <= ny < window_s[1]:
    #                 matrix[ny][nx] = 1


    pygame.display.update()

pygame.quit()
sys.exit()



# # ----------------------------------------------------------------------------------
# import pygame
# import sys

# pygame.init()

# window_s = (500, 500)
# screen = pygame.display.set_mode(window_s)
# pygame.display.set_caption("Falling Sand Simulation")
# matrix = [[0 for _ in range(window_s[0])] for _ in range(window_s[1])]

# clock = pygame.time.Clock()
# running = True

# while running:
#     clock.tick(120)  # Increased FPS for smoother simulation

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((255, 255, 255))

#     # Make sand fall faster by falling multiple pixels per frame
#     fall_distance = 3
#     for y in range(window_s[1] - 2, -1, -1):
#         for x in range(window_s[0]):
#             if matrix[y][x] == 1:
#                 for i in range(1, fall_distance + 1):
#                     if y + i >= window_s[1] or matrix[y + i][x] != 0:
#                         i -= 1
#                         break
#                 if i > 0:
#                     matrix[y][x] = 0
#                     matrix[y + i][x] = 1

#     # Draw pixels
#     for y in range(window_s[1]):
#         for x in range(window_s[0]):
#             if matrix[y][x] == 1:
#                 screen.set_at((x, y), (0, 0, 0))

#     # Add sand with left mouse click
#     if pygame.mouse.get_pressed()[0]:
#         mx, my = pygame.mouse.get_pos()
#         if 0 <= mx < window_s[0] and 0 <= my < window_s[1]:
#             matrix[my][mx] = 1

#     pygame.display.update()

# pygame.quit()
# sys.exit()
