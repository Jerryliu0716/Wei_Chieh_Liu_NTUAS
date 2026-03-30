#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 02:46:32 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt
from windrose import WindroseAxes as WA
import pandas as pd


wd1,ws1=np.genfromtxt('20181001.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd2,ws2=np.genfromtxt('20181002.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd3,ws3=np.genfromtxt('20181003.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd4,ws4=np.genfromtxt('20181004.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd5,ws5=np.genfromtxt('20181005.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd6,ws6=np.genfromtxt('20181006.csv',usecols=(10,11),unpack=True,delimiter=(','))
wd7,ws7=np.genfromtxt('20181007.csv',usecols=(10,11),unpack=True,delimiter=(','))

ws = np.hstack((ws1,ws2,ws3,ws4,ws5,ws6,ws7))
wd = np.hstack((wd1,wd2,wd3,wd4,wd5,wd6,wd7))

ws = ws*10
wd = wd*10

for i in range(len(wd)):
    if wd[i] >= 990:
        wd[i] = np.nan
        
f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(wd,linewidth=0.5)
ax[0].grid()
ax[0].set_ylabel('direction [˚]',fontsize=16)
ax[0].set_ylim([0,360])
ax[0].set_yticks([0,90,180,270,360])
ax[0].set_title('Wind direction with daily evolution in Oct 2018',fontsize=18)
ax[1].plot(ws/10,linewidth=0.5)
ax[1].grid()
ax[1].set_ylabel('speed [m/s]',fontsize=16)
ax[1].set_title('Wind speed with daily evolution in Oct 2018',fontsize=18)
plt.xticks(np.linspace(0,len(ws),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xlim([0,len(ws)])
plt.xlabel('Date',fontsize=18)
plt.savefig('HW3_7day_av.png',dpi=300)
plt.show()
plt.close()


wd_r=np.deg2rad(wd)  
u = -ws*np.sin(-wd_r) #+E-W
v = -ws*np.cos(-wd_r) #+N-S
u10=np.zeros(1004)
v10=np.zeros(1004)
ws10=np.zeros(1004)
wd10=np.zeros(1004)

for i in range(1004):
    u10[i] = np.average(u[10*i:10*i+10])
    v10[i] = np.average(v[10*i:10*i+10])
    ws10[i] = (u10[i]**2+v10[i]**2)**(1/2)
    rad = np.arcsin(u10[i]/ws10[i])
    if u10[i] <=0:
        wd10[i]=360+np.rad2deg(rad)
    else:
        wd10[i]=np.rad2deg(rad)
        


# 10/01
f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(wd[0:1439],linewidth=0.7)
ax[0].grid()
ax[0].set_ylabel('direction [˚]',fontsize=16)
ax[0].set_ylim([0,360])
ax[0].set_yticks([0,90,180,270,360])
ax[0].set_title('Wind direction and wind speed in Oct $1^{st}$ 2018',fontsize=18)
ax[1].plot(ws1,linewidth=0.7)
ax[1].grid()
ax[1].set_ylabel('speed (m/s)',fontsize=16)
ax[1].set_ylim([0,5])
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xticks(np.linspace(0,len(ws1),5),['00:00','06:00','12:00','18:00','24:00'])
plt.xlim([0,len(ws1)])
plt.savefig('HW3_wd&ws_D1.png',dpi=300)
plt.show()
plt.close()

# 10/02
f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(wd[1440:1439+1438],linewidth=0.7)
ax[0].grid()
ax[0].set_ylabel('direction [˚]',fontsize=16)
ax[0].set_ylim([0,360])
ax[0].set_yticks([0,90,180,270,360])
ax[0].set_title('Wind direction and wind speed in Oct $2^{nd}$ 2018',fontsize=18)
ax[1].plot(ws2,linewidth=0.7)
ax[1].grid()
ax[1].set_ylabel('speed (m/s)',fontsize=16)
ax[1].set_ylim([0,5])
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xticks(np.linspace(0,len(ws2),5),['00:00','06:00','12:00','18:00','24:00'])
plt.xlim([0,len(ws2)])
plt.savefig('HW3_wd&ws_D2.png',dpi=300)
plt.show()
plt.close()

# 10/03
f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(wd[1439+1438:1439+1438+1440],linewidth=0.7)
ax[0].grid()
ax[0].set_ylabel('direction [˚]',fontsize=16)
ax[0].set_ylim([0,360])
ax[0].set_yticks([0,90,180,270,360])
ax[0].set_title('Wind direction and wind speed in Oct $3^{rd}$ 2018',fontsize=18)
ax[1].plot(ws3,linewidth=0.7)
ax[1].grid()
ax[1].set_ylabel('speed (m/s)',fontsize=16)
ax[1].set_ylim([0,5])
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xticks(np.linspace(0,len(ws2),5),['00:00','06:00','12:00','18:00','24:00'])
plt.xlim([0,len(ws3)])
plt.savefig('HW3_wd&ws_D3.png',dpi=300)
plt.show()
plt.close()

# 10/04
f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(wd[1439+1438+1440:1439+1438+1440+1432],linewidth=0.7)
ax[0].grid()
ax[0].set_ylabel('direction [˚]',fontsize=16)
ax[0].set_ylim([0,360])
ax[0].set_yticks([0,90,180,270,360])
ax[0].set_title('Wind direction and wind speed in Oct $4^{th}$ 2018',fontsize=18)
ax[1].plot(ws,linewidth=0.7)
ax[1].grid()
ax[1].set_ylabel('speed (m/s)',fontsize=16)
ax[1].set_ylim([0,5])
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xticks(np.linspace(0,len(ws2),5),['00:00','06:00','12:00','18:00','24:00'])
plt.xlim([0,len(ws4)])
plt.savefig('HW3_wd&ws_D4.png',dpi=300)
plt.show()
plt.close()

f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(u/10,linewidth=0.7)
ax[0].grid()
ax[0].set_ylabel('u speed [m/s]',fontsize=16)
ax[0].set_title('uv windspeed (NS and EW) with daily evolution in 2018',fontsize=18)
ax[0].set_ylim(-2,4)
ax[0].set_yticks(np.arange(-2,4,1))
ax[1].plot(v/10,linewidth=0.7)
ax[1].grid()
ax[1].set_ylabel('v speed [m/s]',fontsize=16)
ax[1].set_ylim(-4,2)
ax[1].set_yticks(np.arange(-4,2,1))
ax[1].tick_params(labelsize=14)
ax[0].tick_params(labelsize=14)
plt.xticks(np.linspace(0,len(ws),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.xlim(0,len(wd))
plt.savefig('HW3_uv.png',dpi=300)
plt.show()
plt.close()

f,ax=plt.subplots(2,1,sharex='all',figsize=(10,6))
ax[0].plot(u10/10,linewidth=1)
ax[0].grid()
ax[0].set_ylabel('u speed (m/s)',fontsize=16)
ax[0].set_title('uv windspeed (NS and EW) 10 min average in Oct 2018',fontsize=18)
ax[0].set_yticks(np.arange(-2,4,1))
ax[1].plot(v10/10,linewidth=1)
ax[1].grid()
ax[1].set_ylabel('v speed (m/s)',fontsize=16)
ax[1].set_yticks(np.arange(-4,2,1))
plt.xticks(np.linspace(0,len(u10),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.xlim(0,len(u10))
plt.savefig('HW3_uv10.png',dpi=300)
plt.show()
plt.close()


ax=WA.from_ax()
ax.bar(wd,ws,normed=True,opening=0.8,edgecolor='white')
ax.set_theta_zero_location('E')
ax.set_legend(fontsize=15)
plt.title('Wind speed and wind direction in windrose',fontsize=18)
plt.savefig('HW3_windrose.png',dpi=300)
plt.show()
plt.close()

ws10 = ws10.tolist()
wd10 = wd10.tolist()
Data = pd.DataFrame()
Data['ws'] = ws10
Data['wd'] = wd10

ax=WA.from_ax()
ax.bar(Data['wd'],Data['ws'],normed=True,opening=0.8,edgecolor='white')
ax.set_theta_zero_location('E')
ax.set_legend(fontsize=15)
plt.title('Wind speed and wind direction 10 min average in windrose',fontsize=18)
plt.savefig('HW3_windrose10.png',dpi=300)
plt.show()
plt.close()


