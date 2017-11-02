import numpy as np
import matplotlib.pyplot as plt



# initialize values for a and b
ab = [[1.0,0.0],[0.6,0.4],[0.2,0.8]]

for i in ab:
    # define a list for S and xlist so we can plot later and set j on -4.0
    j = -4.0
    xlist = []
    S = []
    while j < 4.0:

        # calculate phi and taucontinous
        phi = (1/(np.sqrt(np.pi)))*np.exp(-j**2)
        taucont = 1./(1+10*phi)

        # calculate S and in our case I = S since homogeneous
        S.append(i[0] + i[1]*taucont)
        xlist.append(j)

        j+=0.01

    # plot the lines
    legendname = "[a,b] = %s" % str(i)
    plt.plot(xlist,S,label = legendname)

# show the graph
plt.title("Spectral lines with EB approximation")
plt.legend(loc ='lower right')
plt.axis([-4.0,4.0,0,1.1])
plt.xlabel('Frequency (arbitrary units)')
plt.ylabel('Specific Intensity (erg cm^-2 ster^-1 s^-1 Hz^-1)')
plt.savefig('exc10.png')
plt.show()
