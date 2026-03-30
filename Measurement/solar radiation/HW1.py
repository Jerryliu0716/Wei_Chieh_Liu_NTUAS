#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 03:10:07 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as m

#讀取excel資料從dataform轉換array
data = pd.read_excel('B10_psp_20081005.xls')
data = data.to_numpy()
A = data[:,1]
B = data[:,2]
C = data[:,3]

#定義太陽常數w/m2
S=1361

#oct是日期（在一年當中為第幾天）
oct=279

#觀測地緯度
obs=m.radians(25)

# time array
time = np.linspace(1,24,1440)
# hour angle array
HA = np.zeros(1440)
Z = np.zeros(1440)
ZA = np.zeros(1440)

# HA
for i in range(1440):
    HA[i]=(time[i]-11.68)*15 
    HA[i]=m.radians(HA[i])
    #sundec是太陽赤緯
    sundecoct = -23.44*np.cos(((2*np.pi/365)*(oct+10)))
    # sundecoct = -4.8511
    sundecoct = m.radians(sundecoct)
    #cos太陽天頂角=sin緯度sin太陽赤緯角+cos緯度cos太陽赤緯角cos太陽時角
    ZA[i] = np.sin(obs)*np.sin(sundecoct)+np.cos(obs)*np.cos(sundecoct)*np.cos(HA[i])
    Z[i] = S*ZA[i]

print(np.amax(Z))
print(np.argmax(Z))

# sheet = pd.read_excel('NOAA_Solar_Calculations_day.xls',usecols='AD')
# ZA = sheet[sheet['Solar Zenith Angle (deg)'] <= 950]
# ZA = ZA.to_numpy()

# Z = np.zeros(240)
# for i in range(240):
#     Z[i] = S*np.cos(ZA[i])

ZA1 = np.zeros(1440)
for i in range(1440):
    ZA1[i] = m.acos(ZA[i]) *180/np.pi

print(np.amin(ZA1))
print(np.argmin(ZA1))

plt.grid()
plt.title('Zenith angle on NTU on 10/5')
plt.plot(time,ZA1,'b-')
plt.xlim([6,18])
plt.ylim(20,90)
plt.xlabel('time [hr]')
plt.ylabel('angle [degree]')
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.savefig('zenith angle.png',dpi = 300)
plt.show()
plt.close()

plt.grid()
plt.title('2008/10/05 extra-terrestrial radiation on NTU ')
plt.plot(time,Z,'b-')
plt.ylim(0,1200)
plt.xlim(0,24)
plt.xlabel('time [hr]')
plt.ylabel('Radiant flux density [W/$m^{2}$]')
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.savefig('Solar on NTU.png',dpi = 300)
plt.show()
plt.close()

# Z1 = Z[0:9]
# Z2 = Z[59:1440]
# Z3 = np.hstack((Z1,Z2))
# time1 = time[0:9]
# time2 = time[59:1440]
# time3 = np.hstack((time1,time2))

plt.figure(figsize=(9,6))
plt.grid()
plt.plot(time,(A-B)/A)
plt.plot(time,(B-C)/A)
plt.plot(time,C/B)
plt.plot(time,A/Z)
plt.legend(['(A-B)/A','(B-C)/A','C/B','A/Z'],fontsize=20)
plt.xlim(0,24)
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.xlabel('time [hr]',fontsize=18)
plt.ylabel('ratio',fontsize=18)
plt.title('The numerical change of the solar radiation in the whole sky',fontsize=20)
plt.savefig('ratio.png',dpi = 300)
plt.show()
plt.close()

plt.figure(figsize=(9,6))
plt.grid()
plt.title('2008/10/05 PSP observation data on NTU',fontsize=22)
plt.plot(time,A)
plt.plot(time,B)
plt.plot(time,C)
plt.legend(['A','B','C'],fontsize=20)
plt.xlim(0,24)
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.xlabel('time [hr]',fontsize=18)
plt.ylabel('Radiant flux density [W/$m^{2}$]',fontsize=18)
plt.savefig('observation on NTU.png',dpi = 300)
plt.show()
plt.close()

plt.figure(figsize=(8,8))
plt.grid()
plt.title('PSP observation vs extra-terrestrial radiation',fontsize=22)
plt.plot(time,A)
plt.plot(time,B)
plt.plot(time,C)
plt.plot(time,Z)
plt.legend(['A','B','C','Z'],fontsize=20)
plt.xlim(6,18)
plt.ylim(0,1200)
plt.xticks([0,3,6,9,12,15,18,21,24])
plt.xlabel('time [hr]',fontsize=18)
plt.ylabel('Radiant flux density [W/$m^{2}$]',fontsize=18)
plt.savefig('observation vs theorem.png',dpi = 300)
plt.show()
plt.close()


