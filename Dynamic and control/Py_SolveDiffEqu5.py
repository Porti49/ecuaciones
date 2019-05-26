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

def model(z,t):
    x = z[0]
    y = z[1]
    dxdt = 3.0*np.exp(-t)
    dydt = 3.0-y
    return [dxdt,dydt]
z0 = [0,0]
t = np.linspace(0,30,100)
z = odeint(model,z0,t)

x = z[:,0]
y = z[:,1]
plt.plot(t,x,'r-',t,y,'b--')

plt.legend(['x(t)','y(t)'],loc='best')
plt.show()



