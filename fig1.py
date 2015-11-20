import numpy as np
import matplotlib.pyplot as plt
Lsun = 3.826e33
Rsun = 6.9599e10
sig = 5.67051e-5

M = (np.arange(10)+1.)*100.
Z = np.array([1e-9,0.02])

R1 = 10.*Rsun*((M/370.)*((Z[0]/1e-9)**0.2))**(1./2.2)
print "M [Msun] = ", M[0]
print "R [Rsun] = ", R1[0]/Rsun
R2 = 10.*Rsun*((M/370.)*((Z[1]/1e-9)**0.2))**(1./2.2)
Ledd = 1.25e38*M
print "L [erg s^-1] = ", Ledd[0]
TeffL1 = (Ledd/(4.*np.pi*sig*R1**2))**0.25
print "T [K] (from Ledd)  = ", TeffL1[0]
TeffL2 = (Ledd/(4.*np.pi*sig*R2**2))**0.25

Teff1 = (1.1e5)*((Z[0]/1e-9)**-0.05)*((M/100.)**0.025)
print "T [K] (from M) = ", Teff1[0]
Teff2 = (1.1e5)*((Z[1]/1e-9)**-0.05)*((M/100.)**0.025)

plt.plot(np.log10(TeffL1),np.log10(Ledd/Lsun),"D-")
plt.plot(np.log10(Teff1),np.log10(Ledd/Lsun),"D-")
plt.plot(np.log10(TeffL2),np.log10(Ledd/Lsun),"D-")
plt.plot(np.log10(Teff2),np.log10(Ledd/Lsun),"D-")
plt.gca().invert_xaxis()
plt.savefig('fig1.pdf')
