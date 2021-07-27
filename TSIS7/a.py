import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()
size = width, height = (1000, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sin and Cos")
screen.fill(WHITE)

FPS = 0
FPS_CLOCK = pygame.time.Clock()

pygame.draw.rect(screen, BLACK, (80, 50, 840, 600), 3)
pygame.draw.line(screen, BLACK, (80, height / 2), (width - 80, height / 2), 3)
pygame.draw.line(screen, BLACK, (width / 2, 50), (width / 2, height - 50), 3)

for i in range(2, 15):
    font = pygame.font.Font(None, 20)
    if i % 2 == 0 and i != 8:
        pygame.draw.aaline(screen, BLACK, (125 * i / 2, 50), (125 * i / 2, height - 50))
        text = font.render(str(int(i / 2 - 4)) + "п", True, True)
        screen.blit(text, (125 * i / 2 - 7, height - 40))
        if i - 8 < 0:
            font2 = pygame.font.SysFont('TimesNewRoman', 15, True, True)
            text2 = font2.render(str(int(i / 2 - 4)), True, True)
            screen.blit(text2, (125 * i / 2 + 8 - (i - 2) * 15, height / 2 + 50))
    elif i == 8:
        text = font.render(str(int(i / 2 - 4)), True, True)
        font2 = pygame.font.SysFont('TimesNewRoman', 25, True, True)
        text2 = font2.render("x", True, True)
        screen.blit(text, (125 * i / 2 - 2, height - 40))
        screen.blit(text2, (125 * i / 2 - 5, height - 25))
    else:
        text = font.render(str(i - 8) + "п/2", True, True)
        pygame.draw.aaline(screen, BLACK, (125 * i / 2, 50), (125 * i / 2, 50 + 15))
        pygame.draw.aaline(screen, BLACK, (125 * i / 2, height - 15 - 50), (125 * i / 2, height - 50))
        screen.blit(text, (125 * i / 2 - 12, height - 40))

    if i < 14:
        for j in range(1, 4):
            if j % 2 == 0:
                h = 10
            else:
                h = 5
            pygame.draw.aaline(screen, BLACK, (125 * i / 2 + 125 * j / 8, 50), (125 * i / 2 + 125 * j / 8, 50 + h))
            pygame.draw.aaline(screen, BLACK, (125 * i / 2 + 125 * j / 8, height - h - 50),
                               (125 * i / 2 + 125 * j / 8, height - 50))

g = 10
for i in range(1, 10):
    g -= 1
    pygame.draw.aaline(screen, BLACK, (80, 70 * i), (width - 80, 70 * i))
    font = pygame.font.Font(None, 20)
    l = (g - 5) / 4
    text = font.render(str('%.2f' % l), True, True)
    screen.blit(text, (45, 70 * i - 5))
    if i < 9:
        for j in range(1, 4):
            if j % 2 == 0:
                h = 10
            else:
                h = 5
            pygame.draw.aaline(screen, BLACK, (80, 70 * i + 70 * j / 4), (80 + h, 70 * i + 70 * j / 4))
            pygame.draw.aaline(screen, BLACK, (width - 80 - h, 70 * i + 70 * j / 4), (width - 80, 70 * i + 70 * j / 4))

pygame.draw.line(screen, WHITE, (125 * 5, 71), (125 * 5, 139), 3)
font = pygame.font.Font(None, 25)
text = font.render("sin x", True, True)
text2 = font.render("cos x", True, True)
screen.blit(text, (125 * 5 - 35, 70 + 5))
pygame.draw.line(screen, RED, (125 * 5 + 15, 70 + 12), (125 * 5 + 65, 70 + 12), 2)
screen.blit(text2, (125 * 5 - 35, 70 + 30))
pygame.draw.line(screen, BLUE, (125 * 5 + 15, 70 + 37), (125 * 5 + 65, 70 + 37), 2)
for i in range(2, 4):
    pygame.draw.line(screen, WHITE, (125 * 5 + 15 * i, 70 + 37), (125 * 5 + 15 * i + 5, 70 + 37), 2)

x_cor = 125
dx = 1

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    if x_cor < width - 125:
        if x_cor % 5 == 0:
            pygame.draw.line(screen, WHITE, (x_cor, -1 * math.cos((x_cor - width / 2) / 40) * 280 + height / 2),
                             ((x_cor + dx), -1 * math.cos(((x_cor + dx) - width / 2) / 40) * 280 + height / 2), 3)
        else:
            pygame.draw.line(screen, BLUE, (x_cor, -1 * math.cos((x_cor - width / 2) / 40) * 280 + height / 2),
                             ((x_cor + dx), -1 * math.cos(((x_cor + dx) - width / 2) / 40) * 280 + height / 2), 3)

        pygame.draw.line(screen, RED, (x_cor, -1 * math.sin((x_cor - width / 2) / 40) * 280 + height / 2),
                         ((x_cor + dx), -1 * math.sin(((x_cor + dx) - width / 2) / 40) * 280 + height / 2), 3)

    x_cor += dx

    pygame.display.update()
    FPS_CLOCK.tick(FPS)
    # pygame.time.delay(30)

pygame.quit()
