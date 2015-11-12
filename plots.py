import numpy as np
import matplotlib.pyplot as plt
import polytrope as poly
import scipy.interpolate as intp
from astropy.io import fits
import sys

#argument to plots.py is the index of the polytrope
n = float(sys.argv[1])
filename='poly'+str(n)
#if the fits file exists, use it. If not, integrate to get the data
try:
    data = fits.getdata(filename+'.fits')
except IOError:
    data = poly.poly(n,0.0001,0.000001,filename)

#split out important colums of data
z=data[0]
th=data[1]
mz2dthdz=data[2]
m3ozdthdz=data[3]

#extrapolate using linear interpolation to 0
zn = intp.UnivariateSpline(th[-2:][::-1],z[-2:][::-1],k=1)(0.)
mz2dthdzn = intp.UnivariateSpline(z[-2:],mz2dthdz[-2:],k=1)(zn)
print "zn = ", zn
print "(-z^2 dth/dz)zn = ",mz2dthdzn

#constants
Msun = 1.989e33 #g
Rsun = 6.9599e10 #cm
G = 6.67259e-8 #cm^3 g^-1 s^-2

M = 100. * Msun
R = 5.51729860191 * Rsun

#print important values
pc = (M/(4.*np.pi*mz2dthdzn))*(zn/R)**3.
print "pc = ",pc
A = zn/R
print "A = ",A
K=((4.*np.pi*G)/(n*A**2.))*pc**(1.-1./n)
print "K = ",K
Pc=K*pc**(1.+1./n)
print "Pc = ",Pc

#replace . with p in plot filenames so LaTeX doesn't complain
sn = list(str(n))
sn[1]='p'
sn="".join(sn)

#set up dimentional variables and plot

r = z/A
p = pc*th**n
P = K*p**(1.+1./n)
m = 4.*np.pi*p*r**2.
dr = r[1000]-r[999]
menc = np.cumsum(m*dr)

plt.plot(r/R,menc/Msun)
plt.xlabel(r"r/R")
plt.ylabel(r"$m$ [M$_\odot$]")
plt.savefig('mass'+sn+'.pdf')
plt.clf()

plt.plot(menc/Msun,p)
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$\rho$ [g cm$^{-3}$]")
#plt.hlines(pc*m3ozdthdz[-1],0,M)
plt.savefig('density'+sn+'.pdf')
plt.clf()
plt.plot(menc/Msun,P)
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$P$ [dyne cm$^{-2}$]")
plt.savefig('pressure'+sn+'.pdf')
plt.clf()


#constants
a = 7.56591e-15
B=0.5

#temperature from eq 19.22
T=(((1.-B)*3.*P)/a)**0.25
plt.plot(menc/Msun,np.log10(T))
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$T$ [K]")
plt.savefig('temp'+sn+'.pdf')
plt.clf()

U = -G*4.*np.pi* np.trapz((menc*p*r),r)
print "integrated Ugrav = ", U
print "Eg (19.44) = ",(-3./(5.-n))*(G*M*M)/R
print "Eg ave density = ",-G*(16./15.)*np.pi**2*(pc*m3ozdthdz[-1])**2*R**5
