from math import* 

question = eval(input("enter the question number: "))

if question == 1 :
    v = eval(input("enter the speed of the transverse waves in m/s: "))
    l = eval(input("enter the length of the string in m : "))
    m = eval(input("enter the mass of the string in kg: "))
    v = v / 1.0
    l = l / 1.0
    m = m / 1.0

    u = m / l
    T = (v**2)*(u)

    print("the required tension is: " , T , "N")

    question = eval(input("enter the question number: "))

if question == 2 :
    a = eval(input("the equation should be in the form y = Acos(kx-wt): enter the A value in cm: "))
    k = eval(input("enter the k value: "))
    w = eval(input("enter the w value: "))
    phi = eval(input("enter the phase angle in deg : "))
    a = a / 1.0
    k = k / 1.0
    w = w / 1.0
    phi = phi / 1.0

    d = (2*pi) / k

    c = (10 / phi)
    x = d*c

    print("the position along the x-axis of point b is : " , x , "cm")

    question = eval(input("enter the question number : "))

if question == 3 :
    a = eval(input("the equation should be in the form D(x,t) = Asin(kx-wt). enter the A value in m: "))
    k = eval(input("enter the k value: "))
    w = eval(input("enter the w value as positive: "))

    a = a / 1.0
    k = k /1.0
    w = w / 1.0

    wl = (2*pi) / k
    v = w/k

    print("the amplitude of the wave is: " , a , "m")
    print("the angular frequency of the wave is: ", w , "rad/s")
    print("the angular wave number is: " , k , "rad/m")
    print("the wavelength is : " , wl , "m")
    print("the speed of the wave is: " , v , "m/s")

    question = eval(input("enter the question number: "))

if question == 4 :
    T = eval(input("enter the period of the wave in ms: "))
    v = eval(input("enter the speed of the wave in m/s: "))
    x = eval(input("enter the displacement at x = 0 and t = 0  in cm: "))
    vd = eval(input("enter the downward speed of the wave in m/s: "))
    T = T * 1.0e-3
    v = v /1.0
    x = x / 100.0
    

    w = (2*pi) / T
    d = vd / (x*w)
    rad = atan(d)
    amp = x / cos(rad)
    phi = asin((-1*x)/amp)  + pi
    vmax = w*amp
    
    print("the amplitude of the wave is: " , amp , "m")
    print("the initial phase constant is: " , phi , "rad")
    print("the maximum transverse speed of the string is: " , vmax , "m/s")

    question = eval(input("enter the question number: "))

if question == 5 :
    l = eval(input("enter the length of the string in m: "))
    m = eval(input("enter the mass of string in g: "))
    f = eval(input("enter the frequency of the string in Hz: "))
    n = eval(input("enter the number of complete waves: "))
    pk = eval(input("enter the peak-to-valley distance in cm: "))
    l = l / 1.0
    m = m / 1000.0
    f = f / 1.0
    amp = pk / 200.0
    w = 2*pi*f
    u = m / l
    n = n / 1.0

    wl = l / n
    v = f*wl
    P = (0.5)*(u)*(w**2)*(amp**2)*(v)

    print("the power being supplied to the string is: " , P , "W")

    question = eval(input("enter the question number: "))

