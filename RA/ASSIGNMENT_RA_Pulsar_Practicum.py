# In this "Radio Astronomy Pulsar Practicum" you will determine the
# spin period and pulse profile shape of the very first pulsar ever
# discovered by Jocelyn Bell: PSR B1919+21.

# Please fill in this .py file with the necessary code to produce the
# plots and answer the imbedded questions in the comments.  The total
# assignment is worth 10 points + 1 bonus point question.

# Note that some of the necessary code has been left in in order to
# help you along.

# The goal is to produce a plot like the one provided.  You can make a
# single plot with subplots or you can make 4 individual plots.  It
# doesn't matter.  Please label the axes and titles of the plots
# properly.

# 1) Import the necessary python modules

import numpy as np
import scipy as ss
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

# Determine number of bins in the time series (simply the number of
# floats in the binary file

nbins = len(timeseries)

# Set the time per sample (this can be found in the ".inf" file)

time_samp = 0.00262143998406827

# 3) Plot the timeseries.  This plot is worth 1 point.


# QUESTION: Why are there apparently data missing and why does the
# level of the baseline change?  (1 point)

# ANSWER: ionospheric scintillation could cut out the signal, and the second partial
# because more light can get through the atmosphere if the ionospheric scintillation is low.

# Note that I divide by the minimum value to reduce the size of the
# numbers on the y-axis

ax = plt.subplot(4,1,1)
plt.plot(np.arange(0,(len(timeseries)*binwidth),binwidth),timeseries/min(timeseries))
plt.xlabel("Observation Time (s)")
plt.ylabel("Amplitude (arbitrary)")
plt.title("Timeseries")


# 4) Calculate and plot the power spectrum.  This plot is worth 1 point.

# QUESTION: Why are there multiple peaks visible in the power
# spectrum?  What is their relationship, and which one corresponds to
# the pulsar's spin frequency?  (1 point)

# ANSWER: the multiple peaks are the armonics of the pulsar spin frequency. Which is the first peak in the spectrum.
# it is the result of the fouriertransform with output f,2f,3f.... etc

power_spectrum = np.abs(np.fft.fft(timeseries))**2


# Note: you'll want to cut off 10 bins at the beginning and end of the
# power spectrum.  These have very large values and will suppress the
# visibility of the pulsar signal.

# Note: you'll want to plot just the spectrum from ~0.1 - 5 Hz, but
# you can also investigate a broader spectral range if you like.

# Note: to get the x-axis in the right units you need to calculate the
# frequency width of each bin in the power spectrum.  This is given by
# delta_f = 1./(nbins*time_samp) , where nbins is the total number of
# bins in the timeseries and time_samp is the sampling time of the
# data.

ax = plt.subplot(4,1,2)
delta_f = 1./(nbins*time_samp)
lo_f_bin = 18 + 10
hi_f_bin = 898 - 10
maxs = hi_f_bin - nbins
plt.plot(np.arange(lo_f_bin*delta_f,hi_f_bin*delta_f,delta_f),power_spectrum[lo_f_bin:maxs])
plt.xlim(0.1,5)
plt.xlabel("Spin Frequency (Hz)")
plt.ylabel("Fourier Power (arbitrary)")
plt.title("Power Spectrum")

#
# 5) Using the power spectrum peaks, determine the pulse period
# (inverse of the spin frequency).  You can use the higher harmonics
# and divide by the harmonic number to get higher precision on the
# fundamental spin frequency.  Note that in the matplotlib window you
# can zoom in on one of the peaks and then use the cursor so that the
# x,y coordinates are displayed in the bottom left of the plot window.
# That's the easiest way to measure the frequencies of the peaks.

# QUESTION: what are the pulse period and spin frequency (these are
# the inverse of each other)?  (1 point)

# ANSWER: spin frequency: 0.747767 Hz and the spin period : 1.337314 s

# Here's the value that I determined from the data and then tweaked by
# hand.

spin_period = 1./0.747767
print spin_period
#
# 6) Make a plot of the signal strength versus pulse number (time) and
# rotational phase.

# This plot is worth 3 points.  It will be judged on how well the
# pulses line-up in times (i.e. form a vertical line).

# BONUS QUESTION (1 point extra): is it surprising that the pulses
# aren't all of the same intensity?  Pulsars have stable pulse
# profiles, which are the basis for doing precision pulsar timing,
# right?  So how can that work if each pulse is different?  Discuss...

# ANSWER: It is not surprising that the pulses vary cause the intensity may differ due to enviroment effects (increased noise, clouds, changes in orbit, solar wind).
#  However,making use of pulsar timing we just need to know that the pulse exists, it doesnt matter how high in intensity the peak is.

# Note: this requires chopping the timeseries into chunks equal to the
# pulsar period, which you determined in the previous step.

# Note: a tricky thing is that the pulse period will not be an integer
# number of time samples.  You need to drop non-integer number of bins
# for each pulse period (see example code).

# Note: the timeseries also ends on a non-integer pulse phase.  So
# drop the last partial pulse in the data set as a whole.

# Note: if your pulsar period is incorrect then the pulses won't stack
# on top of each other nicely.  You can tweak the period by hand until
# they do.

# Note: I divide the profile in each pulse period by the median in
# that pulse period in order to take out jumps in the baseline
# (cf. first plot of the raw timeseries).

# Number of bins (time samples) across the pulse period
spin_period_bins = spin_period/time_samp
print spin_period_bins
# Create an empty list to store the individual pulse profiles
stacked_profiles = []

# Calculate the bin number that each new pulse starts at
lo_phase_bin = np.round(np.arange(0,len(timeseries),spin_period_bins))

# Chop the data into chunks of the pulse period
for phase in lo_phase_bin:
   profile = timeseries[np.int(phase):np.int(phase)+np.int(spin_period_bins)]
   profile = profile/np.median(profile)
   stacked_profiles.append(profile)

# Convert this to a 2-D numpy array (note that we're chopping off the
# last incomplete pulse).
stacked_profiles = np.asarray(stacked_profiles[:-1])

ax = plt.subplot(4,1,3)
plt.imshow(stacked_profiles,origin='lower',aspect=0.3)
plt.xlabel("Rotational Phase Bin")
plt.ylabel("Pulse Number")
plt.title("Pulse Strength vs Time")

#
# 7) Plot the cumulative pulse profile.  This just requires squashing
# the 2-D array of pulse profiles to a single dimension.

# This plot is worth 1 point.

# QUESTION: what is the approximate pulse width in seconds and how
# does this compare to the duration of the pulse period?  (1 point)

# ANSWER: binsinpulse = 20
# peakwidth = 0.039321599761
#  it compares using pulse_width/spin_period
# = 0.0294042429212 which  means that of the spin_period only 0.029 (3%) part is a pulse.

# add everything to a single dimension using the stack method
combinedphases = np.zeros(510)
i = 0
def squashPhase(i,stacked,combinedphases):
    # check if end has reached
    if i == 133:
        return combinedphases
    i+=1
    combinedphases = np.add(combinedphases,stacked)
    return squashPhase(i,stacked_profiles[i],combinedphases)

y = squashPhase(i,stacked_profiles[i],combinedphases)

ax = plt.subplot(4,1,4)
plt.plot(np.arange(0,len(y)),y)
plt.xlim(0,510)
plt.xlabel("Rotational Phase Bin")
plt.ylabel("Pulse Strength (arbitrary)")
plt.title("Cumulative Pulse Profile")

# This just helps ensure that the plots aren't on top of each other.
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.75)

plt.show()
