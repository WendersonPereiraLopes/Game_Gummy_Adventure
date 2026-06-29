from code.Entity import Entity
from code.EnemyShot import EnemyShot
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY 

class Enemy(Entity):

    def __init__(self, name, position, scale):
        super().__init__(name, position, scale)
        self.shoot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(f'missel_{self.name}', (self.rect.centerx - 5, self.rect.centery + 20 ), (20,20))