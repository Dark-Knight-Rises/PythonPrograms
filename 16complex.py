class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c):
        return Complex(self.r+c.r, self.i+c.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
ob1=Complex(1,7)
ob2=Complex(3,6)
print(ob1+ob2)
