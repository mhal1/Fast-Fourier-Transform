# convolution using fourier transforms

# h convoluted with g = inverseFT[F(w)G(w)]

# use numpy.fft.fft(a,n,axis,norm)

import numpy as np

import matplotlib.pyplot as plt

import math

# define function h(t)

def h(t):
    
    if t < 3 or t > 5 or t<0:

        return 0

    if t >= 3 and t <= 5:

        return 4

# define function g(t)

def g(t):

    #modify to start half way through it and end half way (0->T)

    #due to periodicity use two gaussians, one centred at 0 and one at T

    return (1/(math.sqrt(2*math.pi)))*(math.exp(-0.5*(t)**2) + math.exp(-0.5*(t-T)**2))

def greal(t):

    #used only for final plot to show shape of gaussian

    return (1/(math.sqrt(2*math.pi)))*(math.exp(-0.5*(t)**2))

# set time period, T, for sampling

# padding is controlled by this T too, as it determines the number of zeros
# between the two gaussians

T = 20

# min freq

wmin = 2*math.pi/T

# number of points

N = 128  

# sampling rate

dt = T/N

#max freq

nyquistfreq = math.pi/dt

gvalues = []

# to show the actual shape of guassian in final plot

grealshape = []

hvalues = []

hextended = []

for i in np.arange(-5,6,dt):

    grealshape.append(greal(i))

for i in np.arange(-5,T,dt):

    hextended.append(h(i))

for i in np.arange(0,T,dt):

    gvalues.append(g(i))

    hvalues.append(h(i))

#fourier transforms

gft = np.fft.fft(gvalues)

hft = np.fft.fft(hvalues)

#inverse fourier transforms

gift = np.fft.ifft(gft)

hift = np.fft.ifft(hft)

# convolve

c = np.real(np.fft.ifft(gft*hft))*(T/len(gft))

# plot

f, axarr = plt.subplots(2, sharex=False, sharey=False)

# any frequencies above nyquistfreq are not needed (only for plot, include them in ifft for power)

#:N//2 gives positive values of ft

axarr[0].scatter(np.arange(0,nyquistfreq, wmin), np.abs(hft)[:N//2], s = 2, label='FT of h(t)')

axarr[0].scatter(np.arange(0,nyquistfreq,wmin), np.abs(gft)[:N//2], s = 2, label='FT of g(t)')

axarr[0].set_title('Fourier transforms')

axarr[0].set(xlabel = 'w (s^-1)', ylabel = '|FT|')

legend = axarr[0].legend()

axarr[1].plot(np.arange(0,T,dt), c , label = 'Convolution')

axarr[1].plot(np.arange(-5,6,dt), grealshape, label = 'g(t)')

axarr[1].plot(np.arange(-5,T,dt), hextended, label ='h(t)')

axarr[1].set_title('Convolution')

axarr[1].set(xlabel = 't (s)', ylabel = 'f(t)')

legend = axarr[1].legend()

plt.show()
