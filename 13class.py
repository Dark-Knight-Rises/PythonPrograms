class Programmer:
    company="micro"
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def getInfo(self):
        print("The name is: ",self.name)
        print("Sal: ",self.sal)
        print("Comapny: ",self.company)

piyush=Programmer("piyush",300000)
a1=Programmer("aditi",200000)
piyush.getInfo()
a1.getInfo()
