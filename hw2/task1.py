import math as mth

def expon(x, y):
    r = (x**2 + y**2) ** 0.5
    phi = mth.atan(y/x)
    print(r, '*exp(i*', phi, ')')

#def classic(r, phi):


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

z = Complex_num(2, 4)
print(z.get())
print(expon(*z.get()))