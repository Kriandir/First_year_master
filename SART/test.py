import numpy as np

def ULXe(parm,E): # Calculates the ULX model with exp
    N = parm[0]
    t = parm[1]
    Ecut = parm[2]
    return N*((E**(-1*t)) * np.exp(((-1*E)/Ecut)))

parm = [1,3,4]
x = ULXe(parm,2)
print x
