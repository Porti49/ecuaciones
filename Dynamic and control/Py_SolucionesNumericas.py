#Inicialización
import sympy as sp
import scipy as sc
from sympy.solvers import solve
from scipy.optimize import fsolve
from scipy.constants import g,pi,c
from scipy.misc import derivative as drv
from scipy.integrate import quad 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def h(z):
    x = z[0]
    y = z[1]
    f = x**2+y**2 -10.0
    g = x+y+3.0
    return [f,g]

z0 = [1,1]
ans = fsolve(h,z0)
x = ans[0]
y = ans[1]
print(x)
print(y)


