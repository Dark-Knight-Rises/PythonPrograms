class Avg:
    def setNums(self):
        self.nums=list()
        ch=True
        while ch is True:
            n=(input("enter the num, when done enter done: "))
            if n=='done':
                break
            self.nums.append(int(n))
    
    def getAvg(self):
        return sum(self.nums)/len(self.nums)

    def getSum(self):
        return sum(self.nums)

obj=Avg()

obj.setNums()
print("The sum of the list os: ",obj.getSum())
print("the avg is: ",obj.getAvg())