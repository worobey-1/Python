import math
 
class Hole(object):
    """
    Абстрактная дырка в вашем коде
    """
    def __init__(self, r):
        # задаем радиус дыры
        self.r = r
 
    def put(self, obj):
        # пытаемся поместить
        try:
            # чтобы влезло, нужно,
            # чтобы радиус дырки позволял
            if self.r >= obj.r:
                print('Лезет!')
            else:
                print('Не лезет')
        except AttributeError:
            print('Переданный объект не умеет вычислять радиус дырки,')
            print(u' в которую он влезет! Напишите Адаптер на python!')
 
class Square(object):
    """
    Абстрактный квадратный кол, который позволит
    закрыть абстрактную дырку в коде
    """
    def __init__(self, x, h):
        # зададим параметры дрына
        self.x = x
        self.h = h
 
class SquareHoleAdapter(object):
    def __init__(self, sq_obj):
        self.sq_obj = sq_obj
 
    @property
    def r(self):
        # половина диагонали квадрата будет как раз влезать
        # в дырку радиусом с полученное значение
        return math.sqrt(2*(self.sq_obj.x**2))/2
 
h1 = Hole(5)
h2 = Hole(2)
s1 = Square(5, 7)
s2 = Square(3, 3)
sa = SquareHoleAdapter(s2)
  
h1.put(s1)
h1.put(sa)
h2.put(sa)
