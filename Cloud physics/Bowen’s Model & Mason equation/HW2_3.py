#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 02:11:46 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

#set up parameters
E = 1 
L = 2.5
a = 8500
b = 1
rho_w = 1e6
w2 = 2
w45 = 4.5

z15_2 = [300]
z15_45 = [300]
z40_2 = [300]
z40_45 = [300]

r15_2 = [15e-6]
r15_45 = [15e-6]
r40_2 = [40e-6]
r40_45 = [40e-6]

t15_2 = [0]
t15_45 = [0]
t40_2 = [0]
t40_45 = [0]

time15_2 = t15_2[0]
time15_45 = t15_45[0]
time40_2 = t40_2[0]
time40_45 = t40_45[0]

#%%

# calculate r, z, t
# for r0=15, w = 2
while z15_2[-1] > 200 :
    dt = 0.01
    dr_dt = ( E*L/(4*rho_w)) * (a*(r15_2[-1]**b))
    r_15_2 = r15_2[-1] + dt * (dr_dt)
    r15_2.append(r_15_2)
    time15_2 = time15_2 + dt
    t15_2.append(time15_2)
    dz_dt = w2 - a*(r_15_2**b)
    H15_2 = z15_2[-1] + dt * dz_dt
    z15_2.append(H15_2)
cloudbaset15_2 = t15_2[-1]     
  
while z15_2[-1] > 0 :
    dt = 0.01
    dr_dt = (-0.25/r15_2[-1])*1e-14
    r_15_2 = r15_2[-1] + dt * (dr_dt)
    r15_2.append(r_15_2)
    time15_2 = time15_2 + dt
    t15_2.append(time15_2)
    dz_dt = a*(r_15_2**b)
    H15_2 = z15_2[-1] - dt * dz_dt
    z15_2.append(H15_2)
groundt15_2 = t15_2[-1]  

# for r0=15, w = 4.5
while z15_45[-1] > 200 :
    dt = 0.01
    dr_dt = (E*L/(4*rho_w)) * (a*(r15_45[-1]**b))
    r_15_45 = r15_45[-1] + dt * (dr_dt)
    r15_45.append(r_15_45)
    time15_45 = time15_45 + dt
    t15_45.append(time15_45)
    dz_dt = w45 - a*(r_15_45**b)
    H15_45 = z15_45[-1] + dt * dz_dt
    z15_45.append(H15_45)
cloudbaset15_45 = t15_45[-1]

while z15_45[-1] > 0 :  
    dt = 0.01
    dr_dt = (-0.25/r15_45[-1])*1e-14
    r_15_45 = r15_45[-1] + dt * (dr_dt)
    r15_45.append(r_15_45)
    time15_45 = time15_45 + dt
    t15_45.append(time15_45)
    dz_dt = a*(r_15_45**b)
    H15_45 = z15_45[-1] - dt * dz_dt
    z15_45.append(H15_45)
groundt15_45 = t15_45[-1]

# for r0=40, w = 2
while z40_2[-1] > 200 :
    dt = 0.01
    dr_dt = ( E*L/(4*rho_w)) * (a*(r40_2[-1]**b))
    r_40_2 = r40_2[-1] + dt * (dr_dt)
    r40_2.append(r_40_2)
    time40_2 = time40_2 + dt
    t40_2.append(time40_2)
    dz_dt = w2 - a*(r_40_2**b)
    H40_2 = z40_2[-1] + dt * dz_dt
    z40_2.append(H40_2)
cloudbaset40_2 = t40_2[-1]     
  
while z40_2[-1] > 0 :
    dt = 0.01
    dr_dt = (-0.25/r40_2[-1])*1e-14
    r_40_2 = r40_2[-1] + dt * (dr_dt)
    r40_2.append(r_40_2)
    time40_2 = time40_2 + dt
    t40_2.append(time40_2)
    dz_dt = a*(r_40_2**b)
    H40_2 = z40_2[-1] - dt * dz_dt
    z40_2.append(H40_2)
groundt40_2 = t40_2[-1]  

# for r0=40, w = 4.5
while z40_45[-1] > 200 :
    dt = 0.01
    dr_dt = (E*L/(4*rho_w)) * (a*(r40_45[-1]**b))
    r_40_45 = r40_45[-1] + dt * (dr_dt)
    r40_45.append(r_40_45)
    time40_45 = time40_45 + dt
    t40_45.append(time40_45)
    dz_dt = w45 - a*(r_40_45**b)
    H40_45 = z40_45[-1] + dt * dz_dt
    z40_45.append(H40_45)
cloudbaset40_45 = t40_45[-1]

while z40_45[-1] > 0 :  
    dt = 0.01
    dr_dt = (-0.25/r40_45[-1])*1e-14
    r_40_45 = r40_45[-1] + dt * (dr_dt)
    r40_45.append(r_40_45)
    time40_45 = time40_45 + dt
    t40_45.append(time40_45)
    dz_dt = a*(r_40_45**b)
    H40_45 = z40_45[-1] - dt * dz_dt
    z40_45.append(H40_45)
groundt40_45 = t40_45[-1]

#%%

r15_2 = np.array(r15_2)
r15_45 = np.array(r15_45)
r40_2 = np.array(r40_2)
r40_45 = np.array(r40_45)

