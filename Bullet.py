from LTZJ.flyObject import FlyObject
import pygame

class Bullet(FlyObject):
    # 初始化函数
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.image.load(image)
        #初始化父类
        super(Bullet, self).__init__(screen, self.x, self.y, self.image)

    # 走一步
    def step(self):
        # 修改坐标值
        self.y -= 10

    # 出界
    def outofBounds(self):
        if self.y < -self.height:
            return True
        else:
            return False


