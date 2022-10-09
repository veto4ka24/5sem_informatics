import math as mth

#def sum(z1, z2):
#   u = z1._x + z2._x
#  v = z1._y + z2._y
#   return u, v

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
        r = (x ** 2 + y ** 2) ** 0.5
        phi = mth.atan(y / x)
        print(r, '*exp(i*', phi, ')', sep = '')

    def classic(self, x, y):
        print(x, ' + i*', y, sep = '')

    def summ(self, other):
        self._x += other._x
        self._y += other._y
        return self

#тесты
z = Complex_num(4, 6)
q = Complex_num(5)
w = summ(z, q)