import math as mth

class MyException:
    pass

class NotSingleExponentalRepresent(MyException):
    pass

class Complex_num:
    _x = 0
    _y = 0
    def __init__(self, x=0, y=0):
        self.set(x, y)
        if mth.sqrt(self._x ** 2 + self._y ** 2) > 0:
            self._r = (x ** 2 + y ** 2) ** 0.5
            self._phi = mth.atan(y / x)
        else:
            raise NotSingleExponentalRepresent('Представление в экспоненциальной форме не однозначно!')

    def get(self):
        return self._x, self._y

    def set(self, x, y):
        if int(self._x) == self._x or float(self._x) == self._x:
            self._x = x
        else:
            raise ValueError
        if int(self._y) == self._y or float(self._y) == self._y:
            self._y = y
        else:
            raise ValueError

    def expon(self):
        return self._r, self._phi

    def classic(self):
        if self._r > 0:
            self._x = self._r*mth.cos(self._phi)
            self._y = self._r*mth.sin(self._phi)
            return str(self._x, self._y)
        return str('Значение r должно быть больше нуля!')

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self._x + other, self._y
        if type(other) == Complex_num:
            return self._x + other._x, self._y + other._y

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            return self._x + other, self._y
        if type(other) == Complex_num:
            return self._x + other._x, self._y + other._y

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self._x - other, self._y
        if type(other) == Complex_num:
            return self._x - other._x, self._y - other._y

    def __rsub__(self, other):
        if type(other) == int or type(other) == float:
            return self._x - other, self._y
        if type(other) == Complex_num:
            return self._x - other._x, self._y - other._y

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self._x * other, self._y * other
        if type(other) == Complex_num:
            return self._x * other._x - self._y * other._y, self._x * other._y + self._y * other._x

    def __rmul__(self, other):
        if type(other) == int or type(other) == float:
            return self._x * other, self._y * other
        if type(other) == Complex_num:
            return self._x * other._x - self._y * other._y, self._x * other._y + self._y * other._x

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            if other != 0:
                return self._x / other, self._y / other
            return str('Делитель должен быть олтичен от нуля!')
        if type(other) == Complex_num:
            if other._x != 0 or other._y != 0:
                Re_chisl = self._x * other._x - self._y * other._y
                Im_chisl = self._x * other._y + other._x * self._y
                znam = (other._x) ** 2 + (other._y) ** 2
                u = Re_chisl / znam
                v = Im_chisl / znam
                return u, v
            return str('Делитель должен быть ненулевой!')

    def __rtruediv__(self, other):
        if type(other) == int or type(other) == float:
            if other != 0:
                return self._x / other, self._y / other
            return str('Делитель должен быть олтичен от нуля!')
        if type(other) == Complex_num:
            if other._x != 0 or other._y != 0:
                Re_chisl = self._x * other._x - self._y * other._y
                Im_chisl = self._x * other._y + other._x * self._y
                znam = (other._x) ** 2 + (other._y) ** 2
                u = Re_chisl / znam
                v = Im_chisl / znam
                return u, v
            return str('Делитель должен быть ненулевой!')

#тесты
z = Complex_num(4, 6)
r = Complex_num()
print(r.get())
q = Complex_num(9, 0)
a = 1
b = Complex_num()
print(z.expon())
w = z + q
s = a + z
m = z - q
p = z/q
n = q/b
print(n)
print(p)
print(m)
print(s)
print(w)