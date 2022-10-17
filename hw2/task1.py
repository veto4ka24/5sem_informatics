import math as mth

def sum(z1, z2):
    u = z1._x + z2._x
    v = z1._y + z2._y
    return u, v

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
        if mth.sqrt(self._x ** 2 + self._y ** 2) < 0:
            self._r = 'Значение r должно быть больше нуля!'
            self._phi = 'Значение r должно быть больше нуля!'
        elif mth.sqrt(self._x ** 2 + self._y ** 2) > 0:
            if x != 0:
                self._r = (x ** 2 + y ** 2) ** 0.5
                self._phi = mth.atan(y / x)
            else:
                self._r = 'Значение угла не определено!'
                self._phi = 'Значение угла не определено!'
        else:
            self._r = 'Представление не однозначно'
            self._phi = 'Представление не однозначно'

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

#тесты
z = Complex_num(3, 7)
q = Complex_num(4)
m = Complex_num(0, 8)
#print(q.get())
#z.expon(*z.get())
#z.classic(*z.get())
#print(sum(z, q))
#print(raz(z, q))
#print(pr(z, q))
print(chast(z, q))
print(chast(z, m))