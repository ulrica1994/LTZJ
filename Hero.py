'''
英雄机
'''
from LTZJ.flyObject import FlyObject
from LTZJ.Bullet import Bullet
import pygame


class Hero(FlyObject):
    # 1. init()函数
    def __init__(self, screen, images):
        # 父类属性初始化
        self.screen = screen
        # 图片路径地址
        self.images = images
        self.image = pygame.image.load(images[0])
        self.x = 300
        self.y = 300

        # 初始化父类
        super(Hero, self).__init__(screen, self.x, self.y, self.image)

        # 子类
        self.index = 0 # 动画频率值
        self.life = 10
        self.doubleFire = 0

    # 2. 走一步
    def step(self):
        # 动画效果
        # 修改坐标值
        self.index += 1
        # 频率值算法
        ix = self.index / 10 % len(self.images)
        # 重新赋值给image
        self.image = pygame.image.load(self.images[int(ix)])

    # 3. 出界函数
    def outofBounds(self):
        pass

    # 鼠标移动
    def moveTo(self, mx, my):
        self.x = mx - self.width/2
        self.y = my - self.height/2

    def shootBy(self, image):
        wd = self.width/8
        bs = []
        if self.doubleFire > 0:
            # 双倍火力
            bs.append(Bullet(self.screen, self.x + wd*1, self.y - 10, image))
            bs.append(Bullet(self.screen, self.x + wd*3, self.y - 10, image))
            bs.append(Bullet(self.screen, self.x + wd*5, self.y - 10, image))
            bs.append(Bullet(self.screen, self.x + wd*7, self.y - 10, image))
        else:
            # 单倍火力
            bs.append(Bullet(self.screen, self.x + wd*2, self.y - 10, image))
        # 减少火力值
        self.doubleFire -= 1
        return bs