from oopsDemo import Calculator
# from filename import classname

class ChildImpl(Calculator):
    num2=200

    def __init__(self, a, b):
        super().__init__(a,b) # or Calculator.__init__(self,a,b)
    def getCompleteData(self):
        return self.num2 + self.num+self.sum()
        # in sum a,b were send during runtime so data present inside sum



obj=ChildImpl(4,5)
print(obj.getCompleteData()) # TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'

