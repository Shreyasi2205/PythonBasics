# classes are user defined blueprint or prototype
# operations inside the class -> sum, multiplication,addition, constant
# methods, variables, instance variables, constructor
class Calculator:
    num=100 # class variables
# constructor is method, it is called automatically when object is created
# in other languages we constructor name is same as that of class but in python we
# call it __init__
    def __init__(self) -> None:  #def __init__(self, n) -> None: does have a return type, and it's None (or NoneType, really)
        pass #variables inside constructor : instance variables
    # def __init__(self):
    #     print("constructor is called automatically")

    def __init__(self,a,b): # self is nothing but object. object will be passed as first variable
        self.a=a # self.a is instance variables not class variables
        self.b=b
    def getData(self):
        print("now I am executing as method in class")
    # so to call getData method we cannot simple call this because this is inside the class

    def sum(self): # obj is passed here and values are stored in the object memory
        # return self.a+self.b+num ->can I call like this? 
        # we can give calculator.num because is class variable
        # or self.num because obj will come and read everthing inside the call
        # return self.a+self.b+Calculator.num # 106
        # or 
        return self.a+self.b+self.num


obj=Calculator(2,4) #syntax to create obj in python
obj.getData() # now I am executing as method in class
print(obj.num) # 100
print(obj.sum()) # 6


# self keyword is imp for calling variables names into methods
# constructor name is __init__