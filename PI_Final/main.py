from variaveis import *
import pygame as pg
import random
from settings import *
from sprites import *
from os import path


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        self.cont = 0
        # tentativas pra fazer de acordo com a ultima plataforma

    # self.lastplat = Platform(175, 100, 50, 20)

    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def print_LAVA(self):
        if self.alt_lava == HEIGHT - LAVA_EASY:
            print("Altura da lava = ", self.alt_lava, "(LAVA_EASY)")
        if self.alt_lava == HEIGHT - LAVA_MEDIUM_LOW:
            print("Altura da lava = ", self.alt_lava, "(LAVA_MEDIUM_LOW)")
        if self.alt_lava == HEIGHT - LAVA_MEDIUM_HIGH:
            print("Altura da lava = ", self.alt_lava, "(LAVA_MEDIUM_HIGH)")
        if self.alt_lava == HEIGHT - LAVA_HARD:
            print("Altura da lava = ", self.alt_lava, "(LAVA_HARD)")

    def print_EnemyChance(self):
        if self.enemy_chance == 0:
            print("A cada plataforma que aparecer, há uma chance de 10% de ela conter um inimigo.")
        if self.enemy_chance == 1:
            print("A cada plataforma que aparecer, há uma chance de 15% de ela conter um inimigo.")
        if self.enemy_chance == 2:
            print("A cada plataforma que aparecer, há uma chance de 25% de ela conter um inimigo.")
        if self.enemy_chance == 3:
            print("A cada plataforma que aparecer, há uma chance de 50% de ela conter um inimigo.")


    def new(self):
        # start a new game
        # altura max da lava 0, HEIGHT - 300, WIDTH, 300
        print("------Novo Jogo------")
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.background1 = BackGround1(self)
        self.all_sprites.add(self.background1)
        self.background2 = BackGround2(self)
        self.all_sprites.add(self.background2)
        self.lavas = pg.sprite.Group()
        self.lava = Lava(0, HEIGHT - 40, WIDTH, 1000)
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.lava)
        self.level1 = discret((10, 15, 20, 25))
        print("level1 = ", self.level1)
        self.level2 = discret((45, 50, 55, 60))
        print("level2 = ", self.level2)
        self.width_plataforms = PL_LVL0
        self.enemy_chance = 1
        self.print_EnemyChance()
        # self.alt_lava = discret((HEIGHT - 100, HEIGHT - 70, HEIGHT - 50, HEIGHT - 40))
        self.alt_lava = discret(
            (HEIGHT - LAVA_HARD, HEIGHT - LAVA_MEDIUM_HIGH, HEIGHT - LAVA_MEDIUM_LOW, HEIGHT - LAVA_EASY))
        self.print_LAVA()
        self.c_level1 = False
        self.c_level2 = False
        #  self.plataforms.add
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def change_level(self):
        if self.score == self.level1 and self.c_level1 == False:
            print("entrou level1")
            self.width_plataforms = PL_LVL1
            self.enemy_chance = 2
            # self.alt_lava = discret((HEIGHT - 120, HEIGHT - 110, HEIGHT - 100, HEIGHT - 90))
            self.alt_lava = discret(
                (HEIGHT - LAVA_HARD, HEIGHT - LAVA_EASY, HEIGHT - LAVA_MEDIUM_HIGH, HEIGHT - LAVA_MEDIUM_LOW))
            self.print_LAVA()
            self.print_EnemyChance()
            self.c_level1 = True
        if self.score == self.level2 and self.c_level2 == False:
            print("entrou level2")
            self.width_plataforms = PL_LVL2
            self.enemy_chance = 3
            # self.alt_lava = discret((HEIGHT - 150, HEIGHT - 130, HEIGHT - 130, HEIGHT - 120))
            self.alt_lava = discret(
                (HEIGHT - LAVA_EASY, HEIGHT - LAVA_MEDIUM_LOW, HEIGHT - LAVA_MEDIUM_HIGH, HEIGHT - LAVA_HARD))
            self.print_LAVA()
            self.print_EnemyChance()
            self.c_level2 = True

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.change_level()
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        # if player reaches top 1/2 of screen
        if self.player.rect.top <= HEIGHT / 2:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= self.lava.showY() - 20:
                    plat.kill()
                    self.score += 1
                    self.cont = 0
            for lav in self.lavas:
                lav.rect.y += abs(self.player.vel.y)

        # Die!
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        hitsl = pg.sprite.spritecollide(self.player, self.lavas, False)
        if len(self.platforms) >= self.lava.showY() - 20 or len(self.platforms) == 0 or hitsl:
            self.playing = False

        self.lava.redraw(0, self.alt_lava, WIDTH, 1000)
        # self.cont = self.score + 1

        # change lava
        # if self.score % 3 == 0 and self.score >= self.cont:
        if (self.score == 0):
            self.lava.redraw(0, HEIGHT - 40, WIDTH, 1000)
            # else:
            #     alt = discret((HEIGHT - 100, HEIGHT - 70, HEIGHT - 50, HEIGHT - 40))
            #     self.lava.redraw(0, alt, WIDTH, 1000)
            #     self.cont = self.score + 1

        # spawn new platforms to keep same average number
        while len(self.platforms) < 4:
            width = discret(self.width_plataforms)
            p = Platform(define_platafromX(),
                         define_plataformY(30, 60, 30),
                         width, OBJECT_HEIGHT)
            make_enemy = discret((0, 1, 2, 3))
            if make_enemy == self.enemy_chance:
                wi = p.showX()
                wf = p.showX() + width
                enemy_width = discret((width / 2, width / 3, width / 4, width / 5))
                enemy_x = enemy_X(wi, wf)
                pl = Lava(enemy_x, p.showY() - OBJECT_HEIGHT, enemy_width, enemy_Y(50, 20))
                # enemy_x = enemy_X(0, WIDTH)
                # enemy_y = enemy_Y(1, 50)
                # enemy_width = discret((10, 20, 30, 40))
                # pl = Lava(enemy_x, enemy_y, enemy_width, 20)
                self.lavas.add(pl)
                self.all_sprites.add(pl)

            self.platforms.add(p)
            # self.lavas.add(pl)
            self.all_sprites.add(p)
            # self.all_sprites.add(pl)
        # tentativas pra fazer de acordo com a ultima plataforma
        # self.lastplat = p


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, Space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("NEW HIGH SCORE!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
