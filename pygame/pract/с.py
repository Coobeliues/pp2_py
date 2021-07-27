import pygame
import random

pygame.init()

size = widht, height = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Example')

text_rot_deg = 1
clock = pygame.time.Clock()  # fps

rect_x = 50
rect_y = 50
rect_chang_x = 2
rect_chang_y = 2

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

    rect_x += rect_chang_x
    rect_y += rect_chang_y
    if rect_y > 450 or rect_y < 0:
        rect_chang_y *= -1
    if rect_x > 650 or rect_x < 0:
        rect_chang_x *= -1

    if keys[pygame.K_SPACE]:
        color = colors[random.randint(0, 3)]
    pygame.draw.rect(screen, color, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, (0, 0, 250), [rect_x + 5, rect_y + 5, 40, 40])
    pygame.draw.rect(screen, (250, 0, 0), [rect_x + 10, rect_y + 10, 30, 30])
    pygame.draw.rect(screen, (0, 250, 0), [rect_x + 15, rect_y + 15, 20, 20])
    pygame.draw.rect(screen, (100, 250, 60), [rect_x + 20, rect_y + 20, 10, 10])

    clock.tick(100)
    pygame.display.update()

pygame.quit()
