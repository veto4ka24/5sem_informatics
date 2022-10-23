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

class triangle(figure, point):
    def __init__(self, p1, p2, p3, type="triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3

    def area(self):
        S = abs((self._point_2.get_x() - self._point_1.get_x())*(self._point_3.get_y() - self._point_1.get_y()) - (self._point_3.get_x() - self._point_1.get_x())*(self._point_2.get_y() - self._point_1.get_y()))/2
        return 'Площадь треугольника S = ' + str(S)

    def perimeter(self):
        P = dist(self._point_1, self._point_2) + dist(self._point_2, self._point_3) + dist(self._point_1, self._point_3)
        return 'Периметр треугольника P = ' + str(P)

class parallelogram(figure, point):
    def __init__(self, p1, p2, p3, p4, type="parallelogram"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4

    def Normal(self):
        H = ((dist(self._point_1, self._point_2))**2 + (dist(self._point_2, self._point_3))**2)**0.5
        return H

    def area(self):
        if dist(self._point_1, self._point_2) >= dist(self._point_2, self._point_3):
            S = dist(self._point_1, self._point_2)*self.Normal()
        else:
            S = dist(self._point_2, self._point_3)*self.Normal()
        return 'Площадь параллелограмма S = ' + str(S)

    def perimeter(self):
        P = 2*(dist(self._point_1, self._point_2) + dist(self._point_2, self._point_3))
        return 'Периметр параллелограмма P = ' + str(P)

class rhombus(parallelogram):
    def __init__(self, p1, p2, p3, p4, type="rhombus"):
        super().__init__(p1, p2, p3, p4, type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4

    def area(self):
        S = 0.5*dist(self._point_1, self._point_3)*dist(self._point_2, self._point_4)
        return 'Площадь ромба S = ' + str(S)

    def perimeter(self):
        P = 4*dist(self._point_1, self._point_2)
        return 'Периметр ромба P = ' + str(P)

class rectangle(parallelogram):
    def __init__(self, p1, p2, p3, p4, type="rectangle"):
        super().__init__(p1, p2, p3, p4, type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4

    def area(self):
        S = dist(self._point_1, self._point_2)*dist(self._point_2, self._point_3)
        return 'Площадь прямоугольника S = ' + str(S)

    def perimeter(self):
        P = 2 * (dist(self._point_1, self._point_2) + dist(self._point_2, self._point_3))
        return 'Периметр прямоугольника P = ' + str(P)

class square(rectangle, rhombus):
    def __init__(self, p1, p2, p3, p4, type="square"):
        super().__init__(p1, p2, p3, p4, type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4

    def area(self):
        S = dist(self._point_1, self._point_2)**2
        return 'Площадь квадрата S = ' + str(S)

    def perimeter(self):
        P = 4*dist(self._point_1, self._point_2)
        return 'Периметр квадрата P = ' + str(P)

a = triangle(point(), point(1, 3), point(2, 1))
print(a)
print(a.perimeter())
print(a.area())
b = parallelogram(point(), point(2, 5), point(7, 5), point(5, 0))
print(b.area())
print(b.perimeter())
c = rhombus(point(), point(2, 3), point(0, 4), point(2, -3))
print(c)
print(c.area())
print(c.perimeter())
d = rectangle(point(), point(0, 3), point(4, 3), point(4, 0))
print(d)
print(d.area())
print(d.perimeter())
e = square(point(), point(0, 3), point(3, 3), point(3, 0))
print(e)
print(e.area())
print(e.perimeter())