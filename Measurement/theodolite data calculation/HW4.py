#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:48:21 2022

@author: liuweijie
"""

import math as mh
import numpy as np
import matplotlib.pyplot as plt

T, A, E = np.loadtxt('TAMAYA TD-3.txt',usecols=(1,2,3),unpack=True)

A = np.radians(A)
E = np.radians(E)


w = 150/60 u = np.zeros(len(T)-1)
v = np.zeros(len(T)-1)
z = w*T

for i in range(len(T)-1):
    u[i] = (z[i+1]*(1/mh.tan(E[i+1]))*mh.sin(A[i+1]) - z[i]*(1/mh.tan(E[i]))*mh.sin(A[i]))/(T[i+1]-T[i])
    v[i] = (z[i+1]*(1/mh.tan(E[i+1]))*mh.cos(A[i+1]) - z[i]*(1/mh.tan(E[i]))*mh.cos(A[i]))/(T[i+1]-T[i])

f,ax = plt.subplots(1,3,sharey='row',figsize=(10,6))
ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[0].plot(u,z[:-1],color='coral')
ax[0].plot(v,z[:-1])
ax[0].set_xlim(-8,8)
ax[0].set_xticks(np.arange(-8,9,4),['-8','-4','0','4','8'])
ax[0].set_title('u & v',fontsize=15)
ax[0].set_xlabel('speed [m/s]',fontsize=12)
ax[0].set_ylabel('height [m]',fontsize=12)
ax[1].plot(u,z[:-1],color='coral')
ax[1].set_xticks(np.arange(-8,9,4),['-8','-4','0','4','8'])
ax[1].set_title('u',fontsize=15)
ax[1].set_xlabel('speed [m/s]',fontsize=12)
ax[2].plot(v,z[:-1])
ax[2].set_title('v',fontsize=15)
ax[2].set_xticks(np.arange(-8,9,4),['-8','-4','0','4','8'])
ax[2].set_xlabel('speed [m/s]',fontsize=12)
plt.savefig('uvwind.png',dpi=300)
plt.show()
plt.close()


ws = np.zeros(len(u))
wd = np.zeros(len(u))

for i in range(len(u)):
    ws[i] = (u[i]**2+v[i]**2)**(1/2)
    rad = np.arcsin(u[i]/ws[i])
    if v[i] > 0:
        wd[i] = 180+np.rad2deg(rad)
    elif u[i] > 0 and v[i] < 0:
        wd[i] = 360-np.rad2deg(rad)
    elif u[i] < 0 and v[i] < 0:
        wd[i] = -np.rad2deg(rad)
    else:
        wd[i] = np.rad2deg(rad)

wd = (wd-180)%360


plt.grid()
plt.plot(ws,z[:-1])
plt.title('Height v.s. Wind Speed diagram',fontsize=15)
plt.xlabel('wind speed [m/s]',fontsize=12)
plt.ylabel('height [m]',fontsize=12)
plt.savefig('ws.png',dpi=300)
plt.show()
plt.close()

plt.grid()
plt.plot(wd,z[:-1])
plt.title('Height v.s. Wind Direction diagram',fontsize=15)
plt.xlabel('wind direction [deg]',fontsize=12)
plt.ylabel('height [m]',fontsize=12)
# plt.xlim(-180,180)
plt.xticks(np.arange(0,370,45),['180','225','270','315','0','45','90','135','180'])
plt.savefig('wd.png',dpi=300)
plt.show()
plt.close()


f,ax = plt.subplots(1,3,sharey='row',figsize=(10,6))
ax[0].grid()
ax[1].grid()
ax[2].grid()
ax[0].plot(u,z[:-1])
ax[0].plot(v,z[:-1])
ax[0].set_xlim(-8,8)
ax[0].set_xticks(np.arange(-8,9,4),['-8','-4','0','4','8'])
ax[0].set_title('u & v',fontsize=15)
ax[0].set_xlabel('speed [m/s]',fontsize=12)
ax[0].set_ylabel('height [m]',fontsize=12)
ax[1].plot(ws,z[:-1])
ax[1].set_title('Wind Speed',fontsize=15)
ax[1].set_xlabel('speed [m/s]',fontsize=12)
ax[1].set_xlim(0,8)
ax[2].plot(wd,z[:-1])
ax[2].set_title('Wind Direction',fontsize=15)
ax[2].set_xticks(np.arange(0,370,90),['180','270','0','90','180'])
plt.savefig('uvwswd.png',dpi=300)
plt.show()
plt.close()




    
    