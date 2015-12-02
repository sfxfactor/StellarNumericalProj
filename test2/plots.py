import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

#constants
Msun = 1.989e33 #g
Rsun = 6.9599e10 #cm
G = 6.67259e-8 #cm^3 g^-1 s^-2

M = 100. * Msun
R = 5.51729860191 * Rsun

t0=ascii.read('t0.dat')
tf=ascii.read('tf.dat')

plt.plot(t0['M']/Msun,np.log10(t0['RHO']),label=r"$t_0$")
plt.plot(tf['M']/Msun,np.log10(tf['RHO']),label=r"$t_f$")
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$\log\rho$ [g cm$^{-3}$]")
plt.legend()
plt.savefig('dens.pdf')
plt.clf()

plt.plot(t0['M']/Msun,np.log10(t0['P']),label=r"$t_0$")
plt.plot(tf['M']/Msun,np.log10(tf['P']),label=r"$t_f$")
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$\logP$ [dyne cm$^{-2}$]")
plt.legend()
plt.savefig('pres.pdf')
plt.clf()

plt.plot(t0['M']/Msun,np.log10(t0['T']),label=r"$t_0$")
plt.plot(tf['M']/Msun,np.log10(tf['T']),label=r"$t_f$")
plt.legend()
plt.xlabel(r"$m$ [M$_\odot$]")
plt.ylabel(r"$\logT$ [K]")
plt.savefig('temp.pdf')
plt.clf()
