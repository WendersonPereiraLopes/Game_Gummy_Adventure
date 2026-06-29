import pygame

# C
C_BLACK = (0, 0, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255,255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'player': 3,
    'enemy1': 1,
    'enemy2': 2,
    'missel_enemy1': 3,
    'missel_enemy2': 4


}
ENTITY_SHOT_DELAY ={
    'enemy1': 50,
    'enemy2': 100
}


# M
MENU_OPTION = (
                'New Game',
                'Score',
                'Exit'
)

# S
SPAWN_TIMER = 4000
# W
WIN_WIDTH = 800
WIN_HEIGHT = 456