#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:17:42 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

#%% method 1 
# use loop to iterate and use if to break

# set up parameters
E = 1 
L = 2.5
a = 8500
b = 1
rho_w = 1e6
w2 = 2
w45 = 4.5
dt = 0.01

# set up array
t = np.arange(0,1000,0.01)
r15_2 = np.zeros(len(t))
r15_45 = np.zeros(len(t))
z15_2 = np.zeros(len(t))
z15_45 = np.zeros(len(t))
z15_2[0] = 300
z15_45[0] = 300
r15_2[0] = 15e-6
r15_45[0] = 15e-6

# calculate r, z, t
# for r0=15, w = 2
for i in range(len(z15_2)-1):
    dr_dt = E*L/(4*rho_w)*a*r15_2[i]**b
    r15_2[i+1] = r15_2[i] + dt*dr_dt
    t[i] += 0.01
    dz_dt = w2 - a*r15_2[i]**b
    z15_2[i+1] = z15_2[i] + dt*dz_dt
    if z15_2[i] < 200:
        t_15_2 = i
        z15_2[i:-1] = np.nan
        break

# for r0=15, w = 45
for i in range(len(z15_45)-1):
    dr_dt = E*L/(4*rho_w)*a*r15_45[i]**b
    r15_45[i+1] = r15_45[i] + dt*dr_dt
    t[i] += 0.01
    dz_dt = w45 - a*r15_45[i]**b
    z15_45[i+1] = z15_45[i] + dt*dz_dt
    if z15_45[i] < 200:
        t_15_45 = i
        z15_45[i:-1] = np.nan
        break

#%% method 2
#use list to append and use while to stop

#set up list
z40_2 = [300]
z40_45 = [300]
r40_2 = [40e-6]
r40_45 = [40e-6]
t2 = [0]
t4 = [0]
time2 = t2[0]
time4 = t4[0]

# calculate r, z, t
# for r0=40, w = 2
while z40_2[-1] > 200 :
    dt = 0.01
    dr_dt = ((E * L)/(4 * rho_w)) * (a*(r40_2[-1]**b))
    r_40_2 = r40_2[-1] + dt * (dr_dt)
    r40_2.append(r_40_2)
    time2 = time2 + dt
    t2.append(time2)
    dz_dt = w2 - a*(r_40_2**b)
    H = z40_2[-1] + dt * dz_dt
    z40_2.append(H)

# for r0=40, w = 4.5
while z40_45[-1] > 200 :
    dt = 0.01
    dr_dt = ((E * L)/(4 * rho_w)) * (a*(r40_45[-1]**b))
    r_40_45 = r40_45[-1] + dt * (dr_dt)
    r40_45.append(r_40_45)
    time4 = time4 + dt
    t4.append(time4)
    dz_dt = w45 - a*(r_40_45**b)
    H4 = z40_45[-1] + dt * dz_dt
    z40_45.append(H4)

r40_2 = np.array(r40_2)
r40_45 = np.array(r40_45)

#%% plot Z-R

# same radius(15), different speed (2&4.5)
plt.grid()
plt.plot(r15_2*1e6,z15_2)
plt.plot(r15_45*1e6,z15_45)
plt.plot(r15_45*1e6,[200]*len(r15_45),':')
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s'])
plt.xlabel('Radius [$\mu$m]')
plt.ylabel('Height [m]')
plt.title('Z-R Relation, $R_{0}$=15$\mu$m')
plt.savefig('Z-R r_15 w_2&4.5 .png',dpi=300)
plt.show()
plt.close()

# same radius (40), different speed (2&4.5)
plt.grid()
plt.plot(r40_2*1e6,z40_2)
plt.plot(r40_45*1e6,z40_45)
plt.plot(r40_45*1e6,[200]*len(r40_45),':')
plt.ylim(100,1800)
plt.yticks(np.arange(200,1900,400),['200','600','1000','1400','1800'])
plt.legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'])
plt.xlabel('Radius [$\mu$m]')
plt.ylabel('Height [m]')
plt.title('Z-R Relation, $R_{0}$=40$\mu$m')
plt.savefig('Z-R r_40 w_2&4.5 .png',dpi=300)
plt.show()
plt.close()

