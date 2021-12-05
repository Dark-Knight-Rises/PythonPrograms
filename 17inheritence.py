class A:
    def __init__(self):
        print("Constructor of a")
    def showA(self):
        print("In a")
class B(A):
    def __init__(self):
        super().__init__()
        # print("Constructor of b")
    def showB(self):
        print("In b")
obj=B()
