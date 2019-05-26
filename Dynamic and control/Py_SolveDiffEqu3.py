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

def model(y,t):
    dydt = -y+1.0
    return dydt
y0 = 0
t = np.linspace(0,20)
y = odeint(model,y0,t)
plt.plot(t,y,'r--',label='k=0.1')
plt.legend(loc='best')
plt.show()



