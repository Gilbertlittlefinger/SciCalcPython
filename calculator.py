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
# add lots more methods to this calculator class.
