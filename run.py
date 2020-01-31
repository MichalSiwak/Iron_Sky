import random
import pygame
import sys

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Iron Sky")

fps = 60
width = 1280  # 0
height = 680  # 0
fpsClock = pygame.time.Clock()
font = pygame.font.SysFont('Nimbus Mono L', 40)
start_font = pygame.font.SysFont('Nimbus Mono L', 60)
screen = pygame.display.get_surface()
screen_size = pygame.display.set_mode((width, height))
backgrounds_img = pygame.image.load("img/backgrounds.png").convert()
game_over_img = pygame.image.load("img/game_over.png").convert()

player_x = 550
player_y = 550
enemy_y = -40

explosion_animation = [pygame.image.load("img/Explosion1_1.png"), pygame.image.load("img/Explosion1_2.png"),
                       pygame.image.load("img/Explosion1_3.png"), pygame.image.load("img/Explosion1_4.png"),
                       pygame.image.load("img/Explosion1_5.png"), pygame.image.load("img/Explosion1_6.png"),
                       pygame.image.load("img/Explosion1_7.png"), pygame.image.load("img/Explosion1_8.png"),
                       pygame.image.load("img/Explosion1_9.png"),
                       pygame.image.load("img/Explosion1_10.png")]

emeny_1 =[pygame.image.load("img/Enemy1a.png"), pygame.image.load("img/Enemy1b.png"), pygame.image.load("img/Enemy1c.png"),
pygame.image.load("img/Enemy1d.png"), pygame.image.load("img/Enemy1e.png")]

emeny_2 =[pygame.image.load("img/Enemy2a.png"), pygame.image.load("img/Enemy2b.png"), pygame.image.load("img/Enemy2c.png"),
pygame.image.load("img/Enemy2d.png"), pygame.image.load("img/Enemy2e.png")]

