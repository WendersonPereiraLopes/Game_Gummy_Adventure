from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'LevelBg':
                list_bg = []
                list_bg.append(Background('LevelBg', (0,0), (WIN_WIDTH, WIN_HEIGHT)))
                list_bg.append(Background('plataforma01Bg', (0, 410), (WIN_WIDTH / 4,50)))
                list_bg.append(Background('aguaBg', (200, 410), (WIN_WIDTH / 4,50)))
               
                return list_bg