# same speed (2), different radius (15&40)
plt.grid()
plt.plot(r40_2*1e6,z40_2)
plt.plot(r15_2*1e6,z15_2)
plt.plot(r15_2*1e6,[200]*len(r15_2),':')
plt.ylim(100,1000)
plt.yticks(np.arange(200,1100,200),['200','400','600','800','1000'])
plt.legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=2m/s'])
plt.xlabel('Radius [$\mu$m]')
plt.ylabel('Height [m]')
plt.title('Z-R Relation, w=2m/s')
plt.savefig('Z-R r_15&40 w_2 .png',dpi=300)
plt.show()
plt.close()

# same speed (4.5), different radius (15&40)
plt.grid()
plt.plot(r40_45*1e6,z40_45)
plt.plot(r15_45*1e6,z15_45)
plt.plot(r15_45*1e6,[200]*len(r15_45),':')
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.legend(['$r_{0}$=40$\mu$m, w=4.5m/s','$r_{0}$=15$\mu$m, w=4.5m/s'])
plt.xlabel('Radius [$\mu$m]')
plt.ylabel('Height [m]')
plt.title('Z-R Relation, w=4.5m/s')
plt.savefig('Z-R r_15&40 w_4.5 .png',dpi=300)
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
plt.savefig('Z-R r_15 vs r_40 mix.png',dpi=300)
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
ax[1].legend(['$r_{0}$=`15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper right')
ax[1].grid()
ax[1].set_title('w=4.5m/s',fontsize=15)
ax[1].set_xlabel('Radius [$\mu$m]',fontsize=13)
f.suptitle('Z-R Relation',fontsize=20)
plt.savefig('Z-R w_2 vs w_4.5 mix.png',dpi=300)
plt.show()
plt.close()

# mix
plt.figure(figsize=(6,4))
plt.grid()
plt.plot(r15_2*1e6,z15_2)
plt.plot(r15_45*1e6,z15_45)
plt.plot(r40_2*1e6,z40_2)
plt.plot(r40_45*1e6,z40_45)
plt.plot(r15_45*1e6,[200]*len(r15_45),':')
plt.legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'])
plt.xlabel('Radius [$\mu$m]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.title('Z-R Relation',fontsize=15)
plt.savefig('Z-R diagram mix.png',dpi=300)
plt.show()
plt.close()

#%% plot Z-t

# same radius(15), different speed (2&4.5)
plt.grid()
plt.plot(t[0:t_15_2],z15_2[0:t_15_2])
plt.plot(t[0:t_15_45],z15_45[0:t_15_45])
plt.plot(t[0:t_15_45],[200]*t_15_45,':')
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s'])
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.title('Z-t Relation, $R_{0}$=15$\mu$m')
plt.savefig('Z-t r_15 w_2&4.5 .png',dpi=300)
plt.show()
plt.close()

# same radius (40), different speed (2&4.5)
plt.grid()
plt.plot(t2,z40_2)
plt.plot(t4,z40_45)
plt.plot(t4,[200]*len(t4),':')
plt.ylim(100,1800)
plt.yticks(np.arange(200,1900,200),['200','400','600','800','1000','1200','1400','1600','1800'])
plt.legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper left')
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.title('Z-t Relation, $R_{0}$=40$\mu$m')
plt.savefig('Z-t r_40 w_2&4.5 .png',dpi=300)
plt.show()
plt.close()

# same speed (2), different radius (15&40)
plt.grid()
plt.plot(t2,z40_2)
plt.plot(t[0:t_15_2],z15_2[0:t_15_2])
plt.plot(t[0:t_15_2],[200]*t_15_2,':')
plt.ylim(100,1000)
plt.yticks(np.arange(200,1100,200),['200','400','600','800','1000'])
plt.legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=2m/s'])
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.title('Z-t Relation, w=2m/s')
plt.savefig('Z-t r_15&40 w_2 .png',dpi=300)
plt.show()
plt.close()

# same speed (4.5), different radius (15&40)
plt.grid()
plt.plot(t4,z40_45)
plt.plot(t[0:t_15_45],z15_45[0:t_15_45])
plt.plot(t[0:t_15_45],[200]*t_15_45,':')
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.legend(['$r_{0}$=40$\mu$m, w=4.5m/s','$r_{0}$=15$\mu$m, w=4.5m/s'])
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.title('Z-t Relation, w=4.5m/s')
plt.savefig('Z-t r_15&40 w_4.5 .png',dpi=300)
plt.show()
plt.close()

# subplot r_15 vs r_40
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(t[0:t_15_2],z15_2[0:t_15_2])
ax[0].plot(t[0:t_15_45],z15_45[0:t_15_45])
ax[0].plot(t[0:t_15_45],[200]*t_15_45,':')
ax[0].set_ylim(100,2600)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s'],loc='upper left')
ax[0].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[0].set_xlabel('Time [s]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('$R_{0}$=15$\mu$m',fontsize=15)
ax[1].plot(t2,z40_2)
ax[1].plot(t4,z40_45)
ax[1].plot(t4,[200]*len(t4),':')
ax[1].set_ylim(100,1800)
ax[1].set_yticks(np.arange(200,1900,400),['200','600','1000','1400','1800'])
ax[1].legend(['$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper left')
ax[1].grid()
ax[1].set_title('$R_{0}$=40$\mu$m',fontsize=15)
ax[1].set_xlabel('Time [s]',fontsize=13)
f.suptitle('Z-t Relation',fontsize=20)
plt.savefig('Z-t r_15 vs r_40 mix.png',dpi=300)
plt.show()
plt.close()

# subplot w_2 vs w_4.5
f,ax=plt.subplots(1,2,figsize=(9,5))
ax[0].plot(t[0:t_15_2],z15_2[0:t_15_2])
ax[0].plot(t2,z40_2)
ax[0].plot(t[0:t_15_2],[200]*t_15_2,':')
ax[0].set_ylim(100,1000)
ax[0].legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=2m/s'],loc='upper left')
ax[0].set_yticks(np.arange(200,1100,200),['200','400','600','800','1000'])
ax[0].set_xlabel('Time [s]',fontsize=13)
ax[0].set_ylabel('Height [m]',fontsize=13)
ax[0].grid()
ax[0].set_title('w=2m/s',fontsize=15)
ax[1].plot(t[0:t_15_45],z15_45[0:t_15_45])
ax[1].plot(t4,z40_45)
ax[1].plot(t[0:t_15_45],[200]*t_15_45,':')
ax[1].set_ylim(100,2600)
ax[1].set_yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
ax[1].legend(['$r_{0}$=`15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=4.5m/s'],loc='upper left')
ax[1].grid()
ax[1].set_title('w=4.5m/s',fontsize=15)
ax[1].set_xlabel('Time [s]',fontsize=13)
f.suptitle('Z-t Relation',fontsize=20)
plt.savefig('Z-t w_2 vs w_4.5 mix.png',dpi=300)
plt.show()
plt.close()

# mix
plt.figure(figsize=(6,4))
plt.grid()
plt.plot(t[0:t_15_2],z15_2[0:t_15_2])
plt.plot(t[0:t_15_45],z15_45[0:t_15_45])
plt.plot(t2,z40_2)
plt.plot(t4,z40_45)
plt.plot(t[0:t_15_45],[200]*t_15_45,':')
plt.legend(['$r_{0}$=15$\mu$m, w=2m/s','$r_{0}$=15$\mu$m, w=4.5m/s','$r_{0}$=40$\mu$m, w=2m/s','$r_{0}$=40$\mu$m, w=4.5m/s'])
plt.xlabel('Time [s]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.ylim(100,2600)
plt.yticks(np.arange(200,2700,400),['200','600','1000','1400','1800','2200','2600'])
plt.title('Z-t Relation',fontsize=15)
plt.savefig('Z-t diagram mix.png',dpi=300)
plt.show()
plt.close()

#%% print outcome

print('R0 = 15 µm , w = 2 m/s, The radius is =',r15_2[t_15_2]*1e6, 'µm')
print('R0 = 15 µm , w = 4.5 m/s, The radius is =',r15_45[t_15_45]*1e6, 'µm')
print('R0 = 40 µm , w = 2 m/s, The radius is =',r40_2[-1]*1e6, 'µm')
print('R0 = 40 µm , w = 4.5 m/s, The radius is =',r40_45[-1]*1e6, 'µm')

