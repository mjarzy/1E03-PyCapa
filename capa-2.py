# PyPHYS2.py
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

def planes():
    x = eval(input("Enter the x component of the field (N/C): "))
    y = eval(input("Enter the y component of the field (N/C): "))
    area = eval(input("Enter the surface area (m^2): "))

    flux_yz = x * area
    flux_xz = y * area
    print("a)")
    print(flux_yz)
    print("Units: N*m^2/C")
    print("b)")
    print(flux_xz)
    print("Units: N*m^2/C")
    print("c)")
    print("0.00")
    print("Units: N*m^2/C")

def linecircle():
    q = eval(input("Enter charge per unit length (in C/m): "))
    d = eval(input("Enter the distance (in m): "))
    r = eval(input("Enter the radius(in m): "))

    length = sqrt((r**2)-(d**2))

    flux = (2*q*length)/(permitivity)

    print(flux)
    print("Units: N*m^2/C")

def cube():
    Q = eval(input("Enter the point charge at the centre (in uC): "))
    L = eval(input("Enter the side length of the cube (in m): "))
    q = eval(input("Enter the charge of the six other charges (in uC): "))

    Q = Q*10**-6
    q = abs(q*10**-6)

    flux = (Q-6*q)/(6*permitivity)

    print(flux)
    print("Units: N*m^2/C")

def solidsphere():
    r = eval(input("Enter the radius (in cm): "))
    q = eval(input("Enter the charge (in uC): "))
    q = q*10**-6
    b = eval(input("b) Enter the distance (in cm): "))
    b = b/100.0
    c = eval(input("c) Enter the distance (in cm): "))
    c = c/100.0
    d = eval(input("d) Enter the distance (in cm): "))
    d = d/100.0

    field_one = ke*(q/(r)**3)*b
    field_two = ke*(q/(c)**2)
    field_three = ke*(q/(d)**2)

    print("a)")
    print("0.00")
    print("Units: N/c")
    print("b)")
    print(field_one)
    print("Units: N/C")
    print("c)")
    print(field_two)
    print("Units: N/C")
    print("d)")
    print(field_three)
    print("Units: N/C")

def insulating():
    d = eval(input("Enter the diameter (in cm): "))
    d = (d/100.0)/2
    q = eval(input("Enter the charge (in uC): "))
    q = q*10**-6
    r = eval(input("a) Enter the radius (in cm): "))
    r = r/100.0

    v = (4.0/3)*pi*(d**3)
    density = q/v
    volume = (4.0/3)*pi*(r**3)
    charge = density * volume

    print("a)")
    print(charge)
    print("Units: C")
    print("b)")
    print(q)
    print("Units: C")

def fields():
    r = eval(input("Enter the radius (in cm): "))
    r = r/100.0
    q1 = eval(input("Enter the sphere charge (in uC): "))
    q1 = q1*10**-6
    ri = eval(input("Enter the inner radius (in cm): "))
    ri = ri/100.0
    ro = eval(input("Enter the outer radius (in cm): "))
    ro = ro/100.0
    q2 = eval(input("Enter the shell charge (in uC): "))
    q2 = abs(q2*10**-6)
    r1 = eval(input("b) Enter the radius (in cm): "))
    r1 = r1/100.0
    r2 = eval(input("d) Enter the radius (in cm): "))
    r2 = r2/100.0

    field_one = ke * (q1/(r1**2))
    q3 = q1 - q2
    field_two = ke *(q3/(r2**2))
    print(field_two)
    print("Units: N/C")
    print("a)")
    print("0.00")
    print("Units: N/C")
    print("b)")
    print(field_one)
    print("Units: N/C")
    print("c)")
    print("0.00")
    print("Units: N/C")
    print("d)")
    print(field_two)

def prism():
    a = eval(input("Enter a (in m): "))
    c = eval(input("Enter c (in m): "))
    f1 = eval(input("Enter the first term of the field (in N/C): "))
    f2 = eval(input("Enter the second term of the field WITHOUT the x^2 (in N/C): "))

    flux1 = (a**2) * (f1+f2*(a**2))
    flux2 = (a**2) * (f1+f2*(a+c)**2)
    flux = -1*flux1 + flux2

    Q = flux * permitivity

    print("a)")
    print(flux)
    print("Units: N*m^2/C")
    print("b)")
    print(Q)
    print("Units: C")


def shell():
    r = eval(input("Enter the radius (in m): "))
    l = eval(input("Enter the length (in m): "))
    p = eval(input("Enter the point radially outward (in m): "))
    field = eval(input("Enter the field (in N/C): "))

    q = (field * p)/(2*ke*l)

    print("a)")
    print(q)
    print("Units: C")
    print("b)")
    print("0.00")
    print("Units: N/C")


def copper():
    l = eval(input("Enter the length (in cm): "))
    l = l/100.0
    electrons = eval(input("Enter the number of electrons: "))
    p = eval(input("Enter the distance above the centre of the top surface of the plate (in mm): "))
    p = p/1000.0

    density = (e_q * electrons)/(l**2)
    field = -1 * density/(2*permitivity)

    print("a)")
    print(field)
    print("Units: N/C")
    print("b)")
    print("0.00")
    print("Units: N/C")

def hollow():
    r = eval(input("Enter radius of the solid metal sphere (in cm): "))
    r = r/100.0
    ri = eval(input("Enter inner radius of hollow sphere (in cm): "))
    ri = ri/100.0
    ro = eval(input("Enter the outer radius of the hollow sphere (in cm): "))
    ro = ro/100.0
    d1 = eval(input("Enter the first distance (in cm): "))
    d1 = d1/100.0
    field = eval(input("Enter the magnitude of the field (in N/C): "))
    d2 = eval(input("Enter the second distance (in cm): "))
    d2 = d2/100.0
    
    q1 = -1 * (4*pi*(d1**2)*field*permitivity)
    q2 = 4*pi*(d2**2)*field*permitivity

    print("a)")
    print(q1)
    print("Units: C")
    print("b)")
    print(-1*q1)
    print("Units: C")
    print("c)")
    print(q2)
    print("Units: C")
    
def main():
    print("Welcome to PyPHYS. Plug in values from your physics homework, get the answers.")
    print("This week's topic is on electric fields")
    print("Note: You will need to install NumPy for ball_hanging()")
    while True:
            print("Type any of these functions for whatever scenario you want: ")
            print("planes(), linecircle(), cube(), solidsphere(), insulating()")
            print("fields(), prism(), shell(), copper(), hollow()")
            print("Type 'Done' to exit the program")
            function = input("Enter the function you want: ")
            if function == "Done":
                break
            elif function == "planes":
                planes()
            elif function == "linecircle":
                linecircle()
            elif function == "cube":
                cube()
            elif function == "solidsphere":
                solidsphere()
            elif function == "insulating":
                insulating()
            elif function == "fields":
                fields()
            elif function == "prism":
                prism()
            elif function == "shell":
                shell()
            elif function == "copper":
                copper()
            elif function == "hollow":
                hollow()
            else:
                print("Invalid function")

if __name__ == "__main__":
    main()
            