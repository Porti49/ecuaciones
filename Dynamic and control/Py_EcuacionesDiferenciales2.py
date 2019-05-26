#Inicialización
import sympy as sp
import scipy as sc
from sympy.solvers import solve
from scipy.optimize import fsolve
from scipy.constants import g,pi
from scipy.misc import derivative as drv
from scipy.integrate import quad 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#funcion que retorna dy/dt

def model(z,t,u):
    x = z[0]
    y = z[1]
    """
    if (t<10.0):
        u=0.0
    else:
        u=2.0
    k = 5
    """
    dxdt = (-x+u)/2
    dydt = (-y+x)/5
    return [dxdt,dydt]

#Condicion inicial
z0 = [0,0]
#time points
n = 150
t = np.linspace(0,15,n)
u = np.zeros(n)
u[51:] = 2.0
x = np.zeros(n)
y = np.zeros(n)

#Solve ODE
for i in range(1,n):
    tspan = [t[i-n],t[i]]
    z = odeint(model,z0,t,args=(u[i],))
    z0 = z[1]
    x[i] = z0[0]
    y[i] = z0[0]
    
#plot results
plt.plot(t,u,'k:')
plt.plot(t,x,'r-')
plt.plot(t,y,'b--')
plt.xlabel('time')
plt.legend(['u(t)','x(t)','y(t)'])
plt.show()
