class Employee:
    # total=0
    def __init__(self,sal,incr):
        self.sal=sal
        self.incr=incr
    def getTotal(self):
        # Employee.total+=self.sal+self.incr
        return(self.sal*self.incr)

ob1=Employee(1000,1.5)
print("The total sal is: ",ob1.getTotal())