import pygame
import math
import random
from pygame import mixer


pygame.init()  # The speed kept on increasing because this line code was missing

sw = 800
sh = 900

bg = pygame.image.load("Bulletspix/New BG2.png ")
turkey = pygame.image.load("Bulletspix/TURK Chara.png")
bullet1 = pygame.image.load("Bulletspix/BulletBall.png")
bullet2 = pygame.image.load("Bulletspix/BulletBall1.png")
bullet3 = pygame.image.load("Bulletspix/BulletBall2.png")

pygame.display.set_caption("Turkey run")
win = pygame.display.set_mode((sw, sh))
titlimg = pygame.image.load("Bulletspix/pixilart-drawing.png")
Scoreboared = pygame.image.load("Bulletspix/Boared.png")
Lifeboared = pygame.image.load("Bulletspix/Life board.png")

icon = pygame.image.load("Bulletspix/Defaturk.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
gameover = False
lives = 4
time = 120000

BGmusic = mixer.music.load("Bulletspix/1 Min Chill Guitar Hip Hop Beat Love Prod By The UM.mp3")
mixer.music.play(-1)


class Player(object):
    def __init__(self):
        self.img = turkey
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = sw // 2
        self.y = sh // 2
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, win):
        # win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnleft(self):
        self.angle += 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

    def turnright(self):
        self.angle -= 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

    def moveforward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

    def movedown(self):
        self.x -= self.cosine * 6
        self.y += self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)

        # looping border

    def updatelocation(self):
        if self.x > sw + 50:
            self.x = 0
        elif self.x < 0 + - self.w:
            self.x = sw
        elif self.y < - 50:
            self.y = sh
        elif self.y > sh + 50:
            self.y = 0


class Bullet(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.image = bullet1
        elif self.rank == 2:
            self.image = bullet2
        else:
            self.image = bullet3
        self.w = 15 * rank  # Bullet size of collission to the player
        self.h = 15 * rank
        self.ranPoint = random.choice([(random.randrange(0, sw - self.w), random.choice([-1 * self.h - 5, sh + 5])),
                                       (random.choice([-1 * self.w - 5, sw + 5]), random.randrange(0, sh - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < sw // 2:
            self.xdir = 8
        else:
            self.xdir = -8
        if self.y < sh // 2:
            self.ydir = 8
        else:
            self.ydir = -8
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


def GameWindow():
    win.blit(bg, (0, 0))

    win.blit(Scoreboared, (400, 825))
    win.blit(Lifeboared, (1, 800))
    font = pygame.font.Font("Gameplay.ttf", 20)
    font2 = pygame.font.Font("Gameplay.ttf", 40)
    Livestext = font.render("lives: " + str(lives), 1, (255, 0, 0))
    Time = font.render("Survive 2 min! : " + str(time), 1, (255, 0, 0))
    GameoverTxt = font2.render("GAME OVER Restart Game ", 1, (173, 216, 230))
    GameWin = font2.render("YOU WON!!! ", 1, (173, 216, 230))

    player.draw(win)
    for a in bullet:
        a.draw(win)

    if gameover:
        win.blit(GameoverTxt, (sw // 2 - GameoverTxt.get_width() // 2, sh // 2 - GameoverTxt.get_height() // 2))
    win.blit(Livestext, (75, 850))
    win.blit(titlimg, (225, -1))
    win.blit(Time, (420, 850))
    if time == -1:
        win.blit(GameWin, (sw // 3 - GameWin.get_width() // 100, sh // 3 - GameWin.get_height() // 3))
    pygame.display.update()


player = Player()
bullet = []
count = 0

run = True
while run:

    clock.tick(60)
    count += 1
    if not gameover:
        player.updatelocation()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turnleft()
        if keys[pygame.K_RIGHT]:
            player.turnright()
        if keys[pygame.K_UP]:
            player.moveforward()
        if keys[pygame.K_DOWN]:
            player.movedown()

        if count % 26 == 0:
            ran = random.choice([1, 1, 1, 2, 2, 3])
            bulletsound = mixer.Sound("Bulletspix/Realistic Gunshot Sound Effect.mp3")
            bulletsound.play()
            bullet.append(Bullet(ran))

        if time >= 0:
            time -= 1
        elif time == -1:
            gameover = True

    for a in bullet:
        a.x += a.xv
        a.y += a.yv
        # collision and bullet break
        if (player.x >= a.x and player.x <= a.x + a.w) or (
                player.x + player.w >= a.x and player.x + player.w <= a.x + a.w):
            if (player.y >= a.y and player.y <= a.y + a.h) or (
                    player.y + player.h >= a.y and player.y + player.h <= a.y + a.h):
                turkeysound = mixer.Sound("Bulletspix/Turkey Gobble Sound Effect.mp3")
                turkeysound.play()
                lives -= 1

                bullet.pop(bullet.index(a))
                break
        if lives <= 0:
            gameover = True
            #gamoversound = mixer.Sound("Bulletspix/Game Over Voice  Sound Effect HD.mp3")
            #gamoversound.play()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    GameWindow()
pygame.quit()
