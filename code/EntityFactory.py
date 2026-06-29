from code.Background import Background
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
                
               
                return list_bg