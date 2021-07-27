import pygame

pygame.init()

size = widht, height = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Example')

clock = pygame.time.Clock()  # fps

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (0, 0, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
colors = [WHITE, BLUE, RED, GREEN]
color = WHITE
pi = 3.14

done = True
while done:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, WHITE,
                        [[150, 10], [180, 50],
                         [90, 90], [30, 30]])
    pygame.draw.polygon(screen, WHITE,
                        [[250, 110], [280, 150],
                         [190, 190], [130, 130]])


    clock.tick(100)
    pygame.display.update()

pygame.quit()
