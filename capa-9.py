from math import*

question = eval(input("enter the question number: "))

if question == 1 :
    R = eval(input("enter the radius of the circle in cm: "))
    R = R / 100.0
    Ba = eval(input("the equation for the B field is in the form B(t) = a +bt . enter the a value: "))
    Bb = eval(input("the equation for the B field is in the form B(t) = a +bt . enter the b value: "))
    r = eval(input("enter the resistance in the wire: "))
    r = r / 1.0
    A = pi*(R**2)
    F = Ba*A
    E = Bb*A
    I = E / r

    print(" the magnetic flux through the loop is : " , F , "Wb")
    print(" the magnitude of the emf induced in the loop is : " , E , "V")
    print(" the magnitude of the induced current in the loop is : " , I , "A")
    
    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")

if question == 2 :
    F = eval(input("enter the force applied to the bar: "))
    F = F / 1.0
    V = eval(input("enter the speed of the bar in m/s : "))
    V = V/1.0
    R = eval(input("enter the resistance: "))
    R = R/1.0
    I = ((F*V)/ R )**0.5
    P1 = (I**2) * R
    P2 = F*V

    print(" the current through the resistor is : " , I , "A")
    print(" the rate at which energy is delivered to the resistor is : " , P1 , "W")
    print(" the mechanical power delivered by the force is : " , P2 , "W")

    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")

    
if question == 3 :
    d = eval(input("enter the distance betwen the two plates in m :"))
    R3 = eval(input("enter the value of R3 : "))
    R1 = eval(input("enter the value of R1 : "))
    R2 = eval(input("enter the value of R2 : "))
    v1 = eval(input("enter the first speed value that appears in the sentence: "))
    v2 = eval(input("enter the second speed value that appears in the sentence: "))
    B = eval(input("enter the magnitude of the magnetic field: "))
    d = d/1.0
    R3 = R3 / 1.0
    R2 = R2 / 1.0
    R1 = R1 / 1.0
    v1 = v1 / 1.0
    v2 = v2 / 1.0
    B = B / 1.0
    X = (v1*R2) - (v2*R1)
    Y = (R1*R3) + (R3*R2) + (R1*R2)
    Z = B*d
    I = Z*(X/Y)

    print("the current through the " , R3 , "ohm resistor is : " , I , "A")

    print("")
    print("")
    question = eval(input("enter the question number : "))
    print("")
    print("")
    
if question == 4 :
    N = eval(input("enter the number of turns in the coil: "))
    R = eval(input("enter the resistance of the coil : "))
    A = eval(input("enter the cross sectional area in m^2 : "))
    Q = eval(input("enter the total charge that passes through the coil: "))
    N  = N / 1.0
    R = R / 1.0
    A = A / 1.0
    Q = Q / 1.0
    F = (Q*R) / N
    B = F / A

    print(" the  magnitude of B is : " , B , "T")

    print("")
    print("")
    question = eval(input("enter the question number : "))
    print("")
    print("")
    
if question == 5 :
    L = eval(input("enter the length of the rod in m: "))
    V = eval(input("enter the velcoity of the rod in m/s :"))
    I = eval(input("enter the current in mA : "))
    R = eval(input("enter the distance between the rod and the wire in cm: "))
    L = L / 1.0
    V = V / 1.0
    I = I * 1.0e-3
    R = R / 100.0
    U = (pi*4.0e-7)
    X = (U*I*V ) / (2*pi)
    Y = log(1 + (L/R))
    E = X*Y

    
    print("the magnitude of the emf in the rod is : " , E , "V")

    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")
    
if question == 6 :
    L = eval(input("enter the inductance of the coil in H: "))
    I1 = eval(input("enter the initial current : "))
    I2 = eval(input("enter the final current: "))
    t = eval(input("enter the time it takes for the current to change: "))
    L = L / 1.0
    I1 = I1 / 1.0
    I2 = I2 / 1.0
    t = t / 1.0

    dI = I2 - I1
    dt = t

    E = L*(dI / dt)

    print("the magnitude of the average induced emf is : " , E , "V")

    print("")
    print("")
    question = eval(input("enter the question number : "))
    print("")
    print("")
    
if question == 7 :
    E = eval(input("enter the emf in V : "))
    L = eval(input("enter the inductance in mH: "))
    R = eval(input("enter the resistance : "))
    t = eval(input("enter the time stated in part b in us: "))
    P = eval(input("enter the percent the current has to reach of its maximum value i.e enter 55.4% as 55.4 not 0.554 : "))
    P = P / 100.0
    t = t * 1.0e-6
    E = E / 1.0
    L = L *1.0e-3
    R = R / 1.0

    tau = L / R
    X = -1*(t/tau)
    If = E/R
    I = If *(1-e**X)
    Y = (1- P )
    t2 = log(Y) * tau *-1.0

    print(" the time constant of the circuit is: " , tau, "s")
    print(" the current in the circuit after" , t , "s is" , I , "A")
    print(" the final steady state current is: " , If , "A")
    print(" the time it takes for the current to reach" , P*100 , "% of its maximum value is: " , t2 , "s")

    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")
    
if question == 8 :
    R1 = eval(input("enter the resistance of R1 : "))
    R2 = eval(input("enter the resistance of R2 : "))
    L = eval(input("enter the inductance L : "))
    E = eval(input("enter the emf: "))
    E2 = eval(input("enter the final voltage across in the inductor: "))
    E2 = E2 / 1.0
    R1 = R1 / 1.0
    R2 = R2 / 1.0
    L = L / 1.0
    E = E / 1.0
    
    

    Rp =((1/R1) + (1/R2))**-1
    Rs = R1 + R2
    
    I = E / Rp
    V1 = I * R1
    V2 = I * R2
    V3 = V1 + V2
    tau = L / Rs
    t2 = log(E2/V3) * tau *-1.0
    print(" the current in the inductor after a long time is: " , I , "A")
    print(" the initial voltage across R1 is : " , V1 , "V")
    print(" the initial voltage across R2 : " , V2 , "V")
    print(" the intial voltage across the inductor is: , " , V3 , "V")
    print(" the time it takes for the voltage to drop to" , E2 , "V is: ", t2 , "s") 
    
    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")
    
if question == 9:
    B = eval(input("enter the magnetic field inside the conductor: "))
    D = eval(input("enter the diameter of the solenoid in cm: "))
    L = eval(input("enter the length of the solenoid in cm: "))
    B = B / 1.0
    R = D / 200.0
    L = L / 100.0
    V = (pi*(R**2))*L
    u = (pi*4.0e-7)

    U = (B**2) / (2*u)
    ub = U*V

    print("the magnetic energy density in the field is: " , U , "J/m^3")
    print("the energy stored in the magnetic field is: " , ub , "J")
    print("")
    print("")
    question = eval(input("enter the question number: "))
    print("")
    print("")
    
if question == 10 :
    N = eval(input("enter the number of turns in the coil: "))
    L = eval(input("enter the side length in cm : "))
    R = eval(input("enter the rpm of the coil: "))
    B = eval(input("enter the strength of the magnetic field: "))
    N = N / 1.0
    L = L / 100.0
    R = R / 1.0
    B = B / 1.0
    w = (R*pi) / (30)
    A = (L**2)
    E = N*A*B*w
    print("the maximum emf induced by the field is: " , E , " V ")
    eval(input("press enter to quit."))
