import numpy as np
import matplotlib.pyplot as plt

# define starting values for I0 and tau0
Io = 1
tauo = [0.1,1.0,10]

# loop through the tau0
for i in tauo:
    # define a list for I and xlist so we can plot later and set j on -4.0
    I = []
    xlist = []
    j= -4.0
    # loop through j
    while j < 4.0:
        # perform calculation we use Sv = 0 since there is no emmission
        # and u = 1 for a normal direction observation
        I.append(Io*np.exp(-(i*((1/(np.sqrt(np.pi)))*np.exp(-j**2)))))
        xlist.append(j)

        j+= 0.01

    # plot the lines
    legendname = "tau0 = %.1f" %i
    plt.plot(xlist,I,label = legendname)

# show the graph
plt.title("Specific intensity of a spectral line")
plt.legend(loc ='lower right')
plt.xlabel('Frequency (arbitrary units)')
plt.ylabel('Specific Intensity (erg cm^-2 ster^-1 s^-1 Hz^-1)')
plt.savefig('exc4.png')
plt.show()

