import pygame.key

from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    
    def __init__(self, name, position, scale):
        super().__init__(name, position, scale)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 100:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT - 75:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH - 40:
            self.rect.centerx += ENTITY_SPEED[self.name]