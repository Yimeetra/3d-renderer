import math
from Vec3d import *

class Camera:
    def __init__(self,x,y,z,dir = Vec3d(0,0,0)):
        self.pos = Vec3d(x,y,z)
        self.dir = dir
    def move(self,s):
        pass