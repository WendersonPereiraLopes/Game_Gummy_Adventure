import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.Const import *

class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/MenuBg.png')
        self.scale = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
         menu_option = 0
         pygame.mixer.music.load('asset/MenuSound.mp3')
         pygame.mixer.music.play(-1)
         while True:
            self.window.blit(source=self.scale, dest=self.rect)
            self.menu_text(50, 'Ice', C_YELLOW, ((WIN_WIDTH / 2), 100))
            self.menu_text(60, 'Adventure',  C_YELLOW, ((WIN_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(40, MENU_OPTION[i],  C_WHITE, ((WIN_WIDTH / 2), 250 + 50 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i],  C_YELLOW, ((WIN_WIDTH / 2), 250 + 50 * i))

            pygame.display.flip()

            # All events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # DONW KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=  1
                        else:
                            menu_option = 0
                
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -=  1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: # Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name='Roboto', size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)
