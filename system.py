import pygame

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

game_over = False
start_game = True
death_player = False

