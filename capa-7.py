from math import*

question = eval(input("enter the question number: "))

if question == 1 :
    v = eval(input("enter the electron velocity: "))
    v = v/1.0
    a = eval(input("enter the acceleration: "))
    a = a/1.0
    E = eval(input("enter the magnitude of the eletric field: "))
    q = 1.6e-19
    m = 9.11e-31
    X = -1*q*E
    Y = m*a
    Z = q*v
    By= (X-Y)/Z
    # to get the y component sum of all forces = ma
    # so -Fe - ma = q*v*B
    # (-(q*E) - ma) / (q*v) = B
    print("the y component of the magnectic field in the region is " , By , "T")
    print("the z component of the magnetic field in the region is 0 T ")
    question = eval(input("enter the question number: "))

if question == 2 :
    L = eval(input("enter the length of each side in cm: "))
    L = L / 100.0
    I = eval(input("enter the current: "))
    I = I / 1.0
    B = eval(input("enter the magnitude of the magnetic field: "))
    B = B/1.0
    H = sqrt(L**2 + L**2)
    S = sin(pi/4)
    F_ab = 0
    F_bc = I*L*B
    F_cd = I*H*B*S
    F_da = I*H*B
    # just use F = I * L *Bsin(theta)
    # F_ab is zero because the angel is 180 therefore no force
    # in segment cd the angle is 45 between B and L. and the legth if the hypotenuse
    # in segment bc and da the angel is 90 so sin90 = 1. so its jus the length of that segment times B.
    
    print("the force on segment ab is : " , F_ab , "N")
    print("the force on segment bc is : " , F_bc , "N")
    print("the force on segment cd is : " , F_cd , "N")
    print("the force on segment da is : " , F_da , "N")
    question = eval(input("enter the question number: "))

if question == 3 :
    M = eval(input("enter the mass of the wire in kg: "))
    M = M/1.0
    L = eval(input("enter the total length of wire in m: "))
    N = eval(input("enter the number of turns in the coil: "))
    N = N/1.0
    I = eval(input("enter the current: "))
    I = I/1.0    
    B = eval(input("enter the magnitude of the magnetic field: "))
    G = 9.8
    S = L / (N*4)
    A = S**2.0
    X = M*G*(S/2.0)
    Y = N*I*A*B
    theta = degrees(atan(X/Y))
    phi = 90 - theta
    D = radians(theta)
    F = sin(D)
    T = N*I*A*B*F
    # number of turns times 4 is the amount of segments the total length will be split into
    # with that get the side length and solve for the area
    # torque due to gravity will me mglcos(phi)/ 2 . draw a FBD to visualize.
    # the torque due to gravity will equal torque due to magnetic field.
    # t_m = U *B*sin(theta) >> t_m = I * A * B* sin(phi)
    # set the two torques equal to each other and solve for theta = 90 - phi (refer to FBD to know why)
    # use phi to solve for torque 
    print("the angle between the plane and the vertical is: " , phi , "degrees")
    print("the torque acting on the coil due to the magnetic field is: " , T , "N")
    question = eval(input("enter the question number: "))


if question == 4 :
    V = eval(input("enter the potential difference in kV: "))
    V = V*1000.0
    B = eval(input("enter the magnitude of the magnetic field: "))
    B = B/1.0
    M1 = 238.0 * 1.66e-27
    M2 = 235.0 * 1.66e-27
    q = 1.6e-19
    X1 = (2*q*V)/ M1
    X2 = (2*q*V)/ M2
    v1 = sqrt(X1)
    v2 = sqrt(X2)
    r1 = (M1*v1) / (q*B)
    r2 = (M2*v2) / (q*B)

    # r = (M*V) / (q*B)
    # mass is given . use the potential difference to solve for v . qV = 0.5*m*v^2
    # v = sqrt(2*q*V / M)
    # just solve for r by subbing it into the r equation and use the appropriate masses

    print("the radius of the circular path for the uranium-238 atom is: " , r1 , "meters")
    print("the radies of the circular path for the uranium 235 atom is: " , r2 , "meters")
    question = eval(input("enter the question number: "))

if question == 5 :
    E = eval(input("enter the energy of the protons is MeV: "))
    E = E*1.0e6
    B = eval(input("enter the magnitude of the magnetic field: "))
    B = B/1.0
    q = 1.6e-19
    K = E * q
    M = 1.67e-27
    X = (2*K) / M
    V = sqrt(X)
    R = (M*V)/(q*B)
    # use the energy of the proton and convert it to joules and solve for V .
    # and just sub that v into the r equation.
    print(" the required radius of the cyclotron is: " , R , "meters")
    question = eval(input("enter the question number: "))

