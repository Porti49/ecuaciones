#Inicializacion
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

#y = odeint(model,y0,t)

def model(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x+u)/2.0
    dydt = (-y+x)/5.0
    return [dxdt,dydt]
n = 150
z0 = [0,0]
t = np.linspace(0,15,n)
u = np.zeros(n)
u[51:] = 2.0

x = np.zeros(n)
y = np.zeros(n)

for i in range(1,n):
    tspan = [t[i-1],t[i]]
    z = odeint(model,z0,t,args = (u[i],))
    z0 = z[1]
    x[i] = z0[0]
    y[i] = z0[1]
plt.plot(t,u,'k--')
plt.plot(t,x,'r-',t,y,'b--')

plt.legend(['u(t)','x(t)','y(t)'],loc='best')
plt.show()



