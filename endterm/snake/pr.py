from random import randrange
import pygame
import sys


s = input('choose level:"1, 2" ->    ')
pygame.init()
surface = pygame.display.set_mode((800, 800))
img = pygame.image.load('123.jpg').convert()
a2, b2, c2, d2 = [], [], [], []


def lvl():
    global a2, b2, c2, d2, surface, s
    a = 0
    if s == '1':
        reading_wall = open('level_1.txt', 'r')
        a = reading_wall.readlines()
    elif s == '2':
        reading_wall = open('level_2.txt', 'r')
        a = reading_wall.readlines()

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "#":
                pygame.draw.rect(surface, (0, 0, 255), (i * 40, j * 40, 40, 40))
                a2.append(i * 40)
                b2.append(j * 40)
                c2.append((i * 40, j * 40))
                # d2.append(40)


def mainer():
    pygame.display.init()
    global surface, img
    pygame.font.init()
    RES = 800
    SIZE = 40
    length = 1
    fps = 110

    x, y = 440, 400
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    snake = [(x, y)]

    dx, dy = 0, 0
    score = 0
    speed_count, snake_speed = 0.0, 4
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    # surface = pygame.display.set_mode([RES, RES])
    font_score = pygame.font.SysFont('TimesNewRoman', 26, True, True)
    font_end = pygame.font.SysFont('TimesNewRoman', 66, True, True)
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    done = True
    while done:

        # pos = pygame.mouse.get_pos()a
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

        surface.blit(img, (0, 0))
        # surface.fill((255, 255, 255))
        # drawing snake, apple
        lvl()
        [pygame.draw.rect(surface, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
        for i in range(len(a2)):
            if apple[0] == a2[i] and apple[1] == b2[i]:
                apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        pygame.draw.ellipse(surface, pygame.Color('red'), (apple[0], apple[1], SIZE, SIZE))
        for i in c2:
            if snake[-1] == i:
                render_end = font_end.render('GAME OVER!', True, pygame.Color('orange'))
                surface.blit(render_end, (RES // 2 - 200, RES // 3))
                pygame.display.flip()
                print("Your score: " + str(score))
                done = False
                break
        # show score
        render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
        surface.blit(render_score, (5, 5))
        # snake movement
        speed_count += 0.5
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]
        # eating food
        if snake[-1] == apple:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            length += 1
            score += 1
            if s == '2':
                snake_speed -= 2
            elif s == '1':
                snake_speed -= 3
            snake_speed = max(snake_speed, 4)
        # game over
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            render_end = font_end.render('GAME OVER!', True, pygame.Color('orange'))
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            print("Your score: " + str(score))
            break

        pygame.display.flip()
        pygame.display.update()
        clock.tick(fps)

        # controls
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True}
        elif key[pygame.K_s]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True}
        elif key[pygame.K_a]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False}
        elif key[pygame.K_d]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True}
    # pygame.quit()


def play_again():
    while True:
        answer = input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        else:
            return False


def main():
    while True:
        mainer()
        if not play_again():
            return


if __name__ == '__main__':
    main()
    sys.exit()
