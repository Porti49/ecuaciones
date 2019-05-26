import time
import numpy as np
import matplotlib.pyplot as plt

 
def x(n):
    start = time.time()
    re=np.array(0)
    for x in range(1,n): #only integers if you want less you'd need a step
        res = (x**2-7*x+11)**(x**2-13*x+42)
        re = np.append(re, res)
        if res==1:
            print(x)
                    
    t=np.linspace(0,len(re),len(re))
    end = time.time()
    print(end - start)          
    plt.plot(t,re)
    plt.xscale('log')
    plt.show()
                
def xy(n):
    start = time.time()
    re=np.array(0)
    for x in range(1,n):
        for y in range(1,n):
            #res = x**3+y**3 1729
            res = -x**2+2**y 
            re = np.append(re, res)
            if res==615:
                print(x,y)
                    
    t=np.linspace(0,len(re),len(re))
    end = time.time()
    print(end - start)          
    plt.plot(t,re)
    plt.xscale('log')
    plt.show()

def xyz(n):
    start = time.time()
    re=np.array(0)
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                res = z/(x+y)+y/(x+z)+x/(y+z)
                re = np.append(re, res)
                if res==4:
                    print(x,y,z)
                    
    t=np.linspace(0,len(re),len(re))
    end = time.time()
    print(end - start)          
    plt.plot(t,re)
    plt.xscale('log')
    plt.show()

