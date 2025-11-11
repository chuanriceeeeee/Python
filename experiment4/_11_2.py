import _11_
if __name__=="__main__":
    try_flag=0
    while try_flag==0:
        try :
            r=float(input("Please input the value of r:\n"))
        except ValueError:
            print("Please input a number!\n")
            continue
        try_flag=1
    try_flag = 0
    while try_flag == 0:
        try:
            h = float(input("Please input the value of h:\n"))
        except ValueError:
            print("Please input a number!\n")
            continue
        try_flag = 1
    _11_.sphereVolume(r)
    _11_.sphereSurface(r)
    _11_.CylinderVolume(r,h)
    _11_.CylinderSurface(r,h)
    _11_.conVolume(r,h)
    _11_.conSurface(r, h)
