import pygame

# C
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255,255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'player': 3,
    'player_shot': 2,
    'enemy1': 1,
    'enemy2': 2,
    'missel_enemy1': 3,
    'missel_enemy2': 4


}
ENTITY_SHOT_DELAY ={
    'enemy1': 50,
    'enemy2': 100,
    'player': 20
}

ENTITY_HEALTH = {
    'aguaBg': 999,
    'ArvoreBg': 999,
    'Block01Bg': 999,
    'Block02Bg': 999,
    'Block03Bg': 999,
    'enemy1': 50,
    'enemy2': 70,
    'LevelBg': 999,
    'missel_enemy1': 1,
    'missel_enemy2': 1,
    'plataforma01': 999,
    'plataforma02': 999,
    'plataforma03': 999,
    'player_shot': 1,
    'player': 400,
    'ponteBg': 999
}
ENTITY_DAMEGE ={
    'aguaBg': 0,
    'ArvoreBg': 0,
    'Block01Bg': 0,
    'Block02Bg': 0,
    'Block03Bg': 0,
    'enemy1': 1,
    'enemy2': 1,
    'LevelBg': 0,
    'missel_enemy1': 35,
    'missel_enemy2': 40,
    'plataforma01': 0,
    'plataforma02': 0,
    'plataforma03': 0,
    'player_shot': 30,
    'player': 1,
    'ponteBg': 0
}

ENTITY_SCORE = {
    'aguaBg': 0,
    'ArvoreBg': 0,
    'Block01Bg': 0,
    'Block02Bg': 0,
    'Block03Bg': 0,
    'enemy1': 100,
    'enemy2': 150,
    'LevelBg': 0,
    'missel_enemy1': 0,
    'missel_enemy2': 0,
    'plataforma01': 0,
    'plataforma02': 0,
    'plataforma03': 0,
    'player_shot': 0,
    'player': 0,
    'ponteBg': 0
}

# M
MENU_OPTION = (
                'New Game',
                'Score',
                'Control',
                'Exit'
)

# S
SPAWN_TIMER = 4000

# W
WIN_WIDTH = 800
WIN_HEIGHT = 456