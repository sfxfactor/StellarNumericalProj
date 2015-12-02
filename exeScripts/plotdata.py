import matplotlib.pyplot as plt
import numpy as np
from astropy.io import ascii

lsun = 3.826e33

dat1 = ascii.read('LTeff1.dat')
plt.plot(np.log10(dat1['Teff']),np.log10(dat1['L']/lsun),label = r"1 $M_\odot$")
dat3 = ascii.read('LTeff3.dat')
plt.plot(np.log10(dat3['Teff']),np.log10(dat3['L']/lsun),label = r"3 $M_\odot$")
dat4 = ascii.read('LTeff4.dat')
plt.plot(np.log10(dat4['Teff']),np.log10(dat4['L']/lsun),label = r"4 $M_\odot$")
dat5 = ascii.read('LTeff5.dat')
plt.plot(np.log10(dat5['Teff']),np.log10(dat5['L']/lsun),label = r"5 $M_\odot$")
dat10 = ascii.read('LTeff10.dat')
plt.plot(np.log10(dat10['Teff']),np.log10(dat10['L']/lsun),label = r"10 $M_\odot$")
plt.ylabel(r"$\log L/L_\odot$")
plt.xlabel(r"$\log T_{eff} $[K]")
plt.legend(loc=3)
plt.gca().invert_xaxis()
plt.savefig('HR.pdf')
