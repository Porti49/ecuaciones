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

R = 25 * u.feet
L = 5 * u.meter
V = pi*R**2*L
print(V.to('m**3'))
