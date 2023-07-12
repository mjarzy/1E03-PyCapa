from math import*
import math

def main():

    print("CAPA 6")

    question = eval(input("Enter The Question Number (1-14, 0 to exit): "))

    if question == 1 :
        r1,r2,r3,r4,r5,r6 = eval(input("Enter the values of resistance, in order of R1 to R5, with each value seperated by a comma: "))
        ra = (1.0/r3) + (1.0/r4)
        ra = (1.0/ra)
        rb = r5 + r6
        rc = (1.0/ra) + (1.0/rb)
        rc = (1.0/rc)
        rd = rc + r2
        re = (1.0/r1) + (1.0/rd)
        rt = (1.0/re)
        print("The total resistance between point A and B is:",rt,"Ohms.")
        question = eval(input("enter the question number: "))

    if question == 2 :
        r1,r4,r5 = eval(input("Enter the resistances in Ohms for resistor 1, 4, and 5, all seperated by commas: "))
        a1,a2,a3 = eval(input("Enter the current at r1,r2,  and r3, (use commas): "))
        v = eval(input("Enter the voltage at the source: "))

        r1,r4,r5,a1,a2,a3,v = 1.0*r1,1.0*r4,1.0*r5,1.0*a1,1.0*a2,1.0*a3,1.0*v
        
        a5 = a1 - a2 + a3

        v1 = r1 * a1
        v2 = v - v1
        r2 = v2/a2

        v5 = a5 * r5
        v3 = v - v5
        r3 = v3/a3
        
        print("The current at R5 is: ",a5,"A")
        print("The resistance at R2 is: ",r2,"Ohms")
        print("The resistance at R3 is: ",r3,"Ohms")
        question = eval(input("enter the question number: "))

    if question == 3 :
        r1 = eval(input("Enter the given resistance value: "))
        r2 = (((r1)*((sqrt(2.0))-1))/(1- ((sqrt(2))/2)))
        print("The resistance value for R' is: " , r2 , "Ohms")
        question = eval(input("enter the question number: "))


    if question == 4 :
        e1 = eval(input("Enter the voltage of E1: "))
        i2 = eval(input("Enter the current given: "))
        r1,r2,r3 = eval(input("Enter the resistance values, (use commas, enter three values): "))

        e1,r1,r2,r3 = 1.0*e1,1.0*r1,1.0*r2,1.0*r3

        i1 = (e1 - (i2*r2))/r1
        i3 = i2 - i1
        v2 = (i2*r2) + (i3*r3)
        
        print("current in I1:",i1,"A")
        print("current in I2:",i3,"A")
        print("voltage in E2:",v2,"V")
        question = eval(input("enter the question number: "))

    if question == 5 :
        r1,r2,r3,r4,r5,r6,r7,r8 = eval(input("Enter the 8 resistances (in Ohms): "))
        e1,e4,e6 = eval(input("Enter the volatges give in order (E1,E4,E6),(use commas and volts): "))
        r1,r2,r3,r4,r5,r6,r7,r8,e1,e4,e6 = 1.0*r1,1.0*r2,1.0*r3,1.0*r4,1.0*r5,1.0*r6,1.0*r7,1.0*r8,1.0*e1,1.0*e4,1.0*e6
        i = (e1 + e6)/(r1+r2+r3+r6+r7)
        vab = abs((-e4 -(i*r7) + e6 -(i*r6)))       
        
        print("\nThe potential difference of Vab is:",vab,"V")
        
        fin = abs((e1*r6+e1*r7+e4*r1+e4*r2+e4*r3+e4*r6+e4*r7-e6*r1-e6*r2-e6*r3)/(r1*r4+r1*r5+r1*r6+r1*r7+r1*r8+r2*r4+r2*r5+r2*r6+r2*r7+r2*r8+r3*r4+r3*r5+r3*r6+r3*r7+r3*r8+r4*r6+r4*r7+r5*r6+r5*r7+r6*r8+r7*r8)) 
        print('\nThe current through r8 is: ', fin)
        question = eval(input("enter the question number: "))

    if question == 6 :
        r1,r2,r3,r4 = eval(input("Enter all the resistance values: "))
        v1 = eval(input("Enter the voltage of the battery: "))

        r1,r2,r3,r4,v1 = 1.0*r1,1.0*r2,1.0*r3,1.0*r4,1.0*v1
        
        rt = ((1.0/((1.0/(r1+r2))+(1.0/r3)))+(r4))

        i3 = v1/rt

        i1 = ((v1 - (r4*i3))/(r1+r2))
        
        p = (i1**2.0)*(r2)
        
        print("The going through R2 is : " , p , "W")
        question = eval(input("enter the question number: "))

    if question == 7 :
        s = eval(input("Enter the total resistancce in series: "))
        p = eval(input("Enter the total resistancce in parallel: "))
        s,p=1.0*s,1.0*p
        r1 = ((-s) + (sqrt((s**2)-(4.0*(-1.0)*((-s)*p)))))/(-2.0)
        r2 = ((-s) - (sqrt((s**2)-(4.0*(-1.0)*((-s)*p)))))/(-2.0)
        print("The resistance values are:",r1,"and",r2,"in Ohms.")            
        question = eval(input("enter the question number: "))

    if question == 8:
        r1,r2,r3 = eval(input("Enter the resistance values (in K Ohms): "))
        e1,e2,e3 = eval(input("Enter the voltage values: "))

        r1,r2,r3,e1,e2,e3 = 1.0*r1,1.0*r2,1.0*r3,1.0*e1,1.0*e2,1.0*e3 

        v = (((e1/r1)+(e2/r2)+(e3/r3))/((1.0/r1)+(1.0/r2)+(1.0/r3)))

        i1 = ((v-e1)/r1)
        i2 = ((v-e2)/r2)
        i3 = ((v-e3)/r3)
                
        print("The current in I1 is:",i1,"mA")
        print("The current in I2 is:",i2,"mA")
        print("The current in I3 is:",i3,"mA")
        print("The voltage between c and f is:",v,"V")
        print("If you get one of the currents wrong, try multiplying the value by (-1), that should make it work properly.")
        question = eval(input("enter the question number: "))

    if question == 9 :
        r = eval(input("Enter the value of resistance: "))
        e = eval(input("Enter the voltage given: "))

        r,e = 1.0*r,1.0*e

        i2 = ((1.71*r*e)-(2.71*r*2*e))/((1.71*r*1.71*r)-(2.71*r*3.71*r))
        i1 = (e - (1.71*r*i2))/(2.71*r)

        v = ((i1+i2)*(1.71*r))

        i4 = (v/(4.0*r))
        
        iae = i4 - i1
        
        print("The current in Iae is :",iae,"A")
        
        question = eval(input("enter the question number: "))

    if question == 10 :
        
        c = eval(input("Enter the capicitance of the capicitor (in nF): "))
        q1 = eval(input("Enter the charge of the capicitor (in uC): "))
        r = eval(input("Enter the resistance value (in K Ohms): "))
        t1 = eval(input("Enter the time passed from part A (in uS): "))
        t2 = eval(input("Enter the time passed from part B (in uS): "))
        
        c,q1,r,t1,t2 = (1.0e-9)*c,(1.0e-6)*q1,(1.0e3)*r,(1.0e-6)*t1,(1.0e-6)*t2
        
        x1 = q1/c
        x2 = x1/r
        x3 = (-1.0*t1)/(r*c)

        i1 = (x2*(math.exp(x3)))

        x4 = (-t2/(r*c))
        
        q2 = (q1*(math.exp(x4)))

        i2 = ((q1/c)/r)
        
        print("The value of current is:",i1,"A")
        print("The charge remaining is:",q2,"C")
        print("The max current is:",i2,"A")
        question = eval(input("enter the question number(0 to quit): "))

    if question == 11 :
        r1,r2 = eval(input("Enter the two values for resistance (Do not enter R3): "))
        v1,v2 = eval(input("Enter the volatges from the circiut diagram (Enter the values from the picture from left to right): "))
        i = v1/float(r1+r2)
        v = float(i*r2)
        v3 = abs(v2-v)
        print("Vab=:",v3,"V")
        question = eval(input("enter the question number: "))

    if question == 12 :

        v = eval(input("Enter the emf voltage for the battery: "))
        r = eval(input("Enter the internal resistance of the battery: "))
        p = eval(input("Enter the power that the battery is absorbing: "))

        v,r,p=1.0*v,1.0*r,1.0*p
        r1 = ((v) + (sqrt( ((-v)**2) -(4.0*(r)*(p)) )))/(2.0*r)
        r2 = ((v) - (sqrt( ((-v)**2) -(4.0*(r)*(p)) )))/(2.0*r)

        r1 = p/(r1**2)
        r2 = p/(r2**2)
        
        print("The resistance values are:",r1,"and",r2,"in Ohms.")        

        question = eval(input("enter the question number: "))

    if question == 13 :
        c = eval(input("Enter the capiticance of the capicitor (in F): "))
        v1 = eval(input("Enter the voltage of the battery: "))
        v2 = eval(input("Enter the voltage of the capacitor after time has passed: "))
        t = eval(input("Enter the time that has passed: "))

        c,v1,v2,t = 1.0*c,1.0*v1,1.0*v2,1.0*t

        valLn1 = math.log(v1)

        valLn2 = math.log(v1-v2) 

        r=t/(c*(valLn1-valLn2))

        print("The resistance value is:",r,"Ohms.")

        question = eval(input("enter the question number: "))

    if question == 14 :

        r1,r2 = eval(input("Enter both values of resistance (in K Ohms): "))
        c1,c2 = eval(input("Enter both values of capicitance (in uF): "))
        e = eval(input("Enter the potential of the battery: "))
        t1,t2 = eval(input("Enter both values for time (in mS): "))
        r1,r2,c1,c2,e,t1,t2 = (1.0e3)*r1,(1.0e3)*r2,(1.0e-6)*c1,(1.0e-6)*c2,1.0*e,(1.0e-3)*t1,(1.0e-3)*t2

        ct = c1+c2
        rt = 1.0/((1.0/r1) + (1.0/r2))

        q1 = (c1*e*(1.0-math.exp((-1.0*t1)/(rt*ct))))
        q2 = (c2*e*(1.0-math.exp((-1.0*t2)/(rt*ct))))
        
        print("The value of the charge q1 on capacitor C1 is:",q1,"C")
        print("The value of the charge q2 on capacitor C2 is:",q2,"C")      
        question = eval(input("enter the question number: "))

    if question == 0 :

        print("You are done!")

        close = input("close window? (y/n): ")

        if (close == ("y" or "Y")):
            exit()

main()
