# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:44:42 2013
@author: Julian Surmann
"""
#Using the magic encoding
#-*- coding: utf-8 -*-
from scipy import * 
import matplotlib.pyplot as plt
from uncertainties import *
import math
from numpy import linspace
from scipy.constants import *

def make_LaTeX_table(data,header, flip= 'false', onedim = 'false'):
    output = '\\begin{table}\n\\centering\n\\begin{tabular}{'
    #Get dimensions
    if(onedim == 'true'):
        if(flip == 'false'):
        
            data = array([[i] for i in data])
        
        else:
            data = array([data])
    
    row_cnt, col_cnt = data.shape
    header_cnt = len(header)
    
    if(header_cnt == col_cnt and flip== 'false'):
        #Make Format
        
        for i in range(col_cnt):
            output += 'l'
        output += '}\n\\toprule\n{'+ header[0]
        for i in range (1,col_cnt):
            output += '} &{ ' + header[i]
        output += ' }\\\\\n\\midrule\n'
        for i in data:
            if(isinstance(i[0],(int,float,int32))):
                output +=  str( i[0] ) 
            else:
                output += ' ${:L}$ '.format(i[0])
            for j in range(1,col_cnt):
                if(isinstance(i[j],(int,float,int32))):
                    output += ' & ' + str( i[j])   
                else:          
                    output += ' & ${:L}$ '.format(i[j])                
                
            output += '\\\\\n'
        output += '\\bottomrule\n\\end{tabular}\n\\label{}\n\\caption{}\n\\end{table}\n'
                            
        return output

    else:
        return 'ERROR'



    
def err(data):
    mean = data.mean()
    N = len(data)
    err = 0
    for i in data:
        err += (i - mean)**2
    err = sqrt(err/((N-1)*N))
    return ufloat(mean,err)


def lin_reg(x,y):
    N = len(x)
    sumx = x.sum()
    sumy = y.sum()
    sumxx = (x*x).sum()
    sumxy = (x*y).sum()
    m = (sumxy -  sumx*sumy/N)/(sumxx- sumx**2/N)
    b = sumy/N - m*sumx/N
    
    sy = sqrt(((y - m*x - b)**2).sum()/(N-1))
    m_err = sy *sqrt(N/(N*sumxx - sumx**2))
    b_err= m_err * sqrt(sumxx/N)
    return m,b,m_err,b_err

# Auslesen der Messwerte


#Helmholtzfunktion

def B_HelH(x, I , R, d):
    return (mu_0*I/2)*((R**2+(x+0.5*d)**2)**-1.5+(R**2+(x-0.5*d)**2)**-1.5)
x11, b11 = loadtxt("messwerte11.txt", unpack=True)
x12, b12 = loadtxt("messwerte12.txt", unpack=True)
x13, b13 = loadtxt("messwerte13.txt", unpack=True)
x21, b21 = loadtxt("messwerte21.txt", unpack=True)
x22, b22 = loadtxt("messwerte22.txt", unpack=True)
x23, b23 = loadtxt("messwerte23.txt", unpack=True)

#Kurven verschieben

x11 -= 3.0
x12 -= 1.25
x13 -= 8
x21 -= 18
x22 -= 24
x23 -= 29


x11 *= 1e-2
x12 *= 1e-2
x13 *= 1e-2
x21 *= 1e-2
x22 *= 1e-2
x23 *= 1e-2
# Plots der experimentellen Werte
# Spulenpaar 10 cm:
x = linspace(-0.08,.18)
plt.plot(x11,b11,'x',label = "Messwerte")
plt.plot(x,1e3*B_HelH(x, 2.78, 0.0625, 0.1),label = "Theoriekurve")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")
#plt.xlim(-3, 18)
#plt.ylim(0, 3)
plt.legend()
plt.savefig("e11.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet
#Spulenpaar 6.25cm:
plt.plot(x12,b12,'x',label = "Messwerte")
x = linspace(-0.01,.18)
plt.plot(x,1e3*B_HelH(x, 2.78, 0.0625, 0.0625),label = "Theoriekurve")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")
#plt.xlim(0, 21)
#plt.ylim(0, 4)
plt.legend()
plt.savefig("e12.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet
#Spulenpaar 20cm:
plt.plot(x13,b13,'x',label = "Messwerte")
x = linspace(-0.08,.08)
plt.plot(x,1e3*B_HelH(x, 2.78, 0.0625, 0.2),label = "Theoriekurve")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")
#plt.xlim(0, 16)
#plt.ylim(0, 2.5)
plt.legend()
plt.savefig("e13.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet
#Lange Spule:
plt.plot(x21,b21,'x',label = "Messwerte")
x = linspace(-.09, .24)
B = ones(50)*1e3*mu_0*(3400/0.1)*0.7
plt.plot(x, B, label = "Theoriekurve")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")
#plt.xlim(0, 45)
plt.ylim(0, 35)
plt.legend()
plt.savefig("e21.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet
#Mittlere Spule:
plt.plot(x22,b22,'x',label = "Messwerte")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")
x = linspace(-.15, .27)
B = ones(50)*1e3*mu_0*(3400/0.1)*0.8
plt.plot(x, B, label = "Theoriekurve")
plt.legend()
plt.savefig("e22.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet
#Kurze Spule:
plt.plot(x23,b23,'x',label = "Messwerte")
plt.xlabel("x [m]")
plt.ylabel("B [mT]")

x = linspace(-.2, .25)
B = ones(50)*1e3*mu_0*(3400/0.1)*0.8
plt.plot(x, B, label = "Theoriekurve")
plt.legend()
plt.savefig("e23.png")
plt.show()
plt.close() # Hiermit wird die Zeichung nach dem speichern resettet

print "Alle Plots gespeichert!"




