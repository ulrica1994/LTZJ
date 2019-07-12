from LTZJ.flyObject import FlyObject
import pygame
class BossBullet(FlyObject):
    def __init__(self, screen,x, y, images):
        self.screen = screen
        self.images = images
        self.image = pygame.image.load(self.images[0])
        self.x = x
        self.y = y
        super(BossBullet, self).__init__(screen, self.x, self.y, self.image)

        self.index = 0

    def step(self):
        self.y += 10
        self.index += 3
        ix = self.index / 3 % len(self.images)
        self.image = pygame.image.load(self.images[int(ix)])

    def outofBounds(self):
        return self.y > 768 and self.y < -self.height
