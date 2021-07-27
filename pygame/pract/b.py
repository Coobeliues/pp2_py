import pygame

pygame.init()

size = widht, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Example')

pi = 3.14
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.fill((255, 255, 255))

    #       line
    pygame.draw.line(screen, (0, 0, 0), [0, 0], [100, 100], 5)
    for i in range(0, 100, 10):
        pygame.draw.line(screen, (250, 0, 0), [0, 10 + i], [100, 110 + i], 3)
    #       rectangle
    pygame.draw.rect(screen, (0, 0, 250), [100, 50, 150, 150], 1)
    #       ellipse
    pygame.draw.ellipse(screen, (0, 250, 0), [110, 60, 130, 130], 2)
    #       arc
    pygame.draw.arc(screen, (30, 60, 90), [50, 200, 250, 50], 0, pi / 2, 2)
    pygame.draw.arc(screen, (90, 60, 90), [50, 200, 250, 50], pi / 2, pi, 2)
    pygame.draw.arc(screen, (30, 60, 30), [50, 200, 250, 50], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, (200, 60, 90), [50, 200, 250, 50], 3 * pi / 2, 2 * pi, 2)
    #       text
    font = pygame.font.Font(None, 25)
    txt1 = font.render('Ernar', True, (0, 0, 250))  # сглаживание
    txt2 = font.render('Ernar', False, (0, 0, 250))
    screen.blit(txt1, (300, 300))
    screen.blit(txt2, (300, 320))
    #       text rotate
    font = pygame.font.SysFont("TimesNewRoman", 25, True, True)
    text1 = font.render('Ernar', True, (0, 0, 250))  # сглаживание
    text2 = font.render('Ernar', False, (0, 0, 250))
    text1 = pygame.transform.rotate(text1, 180)
    text2 = pygame.transform.rotate(text2, 180)
    screen.blit(text1, (300, 340))
    screen.blit(text2, (300, 360))

    pygame.display.flip()

pygame.quit()
