from numpy import * 
from pandas import * 
from sympy import * 


#Calculating the De Broglie wavelength. Example 1-6  

h = 6.6260755e-34                #This is, of course, in Joules * second**-1

h_bar = 1.05457266e-34           #This if, of course, in Joules * second**-1

c = 299792458                    #In units of, meters * second**-1



def oz(x):                         #function that converts mass, in ounces, to mass in kilograms
    m=(x)*(1/16)*(0.454/1)         
    print("Thus, your mass, in kilograms is", m)


def pounds(x):                     #function that converts mass, in pounds, to mass in kilograms
    m=x*(0.454/1)
    print("Thus, your mass, in kilograms is", m) 



def ms(x):                         #function that converts velocity, in miles per hour to meters per second
    v=(x/1)*(1610/1)*(1/3600)
    print("Therefore, your velocity, in meters per second, would be", v)
    



def debrog(m,v):                 # m = mass & must be in kilograms. v = velocity & must be in meters * s**-1
    p=m*v
    w=h/p                          # has units of meters
    nano = w * 1.0e9               # converts the wavelength in meters, to a wavelength in nanometers
    print("Thus, the De Broglie wavelength would be", w, "meters")
    print("Which is, of course, equivalent to", nano, "nanometers")


