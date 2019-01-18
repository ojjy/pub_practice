# Python 3.7.2/win10 64bit/IDE:Pycharm 2018.3.3
# create class of complex number and definite operation by using operation overloading
from math import sqrt

class complex_num():
    def __init__(self, realnum, imgnum):
        self.realnum=realnum
        self.imgnum=imgnum

    def get_complex_num(self):
        if(self.imgnum<0):
            return str(self.realnum)+str(self.imgnum)+"i"
        else:
            return str(self.realnum)+"+"+str(self.imgnum)+"i"

    def complex_conjugate(self):
        return complex_num(self.realnum, -self.imgnum)

    def __add__(self, other):
        return complex_num(self.realnum+other.realnum, self.imgnum+other.imgnum)

    def __sub__(self, other):
        return complex_num(self.realnum-other.realnum, self.imgnum-other.imgnum)

    def __mul__(self, other):
        return complex_num(self.realnum*other.realnum-self.imgnum*other.imgnum, self.realnum*other.imgnum+self.imgnum*other.realnum)

    def __truediv__(self, other):
        return complex_num((self.realnum*other.realnum+self.imgnum*other.realnum)/other.realnum**2+other.imgnum**2, (self.imgnum*other.realnum-self.imgnum*other.imgnum)/other.realnum**2+other.imgnum**2)

    def abs(self):
        return sqrt(self.realnum*self.realnum+self.imgnum*self.imgnum)



if __name__=="__main__":
    cn1=complex_num(2,3)
    print(cn1.get_complex_num())
    cn2=complex_num(4,5)
    print(cn2.get_complex_num())
    cn3=cn1+cn2
    print(cn3.get_complex_num())
    cn4=cn1-cn2
    print(cn4.get_complex_num())
    cn5=cn1*cn2
    print(cn5.get_complex_num())
    print(cn4.complex_conjugate().get_complex_num())
    print(cn1.abs())
    cn6=complex_num(0,1)
    cn7=cn6*cn6
    print(cn7.get_complex_num())
    cn7=cn7*cn6
    print(cn7.get_complex_num())
    cn7=cn7*cn6
    print(cn7.get_complex_num())
    cn8=cn1/cn2
    print(cn8.get_complex_num())
    cn9=cn1*cn1.complex_conjugate()
    print(cn9.get_complex_num())