emeny_3 =[pygame.image.load("img/Enemy3a.png"), pygame.image.load("img/Enemy3b.png"), pygame.image.load("img/Enemy3c.png"),
pygame.image.load("img/Enemy3d.png"), pygame.image.load("img/Enemy3e.png")]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/player_1.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 15
            self.image = pygame.image.load("img/space_ship_r.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            if self.rect.x >= 1140:
                self.rect.x = 1140
        if keys[pygame.K_LEFT]:
            self.rect.x -= 15
            self.image = pygame.image.load("img/space_ship_l.png")
            self.image = pygame.transform.scale(self.image, (80, 80))
            if self.rect.x <= 0:
                self.rect.x = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += 15
            if self.rect.y >= 550:
                self.rect.y = 550
        if keys[pygame.K_UP]:
            self.rect.y -= 15
            if self.rect.y <= 0:
                self.rect.y = 0


        if keys[pygame.K_RIGHT] == False and keys[pygame.K_LEFT] == False:
            self.image = pygame.image.load("img/player_1.png")
            self.image = pygame.transform.scale(self.image, (80, 80))

    def shoots(self):
        bullet = Bullet(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet)
        bullets.add(bullet)
        pygame.mixer_music.load("sounds/shoot.wav")
        pygame.mixer_music.play(0)

    def power_shoots(self):
        bullet_l = BulletL(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet_l)
        bullets.add(bullet_l)
        bullet_r = BulletR(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet_r)
        bullets.add(bullet_r)
        bullet = Bullet(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet)
        bullets.add(bullet)
        pygame.mixer_music.load("sounds/shoot.wav")
        pygame.mixer_music.play(0)

    def power_shoots_2(self):
        bullet_l = BulletL(self.rect.x + 26, self.rect.y- 25)
        all_sprite.add(bullet_l)
        bullets.add(bullet_l)
        bullet_l = BulletML(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet_l)
        bullets.add(bullet_l)
        bullet_r = BulletR(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet_r)
        bullets.add(bullet_r)
        bullet_r = BulletMR(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet_r)
        bullets.add(bullet_r)
        bullet = Bullet(self.rect.x + 26, self.rect.y - 25)
        all_sprite.add(bullet)
        bullets.add(bullet)
        pygame.mixer_music.load("sounds/shoot.wav")
        pygame.mixer_music.play(0)


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(emeny_1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(10, 1200)
        self.rect.y = enemy_y
        self.speedy = random.randint(2, 3)
        self.speedx = random.randint(-5, 5)

    def shoots(self):
        enemy_bullet = EnemShoots(self.rect.x, self.rect.y)
        all_sprite.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y >= 680:
            self.rect.x = random.randint(10, 1200)
            self.rect.y = enemy_y
            self.speedy = random.randint(2, 3)
            self.speedx = random.randint(-4, 4)

        if self.rect.y == random.randint(0, height):
            enemy.shoots()


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(emeny_2)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(12, 1200)
        self.rect.y = enemy_y
        self.speedy = random.randint(3, 4)
        self.speedx = random.randint(-3, 3)

    def shoots(self):
        enemy_bullet = EnemShoots(self.rect.x, self.rect.y)
        all_sprite.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y >= 680:
            self.rect.x = random.randint(10, 1200)
            self.rect.y = -40
            self.speedy = random.randint(3, 4)
            self.speedx = random.randint(-3, 3)
        if self.rect.y == random.randint(0, height):
            enemy.shoots()



class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(emeny_3)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(12, 1200)
        self.rect.y = enemy_y
        self.speedy = random.randint(4, 5)
        self.speedx = random.randint(-3, 3)

    def shoots(self):
        enemy_bullet = EnemShoots(self.rect.x, self.rect.y)
        all_sprite.add(enemy_bullet)
        enemy_bullets.add(enemy_bullet)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y >= 680:
            self.rect.x = random.randint(10, 1200)
            self.rect.y = -40
            self.speedy = random.randint(4, 5)
            self.speedx = random.randint(-3, 3)
        if self.rect.y == random.randint(0, height):
            enemy.shoots()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fire_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = - 8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.kill()


class BulletL(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fire_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -8
        self.speedx = -2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()


class BulletR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fire_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -8
        self.speedx = 2

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()


class BulletML(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fire_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -8
        self.speedx = -1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()


class BulletMR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/fire_1.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -8
        self.speedx = 1

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.x < 0:
            self.kill()


class Explotions(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_animation[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 40

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_animation):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_animation[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Shields(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bolt.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(12, 1200)
        self.rect.y = - 200
        self.speedy = 3
        self.speedx = 0


    def update(self):
        self.rect.y += self.speedy
        if self.rect.y >= 900:
            self.rect.x = random.randint(10, 1200)
            self.rect.y = -200
            self.speedy = 3
            self.speedx = 0


class WeaponUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/waepon_power.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(12, 1200)
        self.rect.y = - 400
        self.speedy = 2
        self.speedx = 0


    def update(self):
        self.rect.y += self.speedy
        if self.rect.y >= 900:
            self.rect.x = random.randint(10, 1200)
            self.rect.y = -400
            self.speedy = 2
            self.speedx = 0


class EnemShoots(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load("img/enemy_bolts.png")
        self.image_orig = pygame.transform.scale(self.image_orig, (26, 26))
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        self.radius = 40
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2
        self.speedx = random.randint(-3, 3)
        self.rot = 0
        self.rot_speed = 10
        self.last_update = pygame.time.get_ticks()


    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        self.rotate()
        if width > self.rect.x < 0 or height < self.rect.y:
            self.kill()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 20:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.image_orig, self.rot)

def show_go_screen():
    start_game_txt = start_font.render(f'Naciśnij "T" aby rozpocząć nową grę', 1, (255, 255, 255), 'alfa')
    screen_size.blit(start_game_txt, (width / 5, height / 4))
    pygame.display.flip()
    game = True
    pygame.mixer_music.load("sounds/game_sound.wav")
    pygame.mixer_music.play(0)
    while game:
        fpsClock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_t:
                    game = False


def game_over_screen():
    end_game_txt = start_font.render(f'Naciśnij "T" aby rozpocząć nową grę', 1, (255, 255, 255), 'alfa')
    screen_size.blit(end_game_txt, (width / 5, 100))
    screen_size.blit(game_over_img, (220, 250))
    end_score = start_font.render(f'Twój wynik: {score}', 1, (255, 255, 255), 'alfa')
    screen_size.blit(end_score, (width / 3, 150))
    pygame.display.flip()
    game = True
    pygame.mixer_music.load("sounds/game_sound.wav")
    pygame.mixer_music.play(0)
    while game:
        fpsClock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_t:
                    game = False


def death_screen():
    death_txt = start_font.render(f'Naciśnij "T" aby kontynuować', 1, (255, 255, 255), 'alfa')
    screen_size.blit(death_txt, (340, 300))
    your_live = start_font.render(f'Życia: {live}', 1, (255, 255, 255), 'alfa')
    screen_size.blit(your_live, (560, 210))
    pygame.display.flip()
    pygame.mixer_music.load("sounds/game_sound.wav")
    pygame.mixer_music.play(0)
    death_player = True
    while death_player:
        fpsClock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_t:
                    death_player = False


game_over = False
start_game = True
death_player = False

while True:
    screen_size.blit(backgrounds_img, (0, 0))

    if start_game:
        show_go_screen()
        power = 0
        all_sprite = pygame.sprite.Group()
        power_up = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        waepons = pygame.sprite.Group()
        enemy_bullets = pygame.sprite.Group()
        player = Player()
        all_sprite.add(player)
        score = 0
        shield = 5
        live = 3
        for i in range(8):
            enemy = random.choice([Enemy1(), Enemy2(), Enemy3()])
            enemys.add(enemy)


        shield_up = Shields()
        all_sprite.add(shield_up)
        power_up.add(shield_up)

        waepon_up = WeaponUp()
        all_sprite.add(waepon_up)
        waepons.add(waepon_up)
        start_game = False

    if game_over:
        game_over_screen()
        power = 0
        all_sprite = pygame.sprite.Group()
        power_up = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        waepons = pygame.sprite.Group()
        enemy_bullets = pygame.sprite.Group()
        player = Player()
        all_sprite.add(player)
        score = 0
        shield = 5
        live = 3
        for i in range(8):
            enemy = random.choice([Enemy1(), Enemy2(), Enemy3()])
            enemys.add(enemy)

        shield_up = Shields()
        all_sprite.add(shield_up)
        power_up.add(shield_up)

        waepon_up = WeaponUp()
        all_sprite.add(waepon_up)
        waepons.add(waepon_up)
        game_over = False
        death_player = False

    if death_player:
        death_screen()
        power = 0
        all_sprite = pygame.sprite.Group()
        power_up = pygame.sprite.Group()
        enemys = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        waepons = pygame.sprite.Group()
        enemy_bullets = pygame.sprite.Group()
        player = Player()
        all_sprite.add(player)
        shield = 5
        live = live
        for i in range(8):
            enemy = random.choice([Enemy1(), Enemy2(), Enemy3()])
            enemys.add(enemy)

        shield_up = Shields()
        all_sprite.add(shield_up)
        power_up.add(shield_up)

        waepon_up = WeaponUp()
        all_sprite.add(waepon_up)
        waepons.add(waepon_up)
        death_player = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_SPACE:
                if power == 0:
                    player.shoots()
                elif power == 1:
                    player.power_shoots()
                else:
                    player.power_shoots_2()

    hits = pygame.sprite.spritecollide(player, enemys, True)
    if hits:
        pygame.mixer_music.load("sounds/explodebg.wav")
        pygame.mixer_music.play(0)
        shield -= 1
        power -= 1
        if power < 0:
            power = 0

        if shield < 0:
            live -= 1
            shield = 5
            death_player = True
            if live == 0:
                game_over = True

    for hit in hits:
        # enemy = Enemy1()
        enemy = random.choice([Enemy1(), Enemy2(), Enemy3()])
        all_sprite.add(enemy)
        expl = Explotions(hit.rect.center)
        all_sprite.add(expl)
        enemys.add(enemy)

    hits = pygame.sprite.groupcollide(bullets, enemys, True, True)
    if hits:
        pygame.mixer_music.load("sounds/explodebg.wav")
        pygame.mixer_music.play(0)
        score += 1
        if score % 50 == 0:
            live += 1
            pygame.mixer_music.load("sounds/liveup.wav")
            pygame.mixer_music.play(0)

    for hit in hits:
        # enemy = Enemy1()
        enemy = random.choice([Enemy1(), Enemy2(), Enemy3()])
        expl = Explotions(hit.rect.center)
        all_sprite.add(expl)
        all_sprite.add(enemy)
        enemys.add(enemy)

    hits = pygame.sprite.spritecollide(player, power_up, True)
    if hits:
        pygame.mixer_music.load("sounds/shield_up.wav")
        pygame.mixer_music.play(0)
        shield += 1

    for hit in hits:
        shield_up = Shields()
        all_sprite.add(shield_up)
        power_up.add(shield_up)

    hits = pygame.sprite.spritecollide(player, waepons, True)
    if hits:
        pygame.mixer_music.load("sounds/speedup.wav")
        pygame.mixer_music.play(0)
        power += 1
        if power > 2:
            power = 2


    for hit in hits:
        waepon_up = WeaponUp()
        all_sprite.add(waepon_up)
        waepons.add(waepon_up)


    hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
    if hits:
        pygame.mixer_music.load("sounds/explodebg.wav")
        pygame.mixer_music.play(0)
        shield -= 1
        power -= 1
        if power < 0:
            power = 0

        if shield < 0:
            live -= 1
            shield = 5
            death_player = True
            if live == 0:
                game_over = True

        for hit in hits:
            expl = Explotions(hit.rect.center)
            all_sprite.add(expl)


    your_score = font.render(f'Wynik: {score} Panczerz: {shield} Życia: {live}', 1, (255, 255, 255), 'alfa')
    screen_size.blit(your_score, (0, 0))

    enemys.draw(screen_size)
    all_sprite.draw(screen_size)
    power_up.draw(screen_size)
    waepons.draw(screen_size)
    enemy_bullets.draw(screen_size)
    pygame.display.flip()
    all_sprite.update()
    enemys.update()
    power_up.update()
    waepons.update()
    enemy_bullets.update()
    fpsClock.tick(fps)
