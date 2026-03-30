#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:05:25 2022

@author: liuweijie
"""
import numpy as np
import math as mh
import matplotlib.pyplot as plt

pi = mh.pi

m_e = 9.1093837e-31 #kg mass of electron
h = 6.62607015e-34 #planck m2kg/s
k = 8.617333262e-5 # bolzmann constant eV/K
eV_to_J = 1.602176634e-19 # eV to J

P_e = 20
T = np.arange(5000,25000,1)
A = np.zeros(len(T))
B = np.zeros(len(T))
C = np.zeros(len(T))

# A = HeII/HeI
# B = HEIII/HeII
# C = HeII/Hetotal
for i in range(len(T)):
    A[i] = (1/P_e)*2*2*(2*pi*m_e)**1.5*(k*T[i]*eV_to_J)**2.5*mh.exp(-24.5/(k*T[i]))/h**3
    B[i] = (1/P_e)*(1/2)*2*(2*pi*m_e)**1.5*(k*T[i]*eV_to_J)**2.5*mh.exp(-54.4/(k*T[i]))/h**3
    C[i] = 1/((1/A[i])+1+B[i])
    if abs(C[i]-0.5) < 1e-4:
        print(T[i])

plt.grid()
plt.plot(T,C)
plt.xlabel('Temperature [K]',fontsize=12)
plt.ylabel('$He_{II}$ / $He_{total}$',fontsize=12)
plt.title('$He_{II}$ / $He_{total}$ for T from 5000 to 25000 K',fontsize=15)
plt.savefig('saha.png',dpi=300)
plt.show()
plt.close()

P_e = 1000
T2 = np.arange(10000,60000,1)
D = np.zeros(len(T2))
E = np.zeros(len(T2))
F = np.zeros(len(T2))

# D = HeII/HeI
# E = HEIII/HeII
# F = HeIII/Hetotal
for i in range(len(T2)):
    D[i] = (1/P_e)*2*2*(2*pi*m_e)**1.5*(k*T2[i]*eV_to_J)**2.5*mh.exp(-24.5/(k*T2[i]))/(h**3)
    E[i] = (1/P_e)*(1/2)*2*(2*pi*m_e)**1.5*(k*T2[i]*eV_to_J)**2.5*mh.exp(-54.4/(k*T2[i]))/(h**3)
    F[i] = E[i]/ ((1/D[i])+1+E[i]) 
    if abs(F[i]-0.5) < 1e-4:
        print(T2[i])
        
plt.grid()
plt.plot(T2,F)
plt.xlabel('Temperature [K]',fontsize=12)
plt.ylabel('$He_{III}$ / $He_{total}$',fontsize=12)
plt.title('$He_{III}$ / $He_{total}$ for T from 10000 to 60000 K',fontsize=15)
plt.savefig('saha_2.png',dpi=300)
plt.show()
plt.close()





