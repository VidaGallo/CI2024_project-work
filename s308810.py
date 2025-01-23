import numpy as np


def f1(x: np.ndarray) -> np.ndarray: 
    return  np.sin(x[0])                 
            #sin(x_1)


def f2(x: np.ndarray) -> np.ndarray: 
    return ((x[0] + (x[1] * np.sin(57.176))) * ((((x[0] * (-69.689)))**2 * ((5.9695 * 0.1291) - (x[0] * (x[1] * np.sin(0.7147))))) + 1077248.0))
        

def f3(x: np.ndarray) -> np.ndarray: 
    return ((x[0] * x[0]) - (((x[2] * 2.7713) + ((x[2] + -4.0) - (x[0])**2)) + (x[1])**3))
          

def f4(x: np.ndarray) -> np.ndarray:               
    return  (np.cos(x[1]) + np.cos(x[1]))  +  (((np.cos(x[1]) + np.cos(x[1])) + (2.5831 + (np.cos(x[1]) + np.cos(-5.5859)))) + (np.cos(x[1]) + np.cos(x[1])))               
           

def f5(x: np.ndarray) -> np.ndarray: 
    return (x[0] * -1.7161875e-13)*(((-3.538 + x[1]) + x[1]) * ((((((x[0] + -3.538) + x[1]) + x[1]) + (((x[0] + -3.538) + x[1]))**2) + x[1]))**2)
          

def f6(x: np.ndarray) -> np.ndarray: 
    return  0.6983 * x[1] - (-0.1425 * (x[0] + x[0])) + x[1] - (-0.052744) - x[0]       
          

def f7(x: np.ndarray) -> np.ndarray:  
    return  np.exp((((x[0] * x[1]) - (-0.8597)**3)) - (-0.8597))
     

def f8(x: np.ndarray) -> np.ndarray: 
     return  ((np.sqrt(11.1)*(2*(x[3]*np.cos(x[3])))  - 121.11*(x[4] + (x[4] * np.sin(x[4]))) + 1501 * x[5]*(1-((np.sin(x[5])))**2 - 1011* np.sin(x[5])*(np.cos(x[5])) )))*np.exp(-12.5550)  +   (((61.4442 * x[3]) +  (x[0] + (x[1] * 7.88)) * ((((x[0] * (-69.689)))))*0.00012 + (1876.3838 * x[5])) + ((-70.8133 * np.sin(x[3]))) + (-2709.4892 * np.sin(x[5]))) - (469.9320 * np.cos(x[4])) +  (23.53340 * (x[3] * np.cos(x[3])))  +  (-165.9250 * (x[4] ** 2))  - (111.9509 * (x[4] * np.sin(x[4]))) +  (1492.5005 * (x[5] * np.cos(x[5]))  - 945.2561 * (np.sin(x[5]) * np.cos(x[5])))
       

    
    #return ((x[0])**2 - (x[1])**3) - (((np.sqrt(0.7597) * (x[2] * 3.9445)) + 2.2772) -13.94)
            #((**2(x_1) - **3(x_2)) - (((sqrt(0.7597) * (x_3 * 3.9445)) + 2.2772) + -13.94))
