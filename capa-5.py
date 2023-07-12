# february 9 ,2013
# capa 5
from math import*
question = eval(input("enter the question number: "))

def main(question):
        if question == 1 :
            battery = eval(input("what is your car battery rated at: "))
            battery = float(battery)
            chargeleft = battery*3600
            print((chargeleft, "C of charge has left the battery"))
            question = eval(input("enter the question number(0 to quit): "))

        if question == 2 :
            D = eval(input(" please input the diameter of the beam in mm: "))
            D = D / 1000.0
            R = D / 2.0
            I = eval(input("please input the current of the beam in uA: "))
            I = float(I)
            I = I * (1.0e-6)
            q = 1.6e-19
            N = I / q
            A = (pi)*(R**2)
            J = I / A

            print(("the number of electrons that hit the screen per second is : " , N))
            print(("the current density of the electron beam is : " , J , "A/m^2"))
            
            question = eval(input("enter the question number(0 to quit): "))

        if question == 3 :
            Q = eval(input("please input the charge carried by the sphere: "))
            W = eval(input("please input the angular velocity of ratoaiton: "))
            Q = float(Q)
            W = float(W)
            I = (Q*W) / (2*pi)
            print(("the average current represented by the spinning sphere is : " , I , "A"))

            question = eval(input("enter the question number(0 to quit): "))
            
        if question == 4 :
            b = eval(input("Please enter the beam produced by the generator (in MeV): "))
            I = eval(input("Please enter the current: "))
            I = float(I)
            b = (b*(10.0**6.0))
            q = 1.6e-19
            m = 3.3475e-27
            B = b*q
            x = (B*2.0)/(m)
            V = sqrt(x)
            t = q / I

            d = V*t
            print(("the atoms are: " , d , "meters apart"))

            question = eval(input("enter the question number(0 to quit): "))


        if question == 5 :
            R = eval(input("What is your initial resistance: " ))
            R = float(R)
            f = eval(input("By how much is it lengthened by: "))
            f = float(f)

            N = R * (f**2)
            print(("the new resistance is: " , N , "ohm"))
            
            question = eval(input("enter the question number(0 to quit): "))


        if question == 6 :
            S = eval(input("please enter the length of each side in mm : "))
            S = float(S)
            R1 = eval(input("please enter the resistivity of the first material: "))
            L1 = eval(input("please enter the length of material 1 in cm: "))
            L1 = L1 / 100.0
            R2 = eval(input("please enter the resistivity of material 2: "))
            L2 = eval(input("please enter the length of material 2 in cm: "))
            L2 = L2 / 100.0
            S = S / 1000
            A = S**2.0

            r1 = (R1 * L1) / (A)
            r2 = (R2 * L2) / (A)

            r = r1 + r2
            print(("the total resistance between the ends of the rods is: " , r , "ohm"))

            question = eval(input("enter the question number(0 to quit): "))

            
        if question == 7 :
            d = eval(input("Please enter the diameter of the line in cm: "))
            d = d/100
            l = eval(input("Pleas enter the length of the line in km: "))
            l = l*1000.0
            I = eval(input("Please enter the current carried by the wire: "))
            I = float(I)
            n = eval(input("please enter the free charge density(0 to quit): "))
            n = float(n)
            q = 1.6e-19
            r = d / 2.0
            A = (pi)*(r**2)
            V = (I) / (n*q*A)
            t = l / V

            print(("The time it takes for the electron to travel the line is : " , t , "seconds"))

            question = eval(input("enter the question number(0 to quit): "))

        if question == 8 :
            V = eval(input("please enter the electron drift speed: "))
            V = float(V)
            T = eval(input("Please enter the mean free time between collisions: "))
            T = float(T)
            m = 9.11e-31
            q = 1.6e-19
            E = (m*V) / (q*T)
            print(("the strength electric field is : " , E , " N/C"))

            question = eval(input("enter the question number(0 to quit): "))

        if question == 9 :
            V1 = eval(input("please input the voltage of the main power line: "))
            V1 = float(V1)
            L = eval(input("please input the length of each wire in m : "))
            L = float(L)
            r = eval(input("please input the resistance of each wire: "))
            D = eval(input("please input the meters part of the resistance per meter: "))
            I = eval(input("please input the load current(0 to quit): "))
            I = float(I)
            D = float(D)
            r = float(r)
            R = r/D
            R1 = L * R
            V = V1 - ((I)*(R1*2))
            P = V * I
            PL = (I**2)*(R1*2)
            print(("the voltage at the customer's house is: " , V , "volts"))
            print(("the power that the customer is receiving is : " , P , " W "))
            print(("the power lost in the copper wires is : , " , PL , "W"))

            question = eval(input("enter the question number(0 to quit): "))
                      
        if question == 10 :
            C = eval(input("Please input the change in the current of the resistor: "))
            C = float(C)
            V1 = eval(input("please input the intial voltage: "))
            V1= float(V1)
            V2 = eval(input("Please input the final voltage: "))
            V2 = float(V2)
            R = (V1 - V2 ) / C
            print(("the resistance of the resistor is : " , R , "ohm"))

            question = eval(input("enter the question number(0 to quit): "))

        if question == 11 :
            S = eval(input("Please enter the voltage produced by the surge: "))
            S = float(S)
            V = eval(input("please enter the voltage of the lightbulb: "))
            V = float(V)
            W = eval(input("please enter the wattage of the lightbulb: "))
            W = float(W)

            C = (S**2) / (V**2)
            c = (C*100) - 100
            print(("the output will increase by : " , c , "%"))

            question = eval(input("enter the question number(0 to quit): "))

        if question == 12 :
            M = eval(input("Please enter the mass of avaiable material in grams: "))
            M = float(M)
            P = eval(input("Please enter the resistivity of the material : "))
            P - float(P)
            D = eval(input("please enter the density of material in g/cm^3 : "))
            D = float(D)
            R = eval(input("Please enter the total required resistance : "))
            R = float(R)
            V = M / D
            V = float(V) / 1.0e6

            X = (V*R) / (P)
            L = sqrt(X)
            Y = (V) / (pi*L)
            r = sqrt(Y)
            dia = r*2
            print((" the required length is : " , L , "meters"))
            print((" the diameter of the wire is : " , dia , "meters"))


            question = eval(input("enter the question number(0 to quit): "))

        if question == 0 :
            print("You are done")
try:
    main(question)
except:
    main(question)
