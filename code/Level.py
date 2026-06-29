import pygame.image

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Const import WIN_HEIGHT, WIN_WIDTH

class Level:

    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list:list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))

    def run(self):
        pygame.mixer.music.load('asset/LevelSound.mp3')
        pygame.mixer.music.play(-1)
        while True:
          for ent in self.entity_list:
            self.window.blit(source=ent.scale, dest=ent.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()