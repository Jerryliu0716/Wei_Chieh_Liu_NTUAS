# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:01:50 2022

@author: Jerry Liou
"""

import numpy as np
from scipy.optimize import fsolve

# set up parameters

Rd = 287
Cp = 1004
Lv = 2.5e6
Rv = 461
cw = 4187
epsilon = 0.622
e0 = 6.11

#%%

# Clausius-Clapeeyron equation
e_1015 =  e0 * np.exp( (Lv/Rv) * ( 1/273.15 - 1/(22+273.15) ) ) 

# w = mv/md = (epsilon * e) / (P - e)
w_1015 = (epsilon*e_1015) / (1015-e_1015)

# Before parcel saturated, X = 0, Q = ws = w (Actual vapor)
# calculate the constant of reversible saturated adiabatic process equation 

Q = w_1015
ws = Q
constant = ((31+273.15)/1015**(Rd/(Cp+Q*cw)))*np.exp((ws*Lv)/((31+273.15)*(Cp+Q*cw)))
print('Constant = ',constant)

#%% potential temperature

P0 = 1000
theta = (31+273.15)*(P0/1015)**(Rd/Cp)
T_950 = theta / ((P0/950)**(Rd/Cp)) - 273.15
print('T_parcel at 950 hPa by potential temperature = ',T_950)

#%% use 可逆飽和絶熱公式 to solve out Tc at 800 hPa

T = 273.15
def func2(T):
    P = 800
    return ((T/P**(Rd/(Cp+Q*cw))*np.exp((((epsilon*(e0*np.exp((Lv/Rv)*((1/273.15)-(1/T)))))/(P-e0*np.exp(Lv/Rv*(1/273.15-1/T))))*Lv)/(T*(Cp+Q*cw)))) - constant)

T_800 = fsolve(func2,T)
print('T_parcel at 800 hPa = ',T_800-273.15 , '˚c')

es_800 = e0*np.exp(Lv/Rv*(1/273.15-1/T_800))
ws_800 = epsilon*es_800/(800-es_800)
X_800 = Q-ws_800

print('Total water mixing ratio at 800 hPa = ',Q,'kg/kg')
print('Vapor mixing ratio at 800 hPa = ',ws_800,'kg/kg')
print('Condensed water mixing ratio at 800 hPa = ',X_800,'kg/kg')

#%% use 可逆飽和絶熱公式 to solve out Tc at 950 hPa

T = 300
def func1(T):
    P = 950
    return (T/P**(Rd/(Cp+Q*cw)))*np.exp((w_1015*Lv)/(T*(Cp+Q*cw))) - constant

T_950 = fsolve(func1,T)
print('T_parcel = ',T_950-273.15 , '˚c')

es_950 = e0*np.exp(Lv/Rv*(1/273.15-1/T_950))
ws_950 = epsilon*es_950/(950-es_950)
X_950 = Q-ws_950

print('Total water mixing ratio at 950 hPa = ',Q,'kg/kg')
print('Saturated vapor mixing ratio at 950 hPa = ',ws_950,'kg/kg')
print('Condensed water mixing ratio at 950 hPa =  [0] kg/kg')
