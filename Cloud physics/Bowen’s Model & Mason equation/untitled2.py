#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 22:25:39 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

# set up parameters
E = 1 
L = 2.5
a = 8500
b = 1
rho_w = 1e6
w2 = 2
w45 = 4.5
dt = 0.01

t = np.arange(0,2000,0.01)
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
        cloudbase_t_15_2 = t[i]     
        break
for i in range(len(z15_2)-1):
    if z15_2[i] < 201 and z15_2[i] > 0:
        dr_dt = (-25/r15_2[i])*1e-12
        r15_2[i+1] = r15_2[i] + dt*dr_dt
        t[i] += 0.01
        dz_dt = a*(r15_2[i]**b)
        z15_2[i+1] = z15_2[i] + dt*dz_dt
    if z15_2[i] < 0:
        ground_t_15_2 = i  
        z15_2[i:-1] = np.nan
        break

# # for r0=15, w = 45
# for i in range(len(z15_45)-1):
#     dr_dt = E*L/(4*rho_w)*a*r15_45[i]**b
#     r15_45[i+1] = r15_45[i] + dt*dr_dt
#     t[i] += 0.01
#     dz_dt = w45 - a*r15_45[i]**b
#     z15_45[i+1] = z15_45[i] + dt*dz_dt
#     if z15_45[i] < 200:
#         t_15_45 = i
#         z15_45[i:-1] = np.nan
#         break

dt_15_2 = ground_t_15_2 - cloudbase_t_15_2
# dt_w4 = groundt4 - cloudbaset4
print('R0 = 15 µm , w = 2, time from cloubase to ground is = ',dt_15_2, ' (s)')
# print('R0 = 30 µm , w = 4, time from cloubase to ground is = ',dt_w4, ' (s)')

