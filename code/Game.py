import pygame

from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.image.load('asset/Icon.png')
        self.icon = pygame.display.set_icon(self.surf) # Adicona Icone no jogo
        self.title = pygame.display.set_caption('Ice Adventure') # Altera o Título da Janela

    def run(self):
         
         while True:
            menu = Menu(self.window)
            menu.run()
        
           