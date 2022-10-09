class point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

    def dist(a, b):
        return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5

class figure:
    def __init__(self, type="figure"):
        self._type = type

    def __str__(self):
        return str(self._type)

    def area(self):
        pass

    def perimeter(self):
        pass

class triangle(figure):
    def __init__(self, p1, p2, p3, type="triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3

    def area(self, p1, p2, p3):
        S = abs((p2._x - p1._x)*(p3._y - p1._y) - (p3._x - p1._x)*(p2._y - p1._y))/2
        return 'Площадь треугольника S = ' + str(S)

    def perimeter(self, p1, p2, p3):
        P = self._dist(p1, p2) + self._dist(p2, p3) + self._dist(p1, p3)
        return 'Периметр треугольника P = ' + str(P)

a = triangle(point, point(1, 3), point(2, 1))
print(a)
print(a.perimeter())
print(a.area())