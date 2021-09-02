# Sprite classes for platform game
import pygame as pg
from settings import *

vec = pg.math.Vector2

bg = pg.image.load("transferir.jpg")
bg = pg.transform.scale(bg, (WIDTH, HEIGHT))

plat = pg.image.load("plataforma.png")

lav = pg.image.load("lava.png")

plyr = pg.image.load("smile.jpg")
plyr = pg.transform.scale(plyr, (30, 40))


class BackGround1(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = bg
        self.rect = self.image.get_rect()
        self.cntr = 0
        self.pos = 0

    def update(self):
        self.cntr += 1
        self.pos = self.cntr % HEIGHT
        self.pos = self.pos - HEIGHT
        if self.cntr >= HEIGHT:
            self.cntr = 0
        self.rect.y = self.cntr


class BackGround2(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = bg
        self.rect = self.image.get_rect()
        self.cntr = 0
        self.pos = 0

    def update(self):
        self.cntr += 1
        self.pos = self.cntr % HEIGHT
        self.pos = self.pos - HEIGHT
        if self.cntr >= HEIGHT:
            self.cntr = 0
        self.rect.y = self.pos


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = plyr
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image = pg.transform.scale(plat, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        print("(x,y) = (", x, " , ", y, ")")

    # tentativas pra fazer de acordo com a ultima plataforma
    def showY(self):
        return self.rect.y

    def showX(self):
        return self.rect.x

    # def print_Position(self):
    #     print("(x,y) = (", self.x, " , ", self.y, ")")


class Lava(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def redraw(self, x, y, w, h):
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def showY(self):
        return self.rect.y
