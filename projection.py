import math
from utils import *
from Vec3d import Vec3d

def projection(p,obj,cam):
    w = 800
    h = 600

    cy = math.cos(0)
    sy = math.sin(0)
    cx = math.cos(0)
    sx = math.sin(0)
    cz = math.cos(0)
    sz = math.sin(0)

    d = [0,0,0]

    tr = [p[0]-cam[0],p[1]-cam[1],p[2]-cam[2]]
    tr[0] *= h/w

    y,z = tr[1],tr[2]
    tr[1] = y*cx + z*sx
    tr[2] = y*-sx + z*cx

    z,x = tr[2],tr[0]
    tr[0] = x*cx + z*sx
    tr[2] = x*-sx + z*cx

    y,x = tr[1],tr[0]
    tr[0] = x*cx + y*sx
    tr[1] = x*-sx + y*cx
    
    tr[0] += obj[0]
    tr[1] += obj[1]
    tr[2] += obj[2]

    x = (tr[0]*w)/tr[2] + w/2
    y = (tr[1]*h)/tr[2] + h/2

    return (x,y)
