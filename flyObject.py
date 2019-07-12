# 所有飞行物都要继承FlyObject

import abc
class FlyObject(object):

    # 类的初始化函数 构造方法
    # self类当前的引用地址，类似于this
    # self当前类对象
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.width = self.image.get_rect()[2]
        self.height = self.image.get_rect()[3]

    # 我们抽象出一个基类，知道要有哪些方法，但只是抽象方法，并不实现功能，只能继承，
    # 而不能被实例化，但子类必须要实现该方法
    # abc抽象函数
    @abc.abstractmethod
    def step(self):
        pass

    # 出界函数
    @abc.abstractmethod
    def outofBounds(self):
        pass

    # 公共函数
    def blitMe(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 碰撞函数
    def hitBy(self, bt):
        # 子弹坐标
        bx = bt.x
        by = bt.y
        bxw = bt.x + bt.width
        byh = bt.y + bt.height

        # 飞行物坐标
        fx = self.x
        fy = self.y
        fxw = self.x + self.width
        fyh = self.y + self.height

        return fx < bx and fxw > bxw and fy < by and fyh > byh

