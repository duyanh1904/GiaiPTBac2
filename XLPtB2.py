from math import sqrt
class XuLyPtB2():
    def __init__(self,_a,_b,_c):
        self.a = _a
        self.b = _b
        self.c = _c

    def TimNghiem(self):
        if self.a == 0:
            print('pt da cho k phai pt bac 2')
        else:
            delta = self.b * self.b - 4 * self.a * self.c
            if delta < 0:
                print('pt vo nghiem')
            elif delta == 0:
                print('Phuong trinh co nghiem kep x1 = x2 = ', -self.b / (2 * self.a))
            else:
                print("Phuong trinh co 2 nghiem phan biet")
                print("x1 = ", float((-self.b - sqrt(delta)) / (2 * self.a)))
                print("x2 = ", float((-self.b + sqrt(delta)) / (2 * self.a)))





