#Inicializaction
import sympy as sp
import scipy as sc
from sympy.solvers import solve
from scipy.optimize import fsolve
from scipy.constants import g,pi,c
from scipy.misc import derivative as drv
from scipy.integrate import quad 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint #ode integrator
import pint

#Tank, no spillover, h?

t1 = 2 #s
t2 = 7 #s

def tank(level,time,c,valve):
    rho = 1000.0 #kg/m^3
    A = 1.0 #m^2
    c = 50.0 #kg/s
    dldt = (c/(rho*A)) * valve
    return dldt
ts = np.linspace(0,10,101)

u = np.zeros(101)
u[21:70] = 100.0

level0 = 0
z = np.zeros(101)

for i in range(100):
    valve = u[i+1]
    y = odeint(tank,level0,[0,0,1], args=(c,valve))
    level0 = y[-1]
    z[i+1] = level0

plt.figure()
plt.subplot(2,1,1)
plt.plot(ts,z,'b-')
plt.ylabel('Tank level')
plt.subplot(2,1,2)
plt.plot(ts,u,'r--')
plt.xlabel('valve')
plt.ylabel('Time')
plt.show()
