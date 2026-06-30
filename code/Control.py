import pygame.image
import sys

from pygame import Surface, Rect
from pygame.font import Font
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_BLACK

class Control:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/MenuBg.png')
        self.scale = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        while True:
            self.window.blit(source=self.scale, dest=self.rect)
            self.control_text(60, 'Button',  C_BLACK, ((WIN_WIDTH / 2 ), 100))
            self.control_text(30, 'Esc   |  Back',  C_BLACK, ((WIN_WIDTH / 2), 150 + 10))
            self.control_text(30, '-->   |  Rigth',  C_BLACK, ((WIN_WIDTH / 2), 200 + 10))
            self.control_text(30, '<--   |  Left',  C_BLACK, ((WIN_WIDTH / 2), 250 + 10))
            self.control_text(30, 'Return   |  Enter',  C_BLACK, ((WIN_WIDTH / 2), 300 + 10))
            self.control_text(30, 'Jump  |  Space',  C_BLACK, ((WIN_WIDTH / 2), 350 + 10))
            self.control_text(30, 'Shoot  |  CTRL Left',  C_BLACK, ((WIN_WIDTH / 2), 400  + 10))


            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return Menu(self.window)
                    
    def control_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name='Roboto', size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)