if question == 6 :
    I = eval(input("enter the current of the probe in mA: "))
    I = I * 1.0e-3
    B1 = eval(input("enter the magnitude of the known magnetic field: "))
    B1 = B1 / 1.0
    V1 = eval(input("enter the Hall voltage in the known magnetic field in uV: "))
    V1 = V1 * 1.0e-6
    V2 = eval(input("enter the hall voltage in the unknown magnetic field in uV: "))
    V2 = V2 * 1.0e-6
    D = eval(input("enter the thickness of the probe in mm: "))
    D = D/1000.0
    q = 1.6e-19
    
    
    X = (V2/V1)    
    B2 = X*B1
    N = (I*B1) / (V1*q*D)

    #Vh = (I*B) / (N * q *D) is the main equation
    # Vh has a linear proportionality to B.
    # just ratio the given values and solve for B2 ,
    # and sub in the corresponding values to solve for N. 
    #
    
    print("the magnitude of the unknown field is: " , B2 , "T")
    print("the charge carrier density is : " , N , "m^-3")
    question = eval(input("enter the question number: "))

if question == 7 :
    E = eval(input("enter the kinetic energy of the proton in MeV: "))
    q = 1.6e-19
    E = E*(1.0e6)*q
    M = 1.67e-27    
    A = eval(input("enter the angle of entry of the proton: "))
    B = eval(input("enter the magnitude of the magnetic field: "))
    S = radians(A)
    F = sin(S)
    X = sqrt(2*E*M)
    R = (X)/(B*q*F)
    # you can use kinetic energy to solve for v but
    # k can also expressed in term of momentum ( p = mv ) in the equation
    # r = (m*v) / (q*B*sin(theta))
    # p = sqrt(2*M*E) just convert K to joules
    # its the same same if you were to isolate for v using kinetic energy.
    # hence R = (sqrt(2*E*M)) / (B*q*sin(45))
    # or v = sqrt(2*K / M ) then sub that value into r = (M*v) / (q*B*sin(45))
    print("the distance x is: " , R ,"meters")
    print("the entry and exit angles are the same")
        
    question = eval(input("enter the question number: "))

if question == 8:
    T = eval(input("enter the torque experienced: "))
    T = T / 1.0
    A = eval(input("enter the angle: "))
    A = A / 1.0
    D = radians(A)
    F = sin(D)
    B = eval(input("enter the magnitude of the magnetic field: "))
    B = B/1.0

    U = T / (B*F)
    # torque = U * B * sin(theta)
    # isolate for U and sub in the givens

    print(" the magnitude of its magnetic dipole moment is : " , U , "N*m/T")
    question = eval(input("enter the question number: "))

if question == 9 :
    B = eval(input("enter the magnetic field strength: "))
    B = B / 1.0
    D = eval(input("enter the spacing between the entrance and exit hole in cm: "))
    R = D / 200.0
    q = 1.6e-19
    u = 1.66e-27
    M1 = 28*u
    M2 = 32*u
    M3 = 28*u
    X1 = 2*M1
    X2 = 2*M2
    X3 = 2*M3
    X = (B**2)*(R**2)*(q)
    V1 = X / X1
    V2 = X / X2
    V3 = X / X3

    # since the diameter is given the radius of the circular is know. the kinetic energy can be expressed interms of q B and r
    
    # K = (q^2 * B^2 * r^2) / 2m
    # K = q*V
    # and just solve for V with each mass
    # and isolate for V (potential difference)

    print(" the potential differene required for N2+ is : " , V1 , "V")
    print(" the potential difference required for O2+ is : ", V2 , "V")
    print(" the potential difference required for CO+ is : ", V3 , "V")
    question = eval(input("enter the question number: "))

if question == 10 :
    L = eval(input("enter the length of the loop in cm: "))
    L = L / 100.0
    W = eval(input("enter the width of the loop in cm: "))
    W = W / 100.0
    I = eval(input("enter the current: "))
    I = I / 1.0
    M = eval(input("enter the mass in grams: "))
    N = eval(input("enter the number of turns in the loop: "))
    N = N/1.0
    M = M / 1000.0
    G = 9.8
    A = L*W
    
    B = (M*G*W) / ( 2*N*I*A)
    # B has to provide a torque to counteract the torque due to the hanging mass
    # the hanging mass will be torque = m*g*w/2
    # set that equal to torque =N* I*A*B*sin(theta) . in this case there is no theta needed so. torque = N*I*A*B
    # just isolate for B and solve
    print(" the required magnetic field strength is: " , B , "T")
    question = eval(input("enter the question number(0 to quit): "))

if question == 0 :

    print(" you are done")
