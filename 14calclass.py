class Cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def getSum(self):
        return (self.a+self.b)
    def getPro(self):
        return(self.a*self.b)
    def getDiff(self):
        return(self.a-self.b)
    def getDiv(self):
        return(self.a/self.b)

c=int(input("enter 1st: "))
d=int(input("enter 2nd: "))
a1=Cal(c,d)
print(f"The sum of {c} and {d} is: {a1.getSum()}")
print(f"The Pro of {c} and {d} is: {a1.getPro()}")
print(f"The Diff of {c} and {d} is: {a1.getDiff()}")
print(f"The Div of {c} and {d} is: {a1.getDiv()}")