import pygame

pygame.init()

WIDTH = 900
HEIGHT = 500
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
win = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()


# variable library
player_x = 0
player_y = 0


def draw_player(x_pos, y_pos):
    player = pygame.draw.rect(win, white, [x_pos, y_pos, 30, 30])

    return player


running = True
while running:
    timer.tick(fps)
    win.fill(black)

    player = draw_player(player_x, player_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

