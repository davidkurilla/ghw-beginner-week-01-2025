import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

color = RED

window = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

is_running = True
while is_running:

    pygame.draw.rect(window, color, player)

    key = pygame.key.get_pressed()

    if key[pygame.K_r] == True:
        window.fill(BLACK)

    if key[pygame.K_1] == True:
        color = RED

    if key[pygame.K_2] == True:
        color = GREEN

    if key[pygame.K_3] == True:
        color = BLUE

    if key[pygame.K_4] == True:
        color = BLACK

    if key[pygame.K_5] == True:
        color = WHITE

    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    
    if key[pygame.K_d] == True:
        player.move_ip(1, 0)
    
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)

    if key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()