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
import pint

u = pint.UnitRegistry()
Q = u.Quantity

T_plate = Q(80,u.degC)
T_h2o = Q(70, u.degF)
L_p = 1 *u.m
DT = T_h2o-T_plate

v=1.45 *u.m/u.sec
mu_h2o = 0.979 * u.centipoise
rho_h2o = 62.3 * u.lb/u.ft**3
k = 0.347 * u.BTU/(u.hr*u.ft*u.degR)
cp = 0.998 * u.BTU/ (u.lb*u.degR)

Pr = mu_h2o * cp /k
print(Pr.to(''))

Re = rho_h2o * L_p * v /mu_h2o
print(Re.to(''))

Nu = 0.332 * Pr**(1.0/3.0)*np.sqrt(Re)
print(Nu.to(''))

h = (Nu * k )/L_p
print(h)

q = h* DT
print(q.to('cal/cm**2/min'))
