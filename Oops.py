class Calculator:
    num = 100 # Class Variable

#Default Constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am calling automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def sum(self):
        return self.a + self.b + Calculator.num

obj = Calculator(5,2)
obj.getData()
print(obj.sum())