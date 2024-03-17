# -*- coding: utf-8 -*-
"""

@author: Alonso
"""

from math import pi, log10, sqrt
from control import tf, bode_plot, margin
L= 50e-6; C=10e-6; R=1; rl=0.05; rc=0.15
VB= 10; Vpp=10
s = tf('s')
Gt = (1/Vpp)*VB*(1+rc*C*s)/( L*C*(1+rc/R)*s**2 + (L/R+rc*C+rl*C+rl*rc*C/R)*s + 1+rl/R )
# PI compensator
kc=1.5e5; wz=1/sqrt(L*C); wp=1/(rc*C)
Comp= kc*(1 + s/wz)**2/(s*(1 + s/wp)**2)
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
C2= 10e-9
R3=1/(2*pi*C2*106e3)
R13= 1/(2*pi*C2*7.1e3)
R1=R13-R3
C1=1/(R1*kc)
R2=(C2/C1)*(R1+R3)
C3=C2*R3/R2
print("R1 (kOhm)= ", R1/1000)
print("R2 (kOhm)= ", R2/1000)
print("R3 (kOhm)= ", R3/1000)
print("C1 (nF)= ", C1/1e-9)
print("C2 (nF)= ", C2/1e-9)
print("C3 (nF)= ", C3/1e-9)










