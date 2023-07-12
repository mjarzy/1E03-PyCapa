# PyPHYS1.py
""" Handling physics questions

This program can compute certain physics scenarios that may pop up
when doing physics problems. It is written by Dave Gumba. Just
run the module and follow the instructions!

NumPy: http://www.scipy.org/scipylib/download.html
"""

from math import *
import numpy as np

ke = 8.99*10**9
g = 9.8
permitivity = 8.85*10**-12
e_q = 1.602*10**-19
m_e = 9.11*10**-31

def three_charges():
    q1 = eval(input("Enter the first charge(in C): "))
    x1 = eval(input("Enter q1s distance from q3(no negative): "))
    q2 = eval(input("Enter the second charge(in C): "))
    x2 = eval(input("Enter q2s distance from q3: "))
    q3 = eval(input("Enter q3: "))
    
    fq1 = (q1*q3)/(abs(x1))**2
    fq2 = (q2*q3)/(abs(x2))**2

    fnet = ke * (fq1-fq2)
    print(fnet)
    print("Units: N")

def middle():
    q1 = eval(input("Enter the charge placed at the origin(in C): "))
    q2 = eval(input("Enter the charge placed at the x-coordinate(in C): "))
    x1 = eval(input("Enter the x-coordinate q2 is placed at: "))
    q3 = eval(input("Enter the charge in the middle(in C): "))

    a = (q2/q1) - 1
    b = 2*x1
    c = -1*x1**2

    numerator1 = (-1*b)+sqrt((b**2)-(4*a*c))
    numerator2 = (-1*b)-sqrt((b**2)-(4*a*c))
    denominator = 2*a

    x = numerator1/denominator
    y = numerator2/denominator
    
    print(x)
    print("Units: m")

def ball_hanging():
    m = eval(input("Enter the mass of the cork ball(in kg): "))
    x_comp = eval(input("Enter the x-component of the electric field (in N/C): "))
    y_comp = eval(input("Enter the y-component of the electric field (in N/C): "))
    deg = eval(input("Enter the angle: "))
    deg = (deg*pi)/180

    a = np.array([[-1*sin(deg), x_comp],[cos(deg), y_comp]])
    b = np.array([0,m*g])
    x = np.linalg.solve(a,b)
    print("Tension force, charge")
    print(x)
    print("Units: N, C")

def equilateral():
    m = eval(input("Enter the mass: "))
    l = eval(input("Enter the length: "))
    s = eval(input("Enter the side length: "))

    h = s/(2*sin(pi/3))
    theta = asin(h/l)

    q = sqrt((m*g*tan(theta)*(s**2))/(2*ke*cos(pi/6)))
    print(q)
    print("Units: C")

def charge_and_field():
    m = eval(input("Enter the mass of the spheres(in kg): "))
    l = eval(input("Enter the length of the strings(in m): "))
    q = eval(input("Enter the charge of the sphere(in C): "))
    deg = eval(input("Enter the angle: "))

    deg = (deg*pi)/180
    d = 2*l*sin(deg)
    tension = (m*g)/(cos(deg))
    fe = (tension*sin(deg))+ke*((q**2)/(d**2))
    field = fe/q
    print(field)
    print("Units: N/C")

def triangle():
    q1 = eval(input("Enter the first charge(in C): "))
    q2 = eval(input("Enter the second charge(in C): "))
    q2 = abs(q2)
    q3 = eval(input("Enter the third charge(in C): "))
    a = eval(input("Enter the horizontal distance, a: "))
    b = eval(input("Enter the vertical distance, b: "))

    x_comp = -1*(ke*q3)/(a**2)
    y_comp = -1*(ke*q2)/(b**2)
    f_x = -1*(ke*q1*q3)/(a**2)
    f_y = -1*(ke*q1*q2)/(b**2)

    print("a)")
    print((x_comp, y_comp))
    print("Units: N/C, N/C")
    print("b)")
    print((f_x, f_y))
    print("Units: N, N")