# subplot r_15 vs r_40
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(t15_2,z15_2)
ax[0].plot(t15_45,z15_45)
ax[0].plot(t15_45,[200]*len(t15_45),':')
ax[0].set_ylim(100,2600)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s'],loc='upper left')
ax[0].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[0].set_xlabel('Time [s]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('$R_{0}$=15$\mu$m',fontsize=15)
ax[1].plot(t40_2,z40_2)
ax[1].plot(t40_45,z40_45)
ax[1].plot(t40_45,[200]*len(t40_45),':')
ax[1].set_ylim(100,1800)
ax[1].set_yticks(np.arange(200,1900,400),['200','600','1000','1400','1800'])
ax[1].legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper left')
ax[1].grid()
ax[1].set_title('$R_{0}$=40$\mu$m',fontsize=15)
ax[1].set_xlabel('Time [s]',fontsize=13)
f.suptitle('Z-t Relation',fontsize=20)
plt.savefig('Z-t to z=0 r_15 vs r_40 mix.png',dpi=300)
plt.show()
plt.close()

# subplot w_2 vs w_4.5
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(t15_2,z15_2)
ax[0].plot(t40_2,z40_2)
ax[0].plot(t15_2,[200]*len(t15_2),':')
ax[0].set_ylim(100,1000)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=2m/s'],loc='upper left')
ax[0].set_yticks(np.arange(200,1100,200),['200','400','600','800','1000'])
ax[0].set_xlabel('Time [s]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('w=2m/s',fontsize=15)
ax[1].plot(t15_45,z15_45)
ax[1].plot(t40_45,z40_45)
ax[1].plot(t15_45,[200]*len(t15_45),':')
ax[1].set_ylim(100,2600)
ax[1].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[1].legend(['$r_{0}$=15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper left')
ax[1].grid()
ax[1].set_title('w=4.5m/s',fontsize=15)
ax[1].set_xlabel('Time [s]',fontsize=13)
f.suptitle('Z-t Relation',fontsize=20)
plt.savefig('Z-t to z=0 w_2 vs w_4.5 mix.png',dpi=300)
plt.show()
plt.close()

# subplot r_15 vs r_40
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(r15_2*1e6,z15_2)
ax[0].plot(r15_45*1e6,z15_45)
ax[0].plot(r15_45*1e6,[200]*len(r15_45),':')
ax[0].set_ylim(100,2600)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s'],loc='upper right')
ax[0].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[0].set_xlabel('Radius [$\mu$m]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('$R_{0}$=15$\mu$m',fontsize=15)
ax[1].plot(r40_2*1e6,z40_2)
ax[1].plot(r40_45*1e6,z40_45)
ax[1].plot(r40_45*1e6,[200]*len(r40_45),':')
ax[1].set_ylim(100,1800)
ax[1].set_yticks(np.arange(200,1900,400),['200','600','1000','1400','1800'])
ax[1].legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper right')
ax[1].grid()
ax[1].set_title('$R_{0}$=40$\mu$m',fontsize=15)
ax[1].set_xlabel('Radius [$\mu$m]',fontsize=13)
f.suptitle('Z-R Relation',fontsize=20)
plt.savefig('Z-R to z=0 r_15 vs r_40 mix.png',dpi=300)
plt.show()
plt.close()

# subplot w_2 vs w_4.5
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(r15_2*1e6,z15_2)
ax[0].plot(r40_2*1e6,z40_2)
ax[0].plot(r15_2*1e6,[200]*len(r15_2),':')
ax[0].set_ylim(100,1100)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=2m/s'],loc='upper right')
ax[0].set_yticks(np.arange(200,1100,200),['200','400','600','800','1000'])
ax[0].set_xlabel('Radius [$\mu$m]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('w=2m/s',fontsize=15)
ax[1].plot(r15_45*1e6,z15_45)
ax[1].plot(r40_45*1e6,z40_45)
ax[1].plot(r15_45*1e6,[200]*len(r15_45),':')
ax[1].set_ylim(100,2600)
ax[1].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[1].legend(['$r_{0}$=15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper right')
ax[1].grid()
ax[1].set_title('w=4.5m/s',fontsize=15)
ax[1].set_xlabel('Radius [$\mu$m]',fontsize=13)
f.suptitle('Z-R Relation',fontsize=20)
plt.savefig('Z-R to z=0 w_2 vs w_4.5 mix.png',dpi=300)
plt.show()
plt.close()

#%%

# calculate cloud base to ground time :
dt_r15_w2 = groundt15_2 - cloudbaset15_2
dt_r15_w45 = groundt15_45 - cloudbaset15_45
dt_r40_w2 = groundt40_2 - cloudbaset40_2
dt_r40_w45 = groundt40_45 - cloudbaset40_45
print('R0 = 15 µm , w = 2 m/s, time from cloubase to ground is = ',dt_r15_w2, 's')
print('R0 = 15 µm , w = 4.5 m/s, time from cloubase to ground is = ',dt_r15_w45, 's')
print('R0 = 40 µm , w = 2 m/s, time from cloubase to ground is = ',dt_r40_w2, 's')
print('R0 = 40 µm , w = 4.5 m/s, time from cloubase to ground is = ',dt_r40_w45, 's')

print('R0 = 15 µm , w = 2 m/s, The radius is =',r15_2[-1]*1e6, 'µm')
print('R0 = 15 µm , w = 4.5 m/s, The radius is =',r15_45[-1]*1e6, 'µm')
print('R0 = 40 µm , w = 2 m/s, The radius is =',r40_2[-1]*1e6, 'µm')
print('R0 = 40 µm , w = 4.5 m/s, The radius is =',r40_45[-1]*1e6, 'µm')





