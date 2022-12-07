from numpy import * 
from pandas import * 
from sympy import * 
from math import *
from decimal import Decimal

#Defining commonly used variables in quantum chemistry

h = 6.6260755e-34                #This is, of course, in Joules * second**-1

h_bar = 1.05457266e-34           #This if, of course, in Joules * second**-1

c = 299792458                    #In units of, meters * second**-1


#Example 1-2 asks to compute a thresold frequency for sodium, given the work function for sodium metal. 
#Python can easily be used to generate a general function, which can compute the thresold frequency of any metal, given the work function. For example: 

def fun(x): 
    z= x * (1.602e-19)           #Converts Electron Volts to Joules, so that the thresold frequency will have units of Hz 
    y = z / h                    #Equation 1.7, which computes the thresold frequency for a metal, given the work function, in Joules 
    print("The thresold frequency of your metal, in Hertz, is: " '%E' % y)              #Displays the thresold frequency, in Hertz
    l= c / y                     #Transforms the thresold frequency, in Hertz, to wavelength, in meters 
    n = l * 1.0e9               #Converts the thresold frequency, in meters, to nanometers
    print("Or the thresold frequency, in nanometers, would be: ",  n)                   #Displays the thresold frequency, in nanometers



#Example 1-3 Given the Kinetic Energies of an ejected electron from the Lithium atom, at two different wavelengths, compute (a) The Plank Constant, (b) the threshold frequency,
#The work function of Lithium from the provided data


#Solution to Example 1-3, using ONE function!




def planckwave(K1,K2,w1,w2):     #Here Kn represents the nth Kinetic Energy term & wn represents the nth wavelength (in nm) corresponding to the nth Kinetic Energy term
    W1=w1*1.0e-9                 # Transfroms nth wavelength in nanometers (nm) to meters (m)
    W2=w2*1.0e-9
    hneed=(K1-K2)/(c*((1/W1)-(1/W2)))
    print("Thus, we find Planck's constant (in Joule Seconds) to be:", hneed)
    funda=(c/W1)-(K1/hneed)             #Solution to Example 1-3.b using the value for Plancks constant found in part a of problem
    print("Therefore, the fundamental frequency of the Lithium atom (in Hertz) would be the folloiwng:", funda)
    work=hneed*funda
    print("Using our value of Planck's constant and our computed fundamental frequency, we can say the work function(in Joules) of the lithium atom would be the following:", work)

