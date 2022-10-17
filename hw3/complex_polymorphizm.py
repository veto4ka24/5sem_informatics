import math as mth
def raz(z1, z2):
    u = z1._x - z2._x
    v = z1._y - z2._y
    return u, v

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

    def get(self):
        return self._x, self._y

    def set(self, x, y):
        self._x = x
        self._y = y

    def expon(self, x, y):
        if mth.sqrt(self._x ** 2 + self._y ** 2) >= 0:
            self._r = (x ** 2 + y ** 2) ** 0.5
            self._phi = mth.atan(y / x)
            return str(self._r + 'e^' + self._phi)
        if mth.sqrt(self._x ** 2 + self._y ** 2) == 0:
            self._r = 'Представление не однозначно'
            self._phi = 'Представление не однозначно'
            return str(self._r, self._phi)
        self._r = 'Значение r должно быть больше нуля!'
        self._phi = 'Значение r должно быть больше нуля!'
        return str(self._r, self._phi)


    def classic(self, r, phi):
        if mth.sqrt(r)

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Complex_num(self._a + other, self._b)
        if type(other) == Complex_num:
            return Complex_num(self._a + other._a, self._b + other._b)

#тесты
z = Complex_num(4, 6)
q = Complex_num(5, 0)
w = z + q
print(w)