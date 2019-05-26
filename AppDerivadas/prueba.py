import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
import pandas as pd
import numpy as np
import pyromat as pyro
import os.path
import random
from sympy import *
from tkinter.messagebox import showinfo


LARGE_FONT= ('Verdana', 12) #Large Font
MEDIUM_FONT= ('Verdana',11) #Medium font
SMALL_FONT= ('Verdana',10) #Small font
style.use('ggplot') #Graph design


class TFM(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Matematicas')
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        
        self.frames = {} 
        for F in (StartPage,Solucion):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)
        
        
    def show_frame(self, page_name):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[page_name]
        frame.grid()
    
    def get_page(self, classname):
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None
        
    def quitProgram(self):
        tfQuit = messagebox.askyesno(title='Close Program', message='Are you sure?')
        if tfQuit:
            self.destroy()
    


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text='Derivadas y Límites', font=LARGE_FONT)
        label.grid(column=0,row=0,columnspan=99,sticky='SNEW')
        
    
        #T1_input value
        #Default: 300K
        v1=tk.Label(self,text='Introduce tu f(x)')
        v1.grid(column=0,row=2, sticky='E')
        
        self.T1_input=tk.DoubleVar()
        self.T1_input.set('')
        self.T1_entry=tk.Entry(self,textvariable=self.T1_input, width=30)
        self.T1_entry.grid(column=1,row=2)        
        
        u1=tk.Label(self,text='')
        u1.grid(column=2,row=2, sticky='W')
        
        v1=tk.Label(self,text='Cosas de interes: todo en función de x')
        v1.grid(column=2,row=70, sticky='E')
        v1=tk.Label(self,text='Raices cuadradas: sqrt(FUNCIÓN)')
        v1.grid(column=2,row=71, sticky='E')
        v1=tk.Label(self,text='X elevado a NÚMERO: x**NÚMERO')
        v1.grid(column=2,row=72, sticky='E')
        v1=tk.Label(self,text='Seno y coseno: sin() y cos()....(en ingles vaya)')
        v1.grid(column=2,row=73, sticky='E')
        v1=tk.Label(self,text='Multiplicaciones y divisiones: *, / ...(2x+1: mal, 2*x+1: bien)')
        v1.grid(column=2,row=74, sticky='E')
        v1=tk.Label(self,text='número e: exp()')
        v1.grid(column=2,row=75, sticky='E')
        
        
        
        
        #Empty rows
        f1=tk.Label(self,text="",height=1)
        f1.grid(column=0,row=98, columnspan = 999)
                
        #Empty columns
        c1=tk.Label(self,text="",width=10)
        c1.grid(column=98,row=2,rowspan = 999)
        
        #Buttons
        button1 = ttk.Button(self,text = 'Derivada' , command=self.deriv)
        button1.grid(column=99,row=2,sticky='E')
        
        button2 = ttk.Button(self,text = 'Limite al infinito', command=self.limiteInf)
        button2.grid(column=99,row=3,sticky='E')
        
        self.buttonQuit = ttk.Button(self,text='Calcular límite', command=self.limit)
        self.buttonQuit.grid(column=99,row=4,sticky='SE')
        
        v1=tk.Label(self,text='Tu límite tiende a: ')
        v1.grid(column=0,row=4, sticky='E')
        self.p1_input=tk.DoubleVar()
        self.p1_input.set('')
        self.p1_entry=tk.Entry(self,textvariable=self.p1_input, width=5)
        self.p1_entry.grid(column=1,row=4, sticky='W')  
        
    def limiteInf(self):
        StartPage = self.controller.get_page("StartPage")   
        Ecu=StartPage.T1_entry.get()
        showinfo('Solución',limit(Ecu,x,oo))
    def deriv(self):
        StartPage = self.controller.get_page("StartPage")   
        Ecu=StartPage.T1_entry.get()
        showinfo('Solución', diff(Ecu,x))
    def limit(self):
        StartPage = self.controller.get_page("StartPage")   
        Ecu=StartPage.T1_entry.get()
        Tiende=StartPage.p1_entry.get()
        showinfo('Solución',limit(Ecu,x,Tiende))

class Solucion(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text='Matematicas', font=LARGE_FONT)
        label.grid(column=0,row=0,columnspan=99,sticky='SNEW')
        label = tk.Label(self, text='Variables', font=MEDIUM_FONT)
        label.grid(column=0, row=1,columnspan=99,sticky='W')
        
app = TFM()
app.mainloop()









