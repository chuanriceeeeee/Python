"""
round(2.12312,2) remain 2.12
"""

import math
def sphereVolume(r):
    print(f"{round(4*(r**3)*math.pi/3,3)}")
    return
def sphereSurface(r):
    print(f"{round(3*(r**2)*math.pi/4,3)}")
    return
def CylinderVolume(r,h):
    print(f"{round(math.pi*(r**2)*h,3)}")
    return
def CylinderSurface(r,h):
    print(f"{round(math.pi*(r**2)*2+2*math.pi*r*h,3)}")
    return
def conVolume(r,h):
    print(f"{round(math.pi*(r**2)*h/3,3)}")
    return
def conSurface(r,h):
    print(f"{round(math.pi*(r**2)+r*math.sqrt(r**2+h**2)/2,3)}")
    return