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
    h = z[0]
    I = z[1]
    v = z[2]
    kr1 = 1e5
    kr2 = 0.1
    kr3 = 2e-7
    kr4 = 0.5
    kr5 = 5
    kr6 = 100
    dhdt = (kr1-kr2*h-kr3*h*v)
    didt = (kr3*h*v-kr4*I)
    dvdt = (-kr3*h*v-kr5*v+kr6*I)
    return [dhdt,didt,dvdt]
n = 150
z0 = [1000000,0,100]
t = np.linspace(0,15,n)
u = np.zeros(n)
u[51:] = 2.0

h = np.zeros(n)
I = np.zeros(n)
v = np.zeros(n)

for i in range(1,n):
    tspan = [t[i-1],t[i]]
    z = odeint(model,z0,t,args = (u[i],))
    z0 = z[1]
    h[i] = z0[0]
    I[i] = z0[1]
    v[i] = z0[2]
plt.semilogy(t,h,'b-',t,I,'g:',t,v,'r--')

plt.legend(['h(t)','I(t)','v(t)'],loc='best')
plt.show()



