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

def model(z,t):
    x = z[0]
    y = z[1]
    """
    if (t<10.0):
        u=0.0
    else:
        u=2.0
    """
    k = 5    
    dxdt = 3.0*np.exp(-t)
    dydt = 3.0-y
    return [dxdt,dydt]

#Condicion inicial
z0 = [0,0]
#time points
t = np.linspace(0,10)
#Solve ODE
z = odeint(model,z0,t)
x = z[:,0]
y = z[:,1]
#plot results
plt.plot(t,x,'r--')
plt.plot(t,y,'bo')
plt.xlabel('time')
plt.legend(['x(t)','y(t)'])
plt.show()
