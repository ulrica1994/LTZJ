import abc

class Award(object):
    LIFE = 0
    DOUBLEFIRE = 1

    @abc.abstractmethod
    def getAward(self):
        pass
