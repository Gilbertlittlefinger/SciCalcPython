import math

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x -y
    
    def mult(self, x, y):
        return x * y
    
    def div(self, x, y):
        return x / y
    
    def sqr(self, x):
        return x * x

    def root2(self, x):
        return math.sqrt(x)
    
    def exp(self, x, y):
        return math.pow(x, y)
    
    def inv(self, x):
        return x ** -1
    
    def neg(self, x):
        return x * -1
    
    def sin(self, x):
        return math.sin(x)
    
    def cos(self, x):
        return math.cos(x)
    
    def tan(self, x):
        return math.tan(x)
    
    def isin(self, x):
        return math.asin(x)
    
    def icos(self, x):
        return math.acos(x)
    
    def itan(self, x):
        return math.atan(x)

# add lots more methods to this calculator class.
