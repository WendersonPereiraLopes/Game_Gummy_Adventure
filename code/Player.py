import pygame.key

from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT

class Player(Entity):
    
    def __init__(self, name, position, scale):
        super().__init__(name, position, scale)
        self.is_jumping = False
        self.vel_y = 0
        self.jump_force = -12  # Força do pulo (negativo para ir para cima)
        self.gravity = 0.8

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH - 40:
            self.rect.centerx += ENTITY_SPEED[self.name]


         # 2. Lógica do Pulo (Início)
         # Supondo que 500 é o chão da sua tela (ajuste conforme seu jogo)
        ground_level = 380
    
        if pressed_key[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.vel_y = self.jump_force

        # 3. Gravidade e Movimento Vertical
        if self.is_jumping:
            self.rect.centery += self.vel_y
            self.vel_y += self.gravity  # A gravidade diminui a subida e aumenta a queda

        # Colisão com o chão
        if self.rect.bottom >= ground_level:
            self.rect.bottom = ground_level
            self.is_jumping = False
            self.vel_y = 0