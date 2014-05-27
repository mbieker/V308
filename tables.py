
from numpy import loadtxt, linspace
from array import array 
from scipy import constants
from scipy.constants.constants import mu_0
from matplotlib.pyplot import *

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
            if(isinstance(i[0],(int,float))):
                output +=  str( i[0] ) 
            else:
                output += ' ${:L}$ '.format(i[0])
            for j in range(1,col_cnt):
                if(isinstance(i[j],(int,float))):
                    output += ' & ' + str( i[j])   
                else:          
                    output += ' & ${:L}$ '.format(i[j])                
                
            output += '\\\\\n'
        output += '\\bottomrule\n\\end{tabular}\n\\label{}\n\\caption{}\n\\end{table}\n'
                            
        return output

    else:
        return 'ERROR'




#Dateinamen in array speichern

filenumber = [11,12,13,21,22,23]
header = [r"$x / \si{\centi\meter}$",r"$B/\si{\milli\tesla}$"]


for file in filenumber:

    data = loadtxt("messwerte"+str(file)+".txt")
    print make_LaTeX_table(data, header)
    
    
    
    



x = linspace(-.3,.3)

B = B_HelH(x,1.5,0.15,0.15)

plot(x,B)

show()