if question == 6 :
    part = eval(input("enter part (1,2,3,4): "))
    if part == 1 :
        w = eval(input("the equation should be in form y = Acos(kx-wt + c). enter the magnitude w value: "))
        k = eval(input("enter the k value: "))
        sign = eval(input("what is the sign infront of w value (0 for negative and 1 for positive: "))
        w = w/ 1.0
        k = k /1.0
        if sign == 0 :
            v = w / k
            print("the speed of the wave is: " , v ,"m/s")
        if sign == 1:
            v = w / k
            v = -1.0*v
            print("the speed of the wave is: " , v ,"m/s")
        part = eval(input("enter the part number(2,3,4): "))
    if part == 2 :
        w = eval(input("the equation should be in form y = Acos(kx-wt - c). enter the magnitude w value: "))
        k = eval(input("enter the k value: "))
        sign = eval(input("what is the sign infront of w value (0 for negative and 1 for positive: "))
        w = w/ 1.0
        k = k /1.0
        if sign == 0 :
            v = w / k
            print("the speed of the wave is: " , v ,"m/s")
        if sign == 1 :
            v = w / k
            v = -1.0*v
            print("the speed of the wave is: " , v ,"m/s")

        part = eval(input("enter the part number(3,4): "))

    if part == 3 :
        w = eval(input("the equation should be in form y = Acos(wt-kx). enter the w value: "))
        k = eval(input("enter the magnitude of the k value: "))
        sign = eval(input("what is the sign infront of k value (0 for negative and 1 for positive: "))
        w = w/ 1.0
        k = k /1.0
        if sign == 0 :
            v = w / k
            print("the speed of the wave is: " , v ,"m/s")
        if sign == 1 :
            v = w / k
            v = -1.0*v
            print("the speed of the wave is: " , v ,"m/s")

        part = eval(input("enter the part number(4) : "))

    if part == 4 :
        w = eval(input("the equation should be in form y = Acos(wt-kx+n). enter the w value: "))
        k = eval(input("enter the magnitude of the k value: "))
        sign = eval(input("what is the sign infront of k value (0 for negative and 1 for positive: "))
        w = w/ 1.0
        k = k /1.0
        if sign == 0 :
            v = w / k
            print("the speed of the wave is: " , v ,"m/s")
        if sign == 1 :
            v = w / k
            v = -1.0*v
            print("the speed of the wave is: " , v ,"m/s")
    question = eval(input("enter the question number: "))

if question == 7 :
    v1 = eval(input("enter the wave speed of string in m/s: "))
    t1 = eval(input("enter the tension of string in N: "))
    v2 = eval(input("enter the required wave speed in m/s: "))
    v1 = v1 / 1.0
    t1 = t1 / 1.0
    v2 = v2 / 1.0

    ratio = (v2**2) / (v1**2)

    t2 = ratio * t1

    print("the required tension is: " , t2 , "N")
    question = eval(input("enter the equestion number: "))

if question == 8 :
    w1 = eval(input("enter the wavelength in the air, in nm: "))
    w2 = eval(input("enter the wavelength in the solid, in nm: "))
    c = 3.0e8

    w1 = w1 * 1.0e-9
    w2 = w2 * 1.0e-9
    n = w1 / w2

    v = c / n

    f = v / w2

    print("the speed of light in the solid is: " , v , "m/s")
    print("the lighth's frequency in the solid is: " , f , "Hz")

    question = eval(input("enter the question number: "))

if question == 9 :
    u = eval(input("enter the linear density of the string in g/m: "))
    T = eval(input("enter the tension on the string: "))
    f = eval(input("enter the frequency: "))
    amp = eval(input("enter the maximum displacement in mm: "))
    x = eval(input("in the last part enter the x value in m: "))
    t = eval(input("in the last part the t value in ms: "))
    u = u / 1000.0
    t = t / 1.0
    f = f / 1.0
    amp = amp / 1000.0
    x = x / 1.0
    t = t*1.0e-3
    T = T / 1.0

    v = sqrt(T / u)
    wl = v / f

    phi = 4.71

    w = 2*pi*f
    k = (2*pi) / wl

    Z = (k*x)
    Z1 = (w*t)
    Z2 = 4.71
    Z3 = Z - Z1 +Z2
    y = amp*sin(Z3)
    
   
    

    print("the speed of the string is: " , v  , "m/s")
    print("the wavelength is: " , wl , "m")
    print("the amplitude of the wave is:" , amp , "m")
    print("the phase constant is: " , phi , "rad")
    print("the displacement is: ", y , "m . the answer is either the positive or negative value, you have 10 tries.")
    
    
        
        
    

    
    
