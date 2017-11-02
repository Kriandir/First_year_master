from scipy.integrate import odeint
import numpy as np
#odeint?    # Uncomment to view the help file for this function

# Define a function which calculates the derivative
def dy_dx(y, x):
    return x - y

xs = np.linspace(0,5,100)
y0 = 1.0
ys = odeint(dy_dx, y0, xs)
print ys
