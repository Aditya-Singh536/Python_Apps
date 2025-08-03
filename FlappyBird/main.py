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
player_x = 225
player_y = 225


def draw_player(x_pos, y_pos):
    mouth = pygame.draw.circle(win, gray, [x_pos + 25, y_pos + 15], 12)
    player = pygame.draw.rect(win, white, [x_pos, y_pos, 30, 30], 0, 12)
    eye = pygame.draw.circle(win, black, [x_pos + 24, y_pos + 12], 5)
    jetpack = pygame.draw.rect(win, white, [x_pos - 20, y_pos, 18, 28], 3, 2)
    return mouth, player, eye, jetpack


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
