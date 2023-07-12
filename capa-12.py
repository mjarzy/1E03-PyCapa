
from math import*
print("The final capa code, you are all welcome")
question = eval(input("enter the question number: "))

if question == 1 :
    v = eval(input("enter the speed of sound in m/s: "))
    f = eval(input("enter the frequency of the sound in Hz: "))
    d = eval(input("enter the distance between the slits in cm: "))
    wm = eval(input("enter the wavelength of the microwaves in cm: "))
    d2 = eval(input("enter the slit separation in the last part in um: "))
    wm = wm / 100.0
    c = 3.0e8
    d2 = d2 *1.0e-6
    v = v / 1.0
    f = f / 1.0
    d = d / 100.0
    wl= v / f
    theta = asin(wl/d)

    x = degrees(theta)    
    d1 = wm / (sin(theta))
    y = d2*sin(theta)
    f = c / y

    print("the angle is first order maximum is: " , x , "deg")
    print("the slit separation is: ", d1 , "m")
    print("the frequency of the light is: " , f , "Hz")
    
    question = eval(input("enter the question number: "))

if question == 2 :
    d = eval(input("enter the distance between the slits in mm: "))
    wl = eval(input("enter the wavelength in nm: "))
    l = eval(input("enter the distance between the slit and the screen in m: "))
    d = d / 1000.0
    wl = wl *1.0e-9
    l = l / 1.0

    Y = (l*wl) / d

    print("both of the answers are: " , Y , "m")

    question = eval(input("enter the question number: "))

if question == 3 :
    wl = eval(input("enter the wavelength in m: "))
    d = eval(input("enter the distance from the radio station to the receiver in mm: "))
    wl = wl / 1.0

    x = wl / 4

    print("the minimum distance is: " , x , "m")

    question = eval(input("enter the question number: "))

if question == 4 :
    wl = eval(input("enter the wavelength in nm: "))
    d = eval(input("enter the width of the slit in mm: "))
    y = eval(input("enter the distance between the central maximum and first minimum pattern in mm: "))
    wl = wl *1.0e-9
    d = d / 1000.0
    y = y / 1000.0

    L = (d*y) / (wl)
    w = y * 2

    print("distance the screen should be placed is : " , L , "m")
    print("the width of the central maximum is: " , w , "m")

    question = eval(input("enter the question number: "))

if question == 5 :
    n1 = eval(input("in the interference pattern, the _____ bright line of the lambda 1. fill in the blank with a number: "))
    n2 = eval(input("occurs at the same position as the _____ bright line of lambda 2. fill in the blank with a number: "))
    wl1 = eval(input("enter the wavelength of lambda 1 in nm: "))
    n1 = n1 / 1.0
    n2 = n2 / 1.0

    wl1 = wl1 / 1.0

    wl2 = (n1*wl1) / (n2)

    print("the wavelength of lambda 2 is: " , wl2 , "nm")

    question = eval(input("enter the question number: "))

if question == 6 :
    w = eval(input("enter the width of the slit in mm: "))
    l = eval(input("enter the distance beyond the slit in m: "))
    y = eval(input("enter the distance between the positions in mm: "))
    w = w / 1000.0
    l = l / 1.0
    y = y / 2000.0

    wl = (w*y) / l

    print("the wavelength of the light is: " , wl , "m")

    question = eval(input("enter the question number: " ))

if question == 7 :
    n = eval(input("enter the number of horizontal lines: "))
    D = eval(input("enter the diameter of the pupil in mm: "))
    wl = eval(input("enter the average wavelength in nm: "))
    n = n / 1.0
    D = D / 1000.0
    wl = wl* 1.0e-9

    Y = 1.22 * wl * n

    R = D / Y

    print(" the L/H ratio is: " , R) 

    question = eval(input("enter the question number: "))

if question == 8 :
    a = eval(input("enter the width on the opening in cm: "))
    f = eval(input("enter the frequency: "))
    v = eval(input("enter the speed of sound in m/s: "))
    l = eval(input("enter the distance to the wall in m: "))
    a = a / 100.0
    f = f / 1.0
    v = v / 1.0
    l = l / 1.0
    wl = v / f

    theta = asin(wl/a)
    Y = l *tan(theta)

    print("the distance the listener will hear a minimum is: " , Y ,"m")

    question = eval(input("enter the question number: "))

if question == 9 :
    d = eval(input("enter the distance between the lamps in m : "))
    D = eval(input("enter the pupil diameter in mm: "))
    wl = eval(input("enter the wavelength as it appears: "))
    d = d / 1.0
    D = D / 1000.0
    wl = wl / 1.0

    theta = 1.22 * (wl / D )
    L = (D*d) / (1.22*wl)

    print("the angular separation is: " , theta , "rad")
    print("the maximum distance is: " , L , "m")
    

    
    
    