def field_at_point():
    q1 = eval(input("Enter the first charge(in C): "))
    q1 = abs(q1)
    q2 = eval(input("Enter the second charge(in C): "))
    q2 = abs(q2)
    q3 = eval(input("Enter the third charge(in C): "))
    q3 = abs(q3)
    l1 = eval(input("Enter L1: "))
    l2 = eval(input("Enter L2: "))
    a = eval(input("a) Enter the x-coordinate of the position: "))

    field_x = ke * ((q2/(a**2))+(q3/(a-l2)**2)-(q1/(l1+a)**2))

    deg1 = atan(a/l1)
    deg2 = atan(a/l2)
    r1 = (a**2)+(l1**2)
    r2 = (a**2)+(l2**2)

    x_comp = ke * (((q1/r1)*cos(deg1))+((q3/r2)*cos(deg2)))
    y_comp = ke * (((q3/r2)*sin(deg2))+(q2/(a**2))-((q1/r1)*sin(deg1)))
    field_y = sqrt((x_comp)**2+(y_comp)**2)
    angle = 180 - (atan(y_comp/x_comp)*(180/pi)) 
    

    print("a)")
    print(field_x)
    print("Units: N/C")
    print("b)")
    print(field_y)
    print("Units: N/C")
    print("c)")
    print(angle)
    print("Units: deg")

def bent_rod():
    r = eval(input("Enter the radius(in m): "))
    q = eval(input("Enter the total charge on the semicircle(in C): "))
    q2 = eval(input("b)Enter the charge placed at centre of semicircle(in C): "))

    lamb = q/(2*r)
    force = (pi*ke*q*q2)/(4*r**2)

    print(lamb)
    print("Units: C/m")
    print(force)
    print("Units: N")

def two_dipoles():
    d = eval(input("Enter the spacing(in m): "))
    y = eval(input("Enter the y-value of the field strength(in m): "))
    field = eval(input("Enter the field strength: "))
    s = d/2
    angle = atan(s/y)

    q = (field*(y**3)*2*pi*permitivity)/d
    e_field = (ke*q*2*sin(angle))/(y**2)
    
    print(q)
    print("Units: C")
    print(e_field)
    print("Units: N/C")

def electron_in_field():
    angle = eval(input("Enter the angle: "))
    angle = (angle*pi)/180
    speed = eval(input("Enter the speed: "))
    d = eval(input("Enter the distance the electron lands(in m): "))
    vx = speed*cos(angle)
    vy = speed*sin(angle)
    
    t = d/vx
    a = (2*vy)/t
    field = (m_e*a)/(e_q)

    t = vy/a
    spacing = 0.5*a*(t**2)

    print(field)
    print("Units: N/C")
    print(spacing)
    print("Units: m")


def main():
    print("Welcome to PyPHYS. Plug in values from your physics homework, get the answers.")
    print("This week's topic is on electric fields")
    print("Note: You will need to install NumPy for ball_hanging()")
    while True:
        print("Type any of these functions for whatever scenario you want: ")
        print("three_charges(), middle(), ball_hanging(), equilateral(), charge_and_field()")
        print("triangle(), field_at_point(), bent_rod(), two_dipoles(), electron_in_field()")
        print("Type 'Done' to exit the program")
        function = eval(input("Enter the function you want: "))
        if function == "Done":
            break
        elif function == "three_charges":
            three_charges()
        elif function == "middle":
            middle()
        elif function == "ball_hanging":
            ball_hanging()
        elif function == "equilateral":
            equilateral()
        elif function == "charge_and_field":
            charge_and_field()
        elif function == "triangle":
            triangle()
        elif function == "field_at_point":
            field_at_point()
        elif function == "bent_rod":
            bent_rod()
        elif function == "two_dipoles":
            two_dipoles()
        elif function == "electron_in_field":
            electron_in_field()
        else:
            print("Invalid function")

if __name__ == "__main__":
    main()