import pygame.image
import sys
import random

from pygame import Surface, Rect
from pygame.font import Font
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.Enemy import Enemy
from code.Const import WIN_HEIGHT, WIN_WIDTH, C_WHITE, EVENT_ENEMY, SPAWN_TIMER

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.timeout = 60000
        self.entity_list:list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIMER)
    
        
    def run(self):
        pygame.mixer.music.load('asset/LevelSound.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.scale, dest=ent.rect) 
                ent.move()
                if isinstance(ent, (Enemy)):
                   shoot = ent.shoot()
                   if shoot is not None:
                        self.entity_list.append(shoot) 
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            
            #validation de time for end game 
            if self.timeout > 0:
                 self.timeout -= 1

                    
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}', C_WHITE, (70, 10))
            self.level_text(14, f'FPS: {clock.get_fps() :.0f}', C_WHITE, (30, WIN_HEIGHT - 35))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name='Roboto', size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)