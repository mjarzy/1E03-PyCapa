from math import*

question = eval(input("enter the question number: "))


if question == 1 :
    A = eval(input("enter the value of a in m: "))
    B = eval(input("enter the value of b in m: "))
    I = eval(input("enter the current: "))
    O = eval(input("enter the angle in the diagram: "))
    O = O/1.0
    A = A/1.0
    B = B/1.0
    I = I/1.0
    O = radians(O)
    U = (pi*4e-7)
    X = (U*I*O) / (4*pi)
    Y = (1/A) - (1/B)
    M = X*Y
    print("the magnitude of B at P is: " , M , "T")
    question = eval(input("enter the question number: "))

if question == 2 :
    I = eval(input("enter the current carried by the conductors: "))
    A = eval(input("enter the the value for a in cm: "))
    A = A / 100.0
    I = I / 1.0
    U = (pi*4e-7)

    
    B2 = (U*I) / (4*pi*A)
    B3 = (U*I) / (6*pi*A)
    B1 = B2 + B2 + B3

    print("the magnetic field at point a is: " , B1 , "T")
    print("the magnetic field at point b is: " , B2 , "T")
    print("the magnitude of the field at C is 0")
    question = eval(input("enter the question number: "))

if question == 3:
    I1 = eval(input("enter the inner current: "))
    I2 = eval(input("enter the outer current: "))
    R = eval(input("enter the spacing shown in mm: "))
    I1 = I1/1.0
    I2 = I2/1.0
    R = R / 1000.0
    U = (pi*4e-7)
    I3 = I2 - I1

    B1 = (U*I1) / (2*pi*R)
    B2 = (U*I3) / (6*pi*R)

    print("the magnitude of the magnetic field at a is : " , B1 , "T")
    print("the magnitude of the magnetic field at b is : " , B2 , "T")
    question = eval(input("enter the question number: "))

if question == 4 :
    B1 = eval(input("enter the magnetic field at the distance in uT : "))
    D1 = eval(input("enter the distance given with the magnetic field : "))
    B2 = eval(input("enter the new magnetic field in uT: "))
    I = eval(input("enter the current that the two cords carry: "))
    D = eval(input("enter the distance between the wires in mm: "))
    R = eval(input("enter the distance at which the field is to be calculated in cm: "))
    R3 = eval(input("enter the value in the question as a decimal ie. one-tenth would be 0.1 :At what distance is it ______ as large: "))
    R4 = (R3)**-1
    D = D / 2000.0
    R = R/100.0
    R1 = R - D
    R2 = R + D
    U = (pi*4e-7)
    X = (U*I) / (2*pi)
    Y = (1/R1) - (1/R2)

    B3 = X*Y
    
    B1 = B1/1.0
    B2 = B2/1.0
    D1 = D1/100.0
    ratio = B1 / B2

    D2 = ratio * D1
    D3 = sqrt(R4) * R

    print("at this distance" , D2, "m" , "the field is " , B2 , "T")
    print("the magnetic field from the middle of the cord is : " , B3 , "T")
    print("the distance at which the field is" , R3 , "as large is : ", D3 , "m")
    print("the magnetic field outside of coaxial cable is: " , 0 , "T")
    question = eval(input("enter the question number: "))

if question == 5 :
    R = eval(input("enter the radius of the conductor in cm: "))
    I = eval(input("enter the current : "))
    R = R / 100.0
    I = I / 1.0
    r = R / 2
    A = pi*(R**2)
    J = I / A
    U = (pi*4e-7)
    B = (U*J*r)/ 2
    R1 = (U*I) / (B*2*pi)
    r1 = R1 - R
    

    print("the magnetic field at radius/2 is " , B , "T")
    print("the distance from the surface is : " ,r1 , "m")
    question = eval(input("enter the question number: "))

if question == 6 :
    D = eval(input("enter the diameter of the solenoid in m: "))
    L = eval(input("enter the length of the solenoid in m: "))
    I = eval(input("enter the current of the solenoid: "))
    N = eval(input("enter the number of turns in the solenoid: "))
    R = eval(input("enter the radius of the disk in m : "))
    R1 = eval(input("enter the inner radius of the annulus in cm: "))
    R2 = eval(input("ente the outer radius of the annulus in cm: "))
    R1 = R1 / 100.0
    R2 = R2 / 100.0
    r = D / 2.0
    I = I / 1.0
    N = N / 1.0
    A = pi*(r**2)
    X = (R2**2) - (R1**2)
    A1 = X*pi
    U = (pi*4e-7)
    B = (U*I*N) / (L)
    

    flux = B*A
    flux2 = B*A1

    print("the flux through the surface of the disk is: " , flux , "Wb")
    print("the flux through the annulus is: " , flux2 , "Wb")
    
    question = eval(input("enter the question number: "))

if question == 7 :
    R = eval(input("enter the radius of ring in cm: "))
    R = R / 100.0
    Q = eval(input("enter the total charge carried by the ring: "))
    Q = Q/1000000.0
    W = eval(input("enter the angular speed in rad/s: "))
    W = W / 1.0
    Q = Q / 1.0
    A = pi*(R**2)
    I = (Q*W) / (2*pi)
    Mo = I*A

    print("the magnetic moment of the ring is: " , Mo, "A*m^2")
    question = eval(input("enter the question number: "))

if question == 8 :
    N = eval(input("enter the number of turns: "))
    R = eval(input("enter the radius of the coils in m: "))
    D = eval(input("enter the distance between the coils: "))
    I = eval(input("enter the current in the coils: "))
    N = N/1.0
    R = R/1.0
    D = D/1.0
    I = I /1.0
    U = (pi*4e-7)
    X = (U*I*N) / R
    Y = (4.0/5.0)**(3.0/2.0)   # use biot-savarts law
    B = Y*X

    print("the magnetic field at the point is: " , B , "T")
    question = eval(input("enter the question number: "))

if question == 9:
    I1 = eval(input("enter the current carried by the wire: "))
    L = eval(input("enter the length of the loop in m: "))
    R = eval(input("ente the radius of the loop in m: "))
    I2 = eval(input("enter the current carried by the loop: "))
    I1 = I1/ 1.0
    L = L/ 1.0
    R = R/1.0
    I2 = I2/ 1.0
    U = (pi*4e-7)

    X = (U*I1*I2*L)
    Y = pi*R

    F = X/Y

    print("the magnitude of the force exerted on the loop is: " , F , "N")
    question = eval(input("enter zero to quit: "))

if question == 0 :
    print("you are done")
    
    
    
