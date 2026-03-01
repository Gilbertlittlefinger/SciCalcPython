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

    def deg(self, x):
        return math.degrees(x)
    
    def rad(self, x):
        return math.radians(x)
    
    def fac(self, x):
        return math.factorial(x)
    
    def log(self, x):
        return math.log(x)
    
    def log10(self, x):
        return math.log10(x)
    
    def natlog(self, x):
        return math.log1p(x)
    
    def in_natlog(self, x):
        return math.pow(log1p(x),-1)
    
    def infinity(self, x):
        return math.isinfinite(x)
    
    def abs_val(self, x):
        return math.fabs(x)
# add lots more methods to this calculator class.
