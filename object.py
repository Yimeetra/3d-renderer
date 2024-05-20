import math
from utils import *
from Vec3d import *


class Object:
    def __init__(self,x,y,z):
        self.pos = Vec3d(x,y,z)
        self.points = []
        self.polygons = []

    def add_point(self,point):
        self.points.append(Vec3d(point[0],point[1],point[2]))
    def add_polygon(self,poly):
        self.polygons.append(poly)

    def read_model(self,model):
        for point in model['points']:
            self.add_point(point)
        for poly in model['polygons']:
            self.add_polygon(poly)

    def move(self,mvec):
        self.pos += mvec
    
    def scale(self,scale):
        for i,point in enumerate(self.points):
            self.points[i] = point*scale

    def rotate_z(self,a,pivot):
        cos = round(math.cos(math.radians(a)),10)
        sin = round(math.sin(math.radians(a)),10)
        for i,point in enumerate(self.points): 
            point -= pivot
            y,x = point.y,point.x
            point.x = x*cos + y*sin
            point.y = x*-sin + y*cos
            point += pivot
            self.points[i] = point
            
    def rotate_x(self,a,pivot):
        cos = round(math.cos(math.radians(a)),10)
        sin = round(math.sin(math.radians(a)),10)
        for i,point in enumerate(self.points): 
            point -= pivot
            y,z = point.y,point.z
            point.y = y*cos + z*sin
            point.z = y*-sin + z*cos
            point += pivot
            self.points[i] = point

    def rotate_y(self,a,pivot):
        cos = round(math.cos(math.radians(a)),10)
        sin = round(math.sin(math.radians(a)),10)
        for i,point in enumerate(self.points):
            point -= pivot
            x,z = point.x,point.z
            point.x = x*cos + z*sin
            point.z = x*-sin + z*cos
            point += pivot
            self.points[i] = point