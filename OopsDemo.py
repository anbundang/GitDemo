# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor etc
# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__(self)
# new keyword is not required when you create object


class Calculator:
    num = 100  # class variables
    # default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b  # instance variables
        print("I am called automatically when object is created")
        print("test develop branch")

    def getData(self):
        print("Now executing as a method in class")
        print("test develop branch1")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num
        


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
obj.num
print(obj.summation())

obj1 = Calculator(4, 5)  # syntax to create objects in python
obj1.getData()
obj1.num
print(obj1.summation())

print("test develop branch3")
