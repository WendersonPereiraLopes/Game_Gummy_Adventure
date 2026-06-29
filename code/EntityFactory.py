from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy
from code.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'LevelBg':
                list_bg = []

                list_bg.append(Background('LevelBg', (0,0), (WIN_WIDTH, WIN_HEIGHT)))
                list_bg.append(Background('plataforma01Bg', (0, 410), (WIN_WIDTH / 4, 50)))
                list_bg.append(Background('aguaBg', (200, 430), (WIN_WIDTH / 4,50)))
                list_bg.append(Background('plataforma01Bg', (450, 410), (WIN_WIDTH / 2 - 50, 50)))
                list_bg.append(Background('plataforma02Bg', (550, 310), (WIN_WIDTH / 5 , 100)))
                list_bg.append(Background('plataforma03Bg', (400, 375), (50, 100)))
                list_bg.append(Background('ponteBg', (200, 410), (WIN_WIDTH / 4, 8)))
                list_bg.append(Background('ArvoreBg', (50, 290), (100, 120)))
                list_bg.append(Background('Block01Bg', (0, 220), (50, 50)))
                list_bg.append(Background('Block02Bg', (50, 220), (50, 50)))
                list_bg.append(Background('Block01Bg', (100, 220), (50, 50)))
                list_bg.append(Background('Block02Bg', (150, 220), (50, 50)))
                list_bg.append(Background('Block01Bg', (200, 220), (50, 50)))
                list_bg.append(Background('Block02Bg', (250, 220), (50, 50)))

                for i in range(0, 300, 50):
                        list_bg.append(Background('Block03Bg', (i, 50), (50, 50)))
    
                return list_bg
            case 'Player':
                  return Player('player', (20,364), (50,50))
            case 'Enemy1':
                  return Enemy('enemy1', (WIN_WIDTH,WIN_HEIGHT - 120), (80,80))
            case 'Enemy2':
                  return Enemy('enemy2', (WIN_WIDTH, WIN_HEIGHT / 4 + 20), (60,60))