from LTZJ.flyObject import FlyObject
from LTZJ.Award import Award
import random
import pygame

class Love(FlyObject, Award):
    def __init__(self, screen, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.x = random.randint(0, (512 - self.image.get_rect()[2]))
        self.y = -random.randint(0,768)
        self.awardType = random.randint(0, 1)

        super(Love,self).__init__(screen, self.x, self.y, self.image)
        self.index = 0
        self.xStep = 1
        self.yStep = 1

    def step(self):
        self.y += 1
        self.index += 1
        if self.x > 512 - self.width:
            self.xStep = -1
        elif self.x < 0:
            self.xStep = 1
        self.x += self.xStep

        ix = self.index / 10 % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])

    def outofBounds(self):
        if self.y > 768:
            return True
        else:
            return False

    def getAward(self):
        return self.awardType