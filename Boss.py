from LTZJ.flyObject import FlyObject
from LTZJ.Enemy import Enemy
from LTZJ.BossBullet import BossBullet
import random
import pygame

class Boss(FlyObject, Enemy):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.x = random.randint(0, (512 - self.image.get_rect()[2]))
        self.y = -random.randint(198, 768)
        super(Boss, self).__init__(screen, self.x, self.y, self.image)


        self.index = 0
        self.life = 100
        self.xStep = 1
        self.yStep = 1

    def step(self):
        if self.y > 400 - self.height:
            self.yStep = -1
        elif self.y < 0:
            self.yStep = 1
        self.y += self.yStep

        if self.x > 512 - self.width:
            self.xStep = -1
        elif self.x < 0:
            self.xStep = 1
        self.x += self.xStep

        self.index += 1
        ix = self.index / 10 % (len(self.images))
        self.image = pygame.image.load(self.images[int(ix)])

    def outofBounds(self):
        pass

    def getScore(self):
        return 100

    def shootBy(self, images):
        wd = self.width/8
        bs = []

        bs.append(BossBullet(self.screen, self.x + wd * 1, self.y + self.height, images))
        bs.append(BossBullet(self.screen, self.x + wd * 3, self.y + self.height, images))
        bs.append(BossBullet(self.screen, self.x + wd * 5, self.y + self.height, images))
        bs.append(BossBullet(self.screen, self.x + wd * 7, self.y + self.height, images))
        return bs