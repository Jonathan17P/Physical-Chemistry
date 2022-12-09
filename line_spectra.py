from numpy import * 
from pandas import * 
from sympy import * 

#Python can be used to predict the atomic spectrum of the Hydrogen atom. For example, 

#Example 1-4

#Balmer's Formula 

def balmer(n): 
  for i in array([n]):  
      y=109680*((1/2**2)-(1/i**2))
      lamda=1/y                   #In cm 
      nano=lamda*(1e7)            #converts cm to nm      
      if (nano > 380) & (nano < 450):
         print("This transition requires a photon within the violet spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (nano > 450) & (nano < 485):
         print("This transition requires a photon within the blue spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (nano > 485) & (nano < 500 ):
         print("This transition requires a photon within the cyan spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (nano > 500 ) & (nano < 565  ):
         print("This transition requires a photon within the green spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (nano > 565 ) & (nano < 590  ):
         print("This transition requires a photon within the yellow spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")         
      elif (nano > 590 ) & (nano < 625  ):
         print("This transition requires a photon within the orange spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (nano > 625 ) & (nano < 750 ):
         print("This transition requires a photon within the red spectrum of visible light, since the wavelength of photon required to make this transition is:", round(nano,1), "nm")
      elif (n <= 2) & ( n > 0):
         print("Sorry, this transition requires a lower in energy photon. You may want to look in the IR range")
      elif(n <= 0):
         print("n must not be less then or equal to 0")
      else: 
         print("Sorry, this transition requires a higher in energy photon. You may want to check the UV range.")



#Example 1-5

#Rydberg Formula 

R=109677.581          #Modern value of Rydberg constant, in cm**-1

def rydberg(x,y):
     v=R*((1/(x**2))-(1/(y**2)))
     lamda=1/v                   #In cm
     nano=lamda*(1e7)            #converts cm to nm
     #print(round(nano,3))
     if (nano > 820.6) & (nano < 1876.0):
        print("This transition can be modeled using the Paschen series, since the transition falls within the IR range. This transition requires the following wavelength of photon:", round(nano,2),"nm")
     elif (nano > 364.7) & (nano < 656.5):
        print("This transition can be modeled using the Balmer series, since the transition falls within the Visible range. This transition requires the following wavelength of photon:", round(nano,2), "nm")
     elif (nano > 91.2) & (nano < 121.6):
        print("This transition can be modeled using the Lyman series, since the transition falls within the UV range. This transition requires the followinbg wavelength of photon:", round(nano,2), "nm")
     else:
        print("Are you sure you know what you're doing?")                                                
