from code.Entity import Entity
from code.Const import ENTITY_SPEED

class EnemyShot(Entity):

    def __init__(self, name, position, scale):
        super().__init__(name, position, scale)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]