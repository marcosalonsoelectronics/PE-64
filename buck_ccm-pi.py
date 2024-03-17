# -*- coding: utf-8 -*-
"""
Buck converter CCM

@author: Alonso
"""

from math import pi, log10, sqrt
from control import tf, bode_plot, margin
L= 50e-6; C=10e-6; R=1; rl=0.05; rc=0.15
VB= 10; Vpp=10
s = tf('s')
Gt = (1/Vpp)*VB*(1+rc*C*s)/( L*C*(1+rc/R)*s**2 + (L/R+rc*C+rl*C+rl*rc*C/R)*s + 1+rl/R )
# PI compensator
kc=0.1; fz=20e3; 
wz=2*pi*fz
Comp= kc*(1 + s/wz)/(s/wz)
# Sensor
H=1
# Loop gain
T=Comp*Gt*H
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Gt, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="red" )
mag, phase, omega = bode_plot(Comp, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="blue" )
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100, color="green" )
      
gm, pm, wcg, wcp = margin(T)
print("Bandwidth frequency= ", wcp/(2*pi))
print("Phase margin= ", pm)




'''
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=56
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
'''



