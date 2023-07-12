# Python Script for CAPA 4 - Physics 1E03

import math, sys

epsil = 8.85E-12
k_e = 8.99E9
pi = math.pi

def choose_next():
    num = eval(input("\nDo another problem? Enter the number (1-9) or 0 to quit: "))
    if num == 0:
        sys.exit()
    else:
        solution(num)

def solution(num):
    if num == 1:
        mean_rad = eval(input("Enter the mean radius of the Earth (without units): "))
        C = 4.0*pi*epsil*mean_rad
        print("\nThe capacitance of the Earth is: ", C, "F.")
        choose_next()
    elif num == 2:
        in_parallel = eval(input("Enter the capacitances in parallel (in pF): "))
        in_series = eval(input("Enter the capacitances in series (in pF): "))
        a = -1 # gg
        b = in_parallel
        c = -(in_series*in_parallel)
        C1 = (-b + math.sqrt((b**2 - (4.0*a*c)))) / (2*a)
        C2 = (-b - math.sqrt((b**2 - (4.0*a*c)))) / (2*a)
        print("\nThe capacitances are:", C1, C2, "pF.")
        choose_next()
    elif num == 3:
        print("IT'S MOTHERFUCKING DECOMPOSITION TIME!")
        C1, C2, C3 = eval(input("Enter the capacitances in the order given (C1, C2, C3): "))
        branch = (C1*C2) / (C1+C2)
        bottom = 2.0*C2
        triple_para = 2.0*branch + C3
        total = (triple_para*bottom) / (triple_para+bottom)   
        print("\nThe equivalent capacitance between points a and b is:", total, "uF.")
        choose_next()
    elif num == 4:
        print("\nlol circuits r ez if ur cheezy\n")
        C1, C2, C3, C4 = eval(input("Enter the capacitances in the order (C1, C2, C3, C4): "))
        mid = (C2*C3) / (C2+C3)
        triple_para_motherfucker = C1 + mid + C4
        print("\nThe equivalent capacitance is:", triple_para_motherfucker, "uF.")
        choose_next()
    elif num == 5:
        C = eval(input("Enter the capacitance given *IN FARADS* (e.g. 2.47E-9, not 2.47): "))
        V = eval(input("Enter the potential difference delta(V): "))
        kappa = eval(input("Enter the kappa value: "))
        C_initial = C / kappa
        Q = C * V
        W_init = (Q**2) / (2.0*C_initial)
        W_without_dielec = (Q**2) / (2.0*C)
        W_req = W_init - W_without_dielec
        V_withdrawn = V * kappa
        print("Work required:", W_req, "J.")
        print("The potential difference once withdrawn is:", V_withdrawn, ".")
        choose_next()
    elif num == 6:
        A = eval(input("Enter the area given (in m^2 - hint: if in cm^2 divide by 100^2): "))
        d = eval(input("Enter the value of 'd' in meters: "))
        K1, K2, K3 = eval(input("Enter the kappa values in order (K1, K2, K3): "))
        C1 = K1*epsil*(A/2.0) / d
        C2 = K2*epsil*(A/2.0) / (d/2.0)
        C3 = K3*epsil*(A/2.0) / (d/2.0)
        C2_C3_series = (C2*C3) / (C2+C3)
        C_total = C2_C3_series + C1
        print("The total capacitance is:", C_total, "F.")
        choose_next()
    elif num == 7:
        C1, C2 = eval(input("Enter C1 and C2 in order (C1, C2) *IN FARADS*: "))
        V = eval(input("Enter the battery's voltage: "))
        Q1 = C1*V
        Q2 = C2*V
        V_new = ((C1-C2)/(C1+C2))*V
        Q1_new = C1 * V_new
        Q2_new = C2 * V_new
        print("The charges are (Q1, Q2):", Q1_new, Q2_new,".")
        choose_next()
    elif num == 8:
        C = eval(input("Enter the capacitor's capacitance *IN FARADS*: "))
        V = eval(input("Enter the battery's voltage: "))
        V_new = eval(input("Enter the new voltage when connected to uncharged capacitor C: "))
        Q_1_i = C*V
        C2 = ((Q_1_i) - V_new*C) / V_new
        print("The capacitance C is: ", C2,".")
    elif num == 9:
        print("\n# PART 1 #\n")
        dia = eval(input("Enter the diameter given in meters: "))
        R = dia/2.0
        D = eval(input("Enter the plate separation in m: "))
        V = eval(input("Enter the battery's voltage in V: "))
        charge_mag = (V * epsil * pi * R**2.0 / D)
        E = (charge_mag / (epsil*pi*R**2.0))
        print("The magnitude of charge is:", charge_mag, "C.")
        print("The field is:", E, "V/m.")
        print("The potential difference is:", V, "V.")
        print("\n# PART 2 #\n")
        D_new = eval(input("Enter the new plate separation in m: "))
        charge_mag = (V * epsil * pi * R**2.0 / D_new)
        E = (charge_mag / (epsil*pi*R**2.0))
        print("The magnitude of charge is:", charge_mag, "C.")
        print("The field is:", E, "V/m.")
        print("The potential difference is:", V, "V.")
        print("\n# PART 3 #\n")
        new_dia = eval(input("Enter the new diameter of the electrodes in m: "))
        R_new = new_dia/2.0
        charge_mag = (V * epsil * pi * R_new**2.0 / D)
        E = (charge_mag / (epsil*pi*R_new**2.0))
        print("The magnitude of charge is:", charge_mag, "C.")
        print("The field is:", E, "V/m.")
        print("The potential difference is:", V, "V.")
        choose_next()   

def main():
    
    print("\t\t*** Welcome to CAPA 4! ***\n")

    print("\t\t*** Do NOT convert units unless specified. ***\n")
    
    choice = eval(input("\nPlease choose a question by box number (e.g. 1-9): "))

    if choice == 0:
        print("\n\t\t *~*~*~**~**~* GoOdByE cHoDe 8=======D~~~~")
        sys.exit()
    elif choice >= 1 or choice <= 9:
        solution(choice)
    else:
        choice = eval(input("\nPlease enter a valid choice or enter 0 to quit: "))
        solution(choice)

main()

