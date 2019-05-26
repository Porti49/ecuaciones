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

c = c *u.meter /u.sec
print(c.to('km/hour'))

rho = 62.4 *u.lb / u.ft**3
print(rho.to('kg/m**3'))

Rg = Q(0.08206,'L*atm/(mole*K)')
print(Rg.to('J/(mole*K)'))

print(Rg.to('BTU/((lb/gram*mole)*degR)'))

Length=300
yard_per_cubit = 0.5
print(Length*yard_per_cubit)
