#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 21:00:34 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

#Data
t01 , o01_0 , o01_5 , o01_10 , o01_20 , o01_50 , o01_100 = np.genfromtxt('20181001.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t02 , o02_0 , o02_5 , o02_10 , o02_20 , o02_50 , o02_100 = np.genfromtxt('20181002.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t03 , o03_0 , o03_5 , o03_10 , o03_20 , o03_50 , o03_100 = np.genfromtxt('20181003.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t04 , o04_0 , o04_5 , o04_10 , o04_20 , o04_50 , o04_100 = np.genfromtxt('20181004.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t05 , o05_0 , o05_5 , o05_10 , o05_20 , o05_50 , o05_100 = np.genfromtxt('20181005.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t06 , o06_0 , o06_5 , o06_10 , o06_20 , o06_50 , o06_100 = np.genfromtxt('20181006.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )
t07 , o07_0 , o07_5 , o07_10 , o07_20 , o07_50 , o07_100 = np.genfromtxt('20181007.csv', usecols = (5, 54 ,55 ,56 ,57 ,59 ,60), unpack=True ,delimiter=(',') )

datat =[]
datat.extend(t01) ; datat.extend(t02) ; datat.extend(t03) ; datat.extend(t04) ; datat.extend(t05) ; datat.extend(t06) ; datat.extend(t07)
data0 = []
data0.extend(o01_0) ; data0.extend(o02_0) ; data0.extend(o03_0) ; data0.extend(o04_0) ; data0.extend(o05_0) ; data0.extend(o06_0) ; data0.extend(o07_0)
data5 = []
data5.extend(o01_5) ; data5.extend(o02_5) ; data5.extend(o03_5) ; data5.extend(o04_5) ; data5.extend(o05_5) ; data5.extend(o06_5) ; data5.extend(o07_5)
data10 = []
data10.extend(o01_10) ; data10.extend(o02_10) ; data10.extend(o03_10) ; data10.extend(o04_10) ; data10.extend(o05_10) ; data10.extend(o06_10) ; data10.extend(o07_10)
data20 = []
data20.extend(o01_20) ; data20.extend(o02_20) ; data20.extend(o03_20) ; data20.extend(o04_20) ; data20.extend(o05_20) ; data20.extend(o06_20) ; data20.extend(o07_20)
data50 = []
data50.extend(o01_50) ; data50.extend(o02_50) ; data50.extend(o03_50) ; data50.extend(o04_50) ; data50.extend(o05_50) ; data50.extend(o06_50) ; data50.extend(o07_50)
data100 = []
data100.extend(o01_100) ; data100.extend(o02_100) ; data100.extend(o03_100) ; data100.extend(o04_100) ; data100.extend(o05_100) ; data100.extend(o06_100) ; data100.extend(o07_100)

#Graph

plt.figure(figsize=(10,6))
plt.plot(datat)
plt.plot(data0)
plt.plot(data5)
plt.plot(data10)
plt.plot(data20)
plt.plot(data50)
plt.plot(data100)

plt.title('Air T and Soil T with daily evolution in Oct 2018',fontsize=20)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Temperature (˚C)',fontsize=18)
plt.legend(['T','0cm','-5cm','-10cm','-20cm','-50cm','-100cm'],loc='upper right',prop={'size': 12})
plt.xticks(np.linspace(0,len(data0),8),['10/01','10/02','10/03','10/04','10/05','10/06','10/07','10/08'])
plt.tick_params(labelsize=15)
plt.xlim(0,len(data0))
plt.grid()
plt.savefig('HW3_T&soilT.png',dpi=300)
plt.show()