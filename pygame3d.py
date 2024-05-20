import pygame
import sys
from camera import *
from object import *
from projection import *

HEIGHT = 600
WIDTH = 800
scale = 100

DIST = 2

def update(sc,obj,cam):
    x,y,z = obj.pos.x,obj.pos.y,obj.pos.z

    for poly in obj.polygons:
        p1 = obj.points[poly[0]-1]
        p2 = obj.points[poly[1]-1]
        p3 = obj.points[poly[2]-1]   
        p1 = projection(p1.to_cords(),obj.pos.to_cords(),cam.pos.to_cords())
        p2 = projection(p2.to_cords(),obj.pos.to_cords(),cam.pos.to_cords())
        p3 = projection(p3.to_cords(),obj.pos.to_cords(),cam.pos.to_cords())

        pygame.draw.polygon(sc,(255,255,255),(p1,p2,p3),1)
       

pygame.init()
pygame.event.set_allowed([pygame.QUIT])
screen = pygame.display.set_mode((WIDTH, HEIGHT))

cam = Camera(0,0,0)

objects = []
objects.append(Object(0,0,10))
objects[-1].read_model(obj_to_model('lowpolyfrog.obj'))
objects[-1].scale(.1)
objects[-1].rotate_x(-90,Vec3d(0,0,0))
objects[-1].move(Vec3d(0,2,0))

clock = pygame.time.Clock()

dps = 180
t = 0

while 1:
    pygame.display.set_caption(str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    t = clock.tick_busy_loop(clock.get_fps())/1000

    update(screen,objects[-1],cam)
    #objects[-1].rotate_x(dps*t/2,Vec3d(0,0,0))
    objects[-1].rotate_y(dps*t,Vec3d(0,0,0))
    #objects[-1].rotate_z(dps*t/3,Vec3d(0,0,0))
    
    pygame.display.flip() 
    clock.tick(math.inf)