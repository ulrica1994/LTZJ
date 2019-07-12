import abc

class Enemy(object):

    # 抽象函数
    @abc.abstractmethod
    def getScore(self):
        pass