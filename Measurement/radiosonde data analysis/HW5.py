#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:11:04 2022

@author: liuweijie
"""

import numpy as np
import matplotlib.pyplot as plt

H, P, Temp, RH, Dir, Speed = np.loadtxt('edt2_20201109_0321-1.txt',usecols=(2,3,4,5,7,8),skiprows=6,unpack=True)

Dir = (Dir-180)%360

plt.grid()
plt.plot(P,H)
plt.xlabel('Pressure [hPa]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.title('Pressure of RS41 [2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('P.png', dpi=300)
plt.show()
plt.close()

plt.grid()
plt.plot(Temp,H)
plt.xlabel('Temperature [hPa]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.title('Temperature of RS41 [2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('T.png', dpi=300)
plt.show()
plt.close()

plt.grid()
plt.plot(RH,H)
plt.xlabel('RH [%]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.title('Relative humidty of RS41 [2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('RH.png', dpi=300)
plt.show()
plt.close()

plt.grid()
plt.plot(Dir,H)
plt.xlabel('Dir [deg]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.xticks(np.arange(0,370,45),['180','225','270','315','0','45','90','135','180'])
plt.title('Wind direction of RS41 [2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('Dir.png', dpi=300)
plt.show()
plt.close()

plt.grid()
plt.plot(Speed,H)
plt.xlabel('Speed [deg]',fontsize=12)
plt.ylabel('Height [m]',fontsize=12)
plt.title('Wind speed of RS41 [2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('Speed.png', dpi=300)
plt.show()
plt.close()

Lat, Lon = np.loadtxt('edt2_20201109_0321-1.txt',usecols=(10,11),skiprows=6,unpack=True)
plt.grid()
plt.plot(Lon,Lat)
plt.xlabel('Longitude [deg]',fontsize=12)
plt.ylabel('Lattitude [deg]',fontsize=12)
plt.title('Horizontal trajectory diagram of RS41 \n[2020-11-09T03:21:03 dat]',fontsize=15)
plt.savefig('LonLat.png', dpi=300)
plt.show()
plt.close()



