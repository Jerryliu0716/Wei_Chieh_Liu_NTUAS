#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:42:26 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

P_01 , T_01 , Td_01 , RH_01 , es_01 , e_01 = np.genfromtxt('20181001.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_02 , T_02 , Td_02 , RH_02 , es_02 , e_02 = np.genfromtxt('20181002.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_03 , T_03 , Td_03 , RH_03 , es_03 , e_03 = np.genfromtxt('20181003.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_04 , T_04 , Td_04 , RH_04 , es_04 , e_04 = np.genfromtxt('20181004.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_05 , T_05 , Td_05 , RH_05 , es_05 , e_05 = np.genfromtxt('20181005.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_06 , T_06 , Td_06 , RH_06 , es_06 , e_06 = np.genfromtxt('20181006.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )
P_07 , T_07 , Td_07 , RH_07 , es_07 , e_07 = np.genfromtxt('20181007.csv', usecols = (3,5,6,7,8,9), unpack=True ,delimiter=(',') )

P =[]
P.extend(P_01) ; P.extend(P_02) ; P.extend(P_03) ; P.extend(P_04) ; P.extend(P_05) ; P.extend(P_06) ; P.extend(P_07)
Td =[]
Td.extend(Td_01) ; Td.extend(Td_02) ; Td.extend(Td_03) ; Td.extend(Td_04) ; Td.extend(Td_05) ; Td.extend(Td_06) ; Td.extend(Td_07)
RH =[]
RH.extend(RH_01) ; RH.extend(RH_02) ; RH.extend(RH_03) ; RH.extend(RH_04) ; RH.extend(RH_05) ; RH.extend(RH_06) ; RH.extend(RH_07)
es =[]
es.extend(es_01) ; es.extend(es_02) ; es.extend(es_03) ; es.extend(es_04) ; es.extend(es_05) ; es.extend(es_06) ; es.extend(es_07)
e =[]
e.extend(e_01) ; e.extend(e_02) ; e.extend(e_03) ; e.extend(e_04) ; e.extend(e_05) ; e.extend(e_06) ; e.extend(e_07)
T =[]
T.extend(T_01) ; T.extend(T_02) ; T.extend(T_03) ; T.extend(T_04) ; T.extend(T_05) ; T.extend(T_06) ; T.extend(T_07)

T = np.asarray(T)
Td = np.asarray(Td)
e = np.asarray(e)
P = np.asarray(P)
qv = 0.622*e/P


plt.figure(figsize=(10,6))
plt.grid()
plt.plot(e)
plt.plot(es)
plt.legend(['e','es'],fontsize=18)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Pressure [hPa]',fontsize=18)
plt.xlim(0,len(e))
plt.ylim(10,45)
plt.xticks(np.linspace(0,len(e),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.tick_params(labelsize=15)
plt.title('e and es with daily evolution in Oct 2018',fontsize=20)
plt.savefig('HW3_e&es.png',dpi=300)
plt.show()
plt.close()

plt.figure(figsize=(10,6))
plt.grid()
plt.plot(T)
plt.plot(Td)
plt.plot(T-Td)
plt.legend(['T','Td','T-Td'],fontsize=16,loc='best')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Temperature [T]',fontsize=18)
plt.xlim(0,len(e))
plt.ylim(0,35)
plt.xticks(np.linspace(0,len(e),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.tick_params(labelsize=15)
plt.title('T and Td and  with daily evolution in Oct 2018',fontsize=20)
plt.savefig('HW3_T&Td.png',dpi=300)
plt.show()
plt.close()

plt.figure(figsize=(10,6))
plt.grid()
plt.plot(qv*1000)
plt.legend(['qv'],fontsize=20,loc='lower right')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Specific humidity [kg/kg]',fontsize=18)
plt.xlim(0,len(e))
plt.ylim(7,16)
plt.xticks(np.linspace(0,len(e),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.tick_params(labelsize=15)
plt.title('qv with daily evolution in Oct 2018',fontsize=20)
plt.savefig('HW3_qv.png',dpi=300)
plt.show()
plt.close()

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)
ax1.plot(RH, 'tab:blue')
ax1.set_ylabel('Relative humidity [%]',fontsize=18,color='tab:blue')
ax1.set_xlabel('Date',fontsize=18)
ax1.tick_params(axis='y',labelsize=15,labelcolor='tab:blue')
ax1.tick_params(axis='x',labelsize=15)
ax2 = ax1.twinx()
ax2.plot(T-Td,'orange')
ax2.set_ylabel('Delta temperature [˚C]',fontsize=18,color='orange')
ax2.tick_params(axis='y',labelsize=15,labelcolor='orange')
plt.xlim(0,len(e))
plt.xticks(np.linspace(0,len(e),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.title('RH with daily evolution in Oct 2018',fontsize=20)
plt.grid()
plt.savefig('HW3_RH.png',dpi=300)
plt.show()
plt.close()








