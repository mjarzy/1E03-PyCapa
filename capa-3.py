# PyPHYS3.py
""" Handling physics questions
This program can compute certain physics scenarios that may pop up
when doing physics problems. It is written by Dave Gumba. Just
run the module and follow the instructions!

NumPy: http://www.scipy.org/scipylib/download.html
"""

from math import *

ke = 8.99*10**9
g = 9.8
permitivity = 8.85*10**-12
e_q = 1.602*10**-19
m_e = 9.11*10**-31
m_p = 1.67*10**-27
a_m = 1.66*10**-27

def easy():
    field = eval(input("Enter the field (in V/m): "))
    charge = eval(input("Enter the charge (in C): "))
    x = eval(input("Enter the x-coordinate (in cm): "))
    x = x/100.0

    U = -1*charge*field*x
    difference = -1*field*x

    print("a)")
    print(U)
    print("Units: J")
    print("b)")
    print(difference)
    print("Units: V")

def points():
    q1 = eval(input("Enter the point charges (in uC): "))
    q1 = q1*10**-6
    x = eval(input("Enter the x-coordinate (in m): "))
    y = eval(input("Enter the y-coordinate (in m): "))
    q2 = eval(input("Enter the third charge (in uC): "))
    q2 = abs(q2*10**-6)

    V = 2*ke*(q1/x)*cos(atan(y/x))
    J = -1*ke*2*((q1*q2*cos(atan(y/x)))/x)

    print("a)")
    print(V)
    print("Units: V")
    print("b)")
    print(J)
    print("Units: J")

def electron():
    x = eval(input("Enter the distance from the electron to the ring (in m): "))
    s = eval(input("Enter the linear charge density (in nC/m): "))
    s = s*10**-9
    r = eval(input("Enter the radius (in m): "))

    part1 = (-1*2*e_q)/(m_e)
    part2 = ((2*pi*ke*s*r)/(sqrt(r**2+x**2))) - 2*pi*ke*s
    velocity = sqrt(part1*part2)

    print(velocity)
    print("Units: m/s")
                
def wire():
    d = eval(input("Enter the charge density (in C/m): "))

    V = ke*d*(pi+2*log(3))

    print(V)
    print("Units: V")

def twoshells():
    r1 = eval(input("Enter the first radius (in cm): "))
    r1 = r1/100.0
    q1 = eval(input("Enter the first charge (in nC): "))
    q1 = q1*10**-9
    r2 = eval(input("Enter the second radius (in cm): "))
    r2 = r2/100.0
    q2 = eval(input("Enter the second charge (in nC): "))
    q2 = abs(q2*10**-9)
    d1 = eval(input("b) Enter the distance (in cm): "))
    d1 = d1/100.0
    d2 = eval(input("c) Enter the distance (in cm): "))
    d2 = d2/100.0
    d3 = eval(input("d) Enter the distance (in cm): "))
    d3 = d3/100.0
    d4 = eval(input("e) Enter the distance (in cm): "))
    d4 = d4/100.0
    d5 = eval(input("f) Enter the distance (in cm): "))
    d5 = d5/100.0

    b = (ke*q1)/(d1**2)
    c = (ke*(q1-q2))/(d2**2)
    d = ke*((q1/r1)-(q2/r2))
    e = ke*((q1/d4)-(q2/r2))
    f = ke*((q1-q2)/d5)

    print("a)")
    print("0.00")
    print("Units: N/C")
    print("b)")
    print(b)
    print("Units: N/C")
    print("c)")
    print(c)
    print("Units: N/C")
    print("d)")
    print(d)
    print("Units: V")
    print("e)")
    print(e)
    print("Units: V")
    print("f)")
    print(f)
    print("Units: V")

def sheet():
    sdensity = eval(input("Enter the surface charge density (in nC/m^2): "))
    sdensity = sdensity*10**-9
    ldensity = eval(input("Enter the linear charge density (in nC/m): "))
    ldensity = ldensity*10**-9
    x = eval(input("Enter the x-coordinate (in m): "))
    v = eval(input("Enter the potential at the origin (in kV): "))
    v = v*10**-3
    x2 = eval(input("Enter the x-coordinate being evaluated (in m): "))
    

def leap():
    v1 = eval(input("Enter v1 (in V): "))
    v2 = eval(input("Enter v2 (in V): "))
    v3 = eval(input("Enter v3 (in V): "))
    v = eval(input("Enter the proton's speed (in m/s): "))

    part1 = (v3*e_q)-(v1*e_q)-(0.5*m_p*(v**2))
    part2 = abs((2*part1)/m_p)
    speed = sqrt(part2)

    print(speed)
    print("Units: m/s")

def mercury():
    d = eval(input("Enter the nucleus' diameter (in fm): "))
    d = (d*10**-15)/2
    s = eval(input("Enter the proton's speed (in m/s): "))

    U = 0.5*(m_p)*(s**2)
    dmax = (ke*80*(e_q**2))/U
    r = dmax - d

    print(r)
    print("Units: m")

def alpha():
    s = eval(input("Enter the speed given WITHOUT the c: "))
    s = s*(3*10**8)

    d = ((e_q)*2*(e_q))/((4*pi*permitivity)*(s**2)*((2*m_p*a_m*4)/((m_p+(a_m*4)))))

    print(d)
    print("Units: m")

def drops():
    q = eval(input("Enter the charge (in nC): "))
    q = q*10**-9
    v = eval(input("Enter the potential (in V): "))

    r = ke*(q/v)
    ro = ((2.0)**(1.0/3))*r
    qt = 2*q
    vo = (ke*qt)/ro

    print(vo)
    print("Units: V")

def triangle():
    s = eval(input("Enter the length of each side (in nm): "))
    s = s*10**-9

    U = ke * (((3*(e_q)**2)/s)-(3*(e_q)**2)/(s/sqrt(3)))

    print(U)
    print("Units: J")

def square():
    m = eval(input("Enter the mass of the spheres (in g): "))
    m = m/1000.0
    q1 = eval(input("Enter the charges (in nC): "))
    q1 = q1*10**-9
    d = eval(input("Enter the distance (in cm): "))
    d = d/100.0

    v = sqrt(((((5.41*ke*((q1**2)/d))/4.0)*2.0)/m))

    print(v)
    print("Units: m/s")
    

print("Welcome to PyPHYS. Plug in values from your physics homework, get the answers.")
print("This week's topic is on electric potential")
print("Type any of these functions for whatever scenario you want: ")
print("easy(), points(), electron(), wire(), twoshells(), sheet(), leap(), mercury()")
print("alpha(), drops(), triangle(), square()")
