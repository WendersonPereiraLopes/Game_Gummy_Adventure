import pygame.image
import sys

from pygame import Surface, Rect
from pygame.font import Font
from code.Menu import Menu
from code.ProxyDB import ProxyDB
from code.Const import WIN_WIDTH, WIN_HEIGHT, C_BLACK
class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/Score_end_game.png')
        self.scale = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=0, top=0)
    
    def run(self):
        pygame.mixer.music.load('asset/Score_end_gameSound.mp3')
        pygame.mixer.music.play(-1)
        proxy_db = ProxyDB('DBscore.db')
        list_score = proxy_db.retrive_top5()
        proxy_db.close()
        while True:
            self.window.blit(source=self.scale, dest=self.rect)
            self.score_text(50, 'TOP 5 SCORE',  C_BLACK, ((WIN_WIDTH / 2 ), 100))
            y_offset = 0
            for player_score in list_score:
                texto_formatado = f"Score: {player_score[1]} | Data: {player_score[2]}"
                self.score_text(30, texto_formatado, C_BLACK, (WIN_WIDTH / 2, 250 + y_offset))
                y_offset += 40  # Adjust the gap between items
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return Menu(self.window)

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
            text_font: Font = pygame.font.SysFont(name='Roboto', size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(center=text_center_pos)
            self.window.blit(source=text_surf, dest=text_rect)