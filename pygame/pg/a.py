import pygame

pygame.init()
win = pygame.display.set_mode((852, 480))
pygame.display.set_caption('Cubitos')

wL = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
      pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
      pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
wR = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
      pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
      pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
wT = [pygame.image.load('standing.png')]
bg = [pygame.image.load('bg.jpg')]

clock = pygame.time.Clock()


class snaryad:
    def __init__(self, x, y, rad, col, fac):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.fac = fac
        self.vel = 5 * fac

    def drw(self, win):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)


x = 0
y = 0
width = 64
height = 64
speed = 9

isjump = False
jumper = 10

left = False
right = False
animcnt = 0
lastMove = 'right'


def draww():
    global animcnt
    win.blit(bg[animcnt // 100], (0, 0))
    if animcnt + 1 >= 45:
        animcnt = 0

    if left:
        win.blit(wL[animcnt // 5], (x, y))
        animcnt += 1
    elif right:
        win.blit(wR[animcnt // 5], (x, y))
        animcnt += 1
    else:
        win.blit(wT[animcnt // 5], (x, y))
        animcnt += 1

    for bullet in bullets:
        bullet.drw(win)

    pygame.display.update()


run = True
bullets = []
while run:
    clock.tick(30)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if 852 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1

        if len(bullets) < 90:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 852 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animcnt = 0
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 480 - height - 9:
        y += speed

    if not isjump:
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumper >= -10:
            if jumper < 0 and y < 480 - height - 10:
                y += (jumper ** 2) / 3
            elif jumper >= 0 and y > 15:
                y -= (jumper ** 2) / 3
            jumper -= 1
        else:
            isjump = False
            jumper = 10
    draww()

pygame.quit()
