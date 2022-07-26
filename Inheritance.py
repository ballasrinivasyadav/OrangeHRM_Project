from Oops import Calculator


class Childimpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,10,20)
    def getCompleteData(self):
        return self.num2 + self.num + self.sum()

obj = Childimpl()
print(obj.getCompleteData())
