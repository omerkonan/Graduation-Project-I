####################################################################

#Circle equation with 3 points known:
#(x-x1)^2 + (y-y1)'2 = (x-x2)^2 + (y-y2)'2 = (x-x3)^2 + (y-y3)'2  = r^2 

#So we can extract this equations:
#x1^2 - x2^2 + y1^2 - y2^2 = x(x1-x2)/2 + y(y1-y2)/2
#x1^2 - x3^2 + y1^2 - y3^2 = x(x1-x3)/2 + y(y1-y3)/2

#With this equations, we are going to find center(x,y) and radius

#For question: konanomer@gmail.com

####################################################################

import numpy as np


def circle_center(p1, p2, p3):

    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    equ  = x1**2 - x2**2 + y1**2 - y2**2
    equ2 = x1**2 - x3**2 + y1**2 - y3**2

    coeff  = (x1-x2)/2
    coeff2 = (y1-y2)/2
    coeff3 = (x1-x3)/2
    coeff4 = (y1-y3)/2

    a = np.array([[coeff  , coeff2],
                  [coeff3 , coeff4]],float)

    b = np.array([equ, equ2],float)
    
    x, y = np.linalg.solve(a, b) # To solve linear algebra system of equations

    center = (x, y)
    
    return center

def radius(center,p1):

    x  , y  = center
    x1 , y1 = p1

    r = ((x - x1)**2 + (x - y1)**2) ** 0.5 

    return r



"""
#######TEST_CODE#######

def main():
    p1 = (0, -4)
    p2 = (0, 4)
    p3 = (4, 0)

    center = circle_center(p1, p2 ,p3)
    r = radius(center, p1)

    print("Center:", center)
    print("Radius:", r)
if __name__ == "__main__":
    main()

#######################
"""