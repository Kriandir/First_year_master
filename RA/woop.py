
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# 2) Load the data into a numpy array

# Note: the data is:

# a) L197621_SAP0_BEAM1_DM12.437.dat : a simple binary file of 32-bit
# floats.  This file is a timeseries of the data.  The raw data were
# already dedispersed and the bandwidth summed together.  As such,
# this just represents the total signal strength over the whole band
# at a dispersion measure of 12.437pc/cc.  This is the data you need
# to read-in to a numpy array.

# b) L197621_SAP0_BEAM1_DM12.437.inf : a simple text file that lists
# the metadata associated with the .dat file (you can open this with
# any text editor).  For this exercise, you just need the "Width of
# each time series bin (sec)".  That's all you need from this file,
# and you can just copy-paste that value into your code.

data_file = open('L197621_SAP0_BEAM1_DM12.437.dat', 'rb')
timeseries = np.fromfile(file=data_file, dtype=np.float32)
binwidth = 0.00262143998406827
x = ss.norm.rvs(scale=100,size=400)
plt.hist(x,normed=True)
plt.show()
print x
