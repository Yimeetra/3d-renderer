import math

class Vec2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,vec):
        return Vec2d(self.x+vec.x,self.y+vec.y)
    
    def __sub__(self,vec):
        if isinstance(vec,Vec2d):
            return Vec2d(self.x-vec.x,self.y-vec.y)

    def __mul__(self,b):
        if isinstance(b,Vec2d):
            return
        return Vec2d(self.x*b,self.y*b)

    def __truediv__(self,b):
        if isinstance(b,Vec2d):
            return
        return Vec2d(self.x/b,self.y/b)

    def __iter__(self):
        return (self.x,self.y)

    def __call__(self):
        return self.to_cords()

    def to_cords(self):
        return (self.x,self.y)

    def length(self):
        if self.x == 0 and self.y == 0:
            return 0
        return math.sqrt(self.x**2+self.y**2)

    def normalise(self):
        length = self.length()
        if length == 0:
            self.x = 0
            self.y = 0
            return self
        self.x /= length
        self.y /= length
        return self
    
    def normalised(self):
        length = self.length()
        if length == 0:
            return Vec2d(0,0)
        return self/length

def distance(a,b):
    return (b-a).length()

def dot(a,b):
    return a.x*b.x+a.y*b.y