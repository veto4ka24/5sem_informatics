import math as mth

def chast(z1, z2):
    Re_chisl = z1._x*z2._x - z1._y*z2._y
    Im_chisl = z1._x*z2._y + z2._x*z1._y
    znam = (z2._x)**2 + (z2._y)**2
    u = Re_chisl/znam
    v = Im_chisl/znam
    return u, v

def pr(z1, z2):
    u = z1._x*z2._x - z1._y*z2._y
    v = z1._y*z2._x + z1._x*z2._y
    return u, v

class Complex_num:
    _x = 0
    _y = 0
    def __init__(self, x=0, y=0):
        self.set(x, y)
        if mth.sqrt(self._x ** 2 + self._y ** 2) >= 0:
            self._r = (x ** 2 + y ** 2) ** 0.5
            self._phi = mth.atan(y / x)
        elif mth.sqrt(self._x ** 2 + self._y ** 2) == 0:
            self._r = 'Представление не однозначно'
            self._phi = 'Представление не однозначно'
        else:
            self._r = 'Значение r должно быть больше нуля!'
            self._phi = 'Значение r должно быть больше нуля!'

    def get(self):
        return self._x, self._y

    def set(self, x, y):
        self._x = x
        self._y = y

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

#тесты
z = Complex_num(4, 6)
q = Complex_num(9, 0)
a = 1
print(z.expon())
w = z + q
s = a + z
m = z - q
print(m)
print(s)
print(w)