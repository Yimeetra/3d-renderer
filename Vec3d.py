import math

class Vec3d:
    x: float
    y: float
    z: float
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self,vec):
        return Vec3d(self.x+vec.x,self.y+vec.y,self.z+vec.z)
    
    def __sub__(self,vec):
        return Vec3d(self.x-vec.x,self.y-vec.y,self.z-vec.z)

    def __mul__(self,b):
        if isinstance(b,Vec3d):
            return
        return Vec3d(self.x*b,self.y*b,self.z*b)

    def __truediv__(self,b):
        if isinstance(b,Vec3d):
            return
        return Vec3d(self.x/b,self.y/b,self.z/b)

    def __call__(self):
        return self.to_cords()

    def to_cords(self):
        return (self.x,self.y,self.z)

    def length(self):
        if self.x == 0 and self.y == 0 and self.z == 0:
            return 0
        return math.sqrt(self.x**2+self.y**2+self.z**2)

    def normalise(self):
        length = self.length()
        if length == 0:
            self.x = 0
            self.y = 0
            return self
        self /= length
        return self

    def normalised(self):
        length = self.length()
        if length == 0:
            return Vec3d(0,0,0)
        return self/length

def distance(a,b):
    return (b-a).length()
