import pygame.image

from abc import ABC, abstractmethod

class Entity(ABC):
    
    def __init__(self, name:str, position:tuple, scale:tuple):
        self.name = name
        self.surf = pygame.image.load('asset/' + name + '.png') 
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.scale = pygame.transform.scale(self.surf, size=scale)

        