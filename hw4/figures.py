class figure:
    def area(self):
        pass

    def perimeter(self):
        pass

class triangle:
    def set(self, x, y):
        self._x = x
        self._y = y

    def __init__(self, x = 0, y = 0):
        self.set(x, y)

    def get(self):
        return self._x, self._y
    
    def area(self):
        s = abs((p2._x - p1._x)*(p3._y - p1._y) - (p3._x - p1._x)*(p2._y - p1._y))/2