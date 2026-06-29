from code.Entity import Entity

class Enemy(Entity):

    def __init__(self, name, position, scale):
        super().__init__(name, position, scale)

    def move(self):
        pass