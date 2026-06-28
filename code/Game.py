import pygame

from code.Menu import Menu
from code.Level import Level
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.surf = pygame.image.load('asset/Icon.png')
        self.icon = pygame.display.set_icon(self.surf) # Adicona Icone no jogo
        self.title = pygame.display.set_caption('Gummy Adventure') # Altera o Título da Janela

    def run(self):
         
         while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window)
                level.run()
            elif menu_return == MENU_OPTION[1]:
                pass
            else:
                pygame.quit()
                quit

           