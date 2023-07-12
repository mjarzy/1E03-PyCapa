from math import*

question = eval(input("enter the question number: "))

if question == 1 :
    k = eval(input("the equation appears in the form y = Asin(kx)cos(wt) , enter the k value: "))
    k = k / 1.0
    wl = (2*pi) / k

    print("the wavelength of the waves is: " , wl , "m")

    question = eval(input("enter the question number: " ))
if question == 2 :
    L = eval(input("enter the length of the string in cm: "))
    F = eval(input("enter the frequency of the second-longest wavelength in Hz: "))
    F = F / 1.0
    L = L / 100.0
    L1 = 2*L
    L2 = L
    L3 = (2*L) / 3
    F3 = F * (3.0/2.0)

    print("the longest wavelength is: " , L1 , "m")
    print("the second longest wavelength is: " , L2 , "m")
    print("the third longest wavelength is: " , L3 , "m")
    print("the frequency of the third longest wavelength is: " , F3 , "Hz")

    question = eval(input("enter the question number: "))

if question == 3 :
    F = eval(input("enter the fundamental frequency: "))
    F = F / 1.0
    F2 = sqrt(2) * F

    print("the fundamental frequency is now: " , F2 , "Hz")

    question = eval(input("enter the question number: "))

if question == 4 :
    L = eval(input("enter the length of the wire in cm: "))
    M = eval(input("enter the mass of the steel wire in g: "))
    F = eval(input("enter the fundamental frequency: "))
    L = L / 100.0
    M = M / 1000.0
    F = F / 1.0
    g = 9.81
    m = ((4)*(F**2)*(M*L)) / (g)

    print("the mass of sculpture is: " , m , "kg")

    question = eval(input("enter the question number: "))

if question == 5 :
    u = eval(input("enter the linear mass density: "))
    L = eval(input("enter the length of the string between point P in m : "))
    m1 = eval(input("enter the lighter mass in kg : "))
    m2 = eval(input("enter the heavier mass in kg: "))
    
    u = u / 1.0
    L = L / 1.0
    m1 = m1 / 1.0
    m2 = m2/1.0
    g = 9.81

    T1 = g * m1
    T2 = g * m2
    Y = 1.0 / (2*L)
    x1 = Y * sqrt(T1 / u ) 
    x2 = Y * sqrt(T2 / u ) 
    
    n2 = x1 / (x2 - x1) 
    n1 = n2 + 1.0

    F = x1 * n1
    m3 = u * L

    M = ((4)*(F**2)*(m3)*(L)) / (g)
    
    print("the frequency of the vibrator is: " , F , "Hz")
    print("the maximum mass for which standing waves could be observed is: " , M , "kg")

    question = eval(input("enter the question number: "))

if question == 6 :
    x1 = eval(input("enter the distance speaker 2 is behind speaker 1 in cm: "))
    x2 = eval(input("enter the distance speaker 2 is in front speaker 1 in cm: "))
    x1 = x1 / 100.0
    x2 = x2 / 100.0
    x3 = x1 + x2

    wl = 2*(x3)

    y = (2*pi) * (x1 / wl)

    phi = (1*pi) - y

    print("the wavelength of the sound is: " , wl , "m")
    print("the phase difference between the two loudspeakers is: " , phi, "rad")

    question = eval(input("enter the question nunmber: "))

if question == 7 :
    wl = eval(input("enter the wavelength of the waves in m : "))
    v = eval(input("enter the speed of the waves in m/s : "))
    wl = wl / 1.0
    v = v / 1.0

    x = v / wl
    w = 2*pi*x

    phi = (2*pi) / 3 
    
    t = phi / w

    print("the minimal time is: " , t , "s")

    question = eval(input("enter the question number: "))

if question == 8 :
    D = eval(input("enter the distacne between the two microphones in m: "))
    v = eval(input("enter the speed of the sound in m/s "))
    t = eval(input("enter the time in ms: "))
    D = D / 1.0
    v = v / 1.0
    t = t * 1.0e-3

    x = t * v

    L1 = ((D**2) - (x**2)) / (2*x)

    y = (L1**2) + (D**2)

    L2 = sqrt(y)

    print("the distance L1 is: " , L1 , "m")
    print("the distance L2 is: " , L2 , "m")

    question = eval(input("enter the question number: "))

if question == 9 :
    f = eval(input("enter frequency: "))
    d = eval(input("enter the distance between the speakers in m: "))
    v = eval(input("enter the speed of sound in m/s : "))
    f = f / 1.0
    d = d / 1.0
    v = v / 1.0
    x = v / f

    L = ((d**2) - ((0.5**2)*(x**2))) / x

    print("the person is: " , L , "m away from the pole")

    question == eval(input("enter the question number: "))

if question == 10:
        deg = eval(input("is the angle given more than 90? ( 1 if it is, 0 if it is not: "))

        if deg == 1 :
            x = eval(input("enter the angle in deg(it better be more than 90 deg): "))
            SC = eval(input("enter the distance of the sound source from the center of your head in m: "))
            d = eval(input("enter the distance between the ears in cm: "))
            v = eval(input("enter the velocity of the sound in m/s: "))
            v = v / 1.0
            d1 = d / 200.0
            z = x - 90.0 
            y = radians(z)
            SB = SC * sin(y)
            CB = SC * cos(y)
            RB = CB - d1
            LB = CB + d1

            L1 = sqrt((SB**2)+(RB**2))
            L2 = sqrt((SB**2)+(LB**2))

            L = L2 - L1

            t = L / v

            print(t)

        if deg ==  0 :
            x = eval(input("enter the angle in deg(it better be less than 90 deg): "))
            SC = eval(input("enter the distance of the sound source from the center of your head in m: "))
            d = eval(input("enter the distance between the ears in cm: "))
            v = eval(input("enter the velocity of the sound in m/s: "))
            v = v / 1.0
            d1 = d / 200.0
            z = 90.0 - x 
            y = radians(z)
            SB = SC * sin(y)
            CB = SC * cos(y)
            RB = CB - d1
            LB = CB + d1

            L1 = sqrt((SB**2)+(RB**2))
            L2 = sqrt((SB**2)+(LB**2))

            L = L2 - L1

            t = L / v

            print("the difference in arrival times is: " , t , "s")

        question = eval(input("enter the question number: "))
                
if question == 11:
    a = eval(input("enter the surface area in m^2 : "))
    a = a / 1.0
    I = eval(input("enter the sound intensity in W / m^2: "))
    I  = I / 1.0

    P = I*a

    print("the power intercepted by the ear is: " , P , "W")
