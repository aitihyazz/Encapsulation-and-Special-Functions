class Computerprice:
    def __init__(self,):
        self.__maximumprice= 900
    def sell(self):
        print('Price {}'. format(self.__maximumprice))
    def set(self,price):
        self.__maximumprice =price 
c = Computerprice()
c.sell()
c.__maximumprice =1000
c.sell()
c.set(1000)
c.sell()