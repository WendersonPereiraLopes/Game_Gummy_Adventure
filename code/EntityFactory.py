from code.Background import Background

class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'LevelBg':
                list_bg = []
                for i in range(1):
                    list_bg.append(Background('LevelBg', (0, 0)))

                return list_bg