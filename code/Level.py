import pygame.image

from code.Const import WIN_HEIGHT, WIN_WIDTH

class Level:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/Level01Bg.png')
        self.plat_01 = pygame.image.load('asset/plataforma01Bg.png')
        self.plat_02 = pygame.image.load('asset/plataforma02Bg.png')
        self.plat_03 = pygame.image.load('asset/Plataforma03Bg.png')
        self.arv = pygame.image.load('asset/ArvoreBg.png')
        self.agua = pygame.image.load('asset/aguaBg.png')
        self.ponte = pygame.image.load('asset/ponteBg.png')
        self.block_01 = pygame.image.load('asset/Block01Bg.png')
        self.block_02 = pygame.image.load('asset/Block02Bg.png')
        self.block_03 = pygame.image.load('asset/Block03Bg.png')
       
        
        self.scale = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.scale_01 = pygame.transform.scale(self.plat_01, (200, 40))
        self.scale_02 = pygame.transform.scale(self.arv, (100, 120))
        self.scale_03 = pygame.transform.scale(self.plat_02, (150, 120))
        self.scale_04 = pygame.transform.scale(self.agua, (150, 120))
        self.scale_05 = pygame.transform.scale(self.plat_01, (400, 40))
        self.scale_06 = pygame.transform.scale(self.ponte, (150, 8))
        self.scale_07 = pygame.transform.scale(self.plat_03, (50, 100))
        self.scale_08 = pygame.transform.scale(self.block_01, (50, 50))
        self.scale_09 = pygame.transform.scale(self.block_02, (50, 50))
        self.scale_10 = pygame.transform.scale(self.block_03, (50, 50))

        
        self.rect = self.surf.get_rect(left=0, top=0)
        self.rect_01 = self.surf.get_rect(left=0, top=420)
        self.rect_02 = self.surf.get_rect(left=20, top=300)
        self.rect_03 = self.surf.get_rect(left=500, top=300)
        self.rect_04 = self.surf.get_rect(left=200, top=435)
        self.rect_05 = self.surf.get_rect(left=400, top=420)
        self.rect_06 = self.surf.get_rect(left=200, top=420)
        self.rect_07 = self.surf.get_rect(left=350, top=385)
        self.rect_08 = self.surf.get_rect(left=0, top=240)
        self.rect_09 = self.surf.get_rect(left=50, top=240)
        self.rect_10 = self.surf.get_rect(left=100, top=240)
        self.rect_11 = self.surf.get_rect(left=150, top=240)
        self.rect_12 = self.surf.get_rect(left=200, top=240)
        self.rect_13 = self.surf.get_rect(left=250, top=240)
        self.rect_14 = self.surf.get_rect(left=0, top=50)
        self.rect_15 = self.surf.get_rect(left=50, top=50)
        self.rect_16 = self.surf.get_rect(left=100, top=50)
        self.rect_17 = self.surf.get_rect(left=150, top=50)
        self.rect_18 = self.surf.get_rect(left=200, top=50)
        self.rect_19 = self.surf.get_rect(left=250, top=50)



    def run(self):
        pygame.mixer.music.load('asset/LevelSound.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.scale, dest=self.rect)
            self.window.blit(source=self.scale_01, dest=self.rect_01)
            self.window.blit(source=self.scale_02, dest=self.rect_02)
            self.window.blit(source=self.scale_03, dest=self.rect_03)
            self.window.blit(source=self.scale_04, dest=self.rect_04)
            self.window.blit(source=self.scale_05, dest=self.rect_05)
            self.window.blit(source=self.scale_06, dest=self.rect_06)
            self.window.blit(source=self.scale_07, dest=self.rect_07)
            self.window.blit(source=self.scale_08, dest=self.rect_08)
            self.window.blit(source=self.scale_09, dest=self.rect_09)
            self.window.blit(source=self.scale_08, dest=self.rect_10)
            self.window.blit(source=self.scale_09, dest=self.rect_11)
            self.window.blit(source=self.scale_08, dest=self.rect_12)
            self.window.blit(source=self.scale_09, dest=self.rect_13)
            self.window.blit(source=self.scale_10, dest=self.rect_14)
            self.window.blit(source=self.scale_10, dest=self.rect_15)
            self.window.blit(source=self.scale_10, dest=self.rect_16)
            self.window.blit(source=self.scale_10, dest=self.rect_17)
            self.window.blit(source=self.scale_10, dest=self.rect_18)
            self.window.blit(source=self.scale_10, dest=self.rect_19)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()