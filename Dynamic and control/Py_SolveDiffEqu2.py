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

#y = odeint(model,y0,t)

def model(y,t,k):
    dydt = -k * y
    return dydt
y0 = 5
t = np.linspace(0,20)
k = 0.1
y1 = odeint(model,y0,t,args=(k,))
k = 0.3
y2 = odeint(model,y0,t,args=(k,))
plt.plot(y1,t,'r--',label='k=0.1')
plt.plot(y2,t,'b-',label='k=0.3')
plt.legend(loc='best')
plt.show()



