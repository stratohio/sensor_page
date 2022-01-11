#!/usr/bin/python3
# Test Dew Point routine

import math

def dp1( t,h):
	lamda=5390.0
	K0 = 273.15
	dp = lamda*(t+K0) / (lamda - ((t+K0) * math.log(h)))
	
	return dp-K0

# there are discrepancies between libreOffice Calc ln()
# and python math.log()
# my HP 33S agrees with python 

def dp2(t,h):
	beta = 17.625
	lamda = 243.04
	dp1 = lamda * (math.log(h)+((beta*t)/(lamda+t))) 
	dp = dp1/(beta - (math.log(h)+ ((beta*t)/(lamda+t))))
	return dp

temp = [30.0,25.0,20.0,15.0,10.0,0.0]
hum = [42.5,31.7,23.4,17.1,12.3,6.1]

for i in range(0,6):
	print (i, temp[i], hum[i]/hum[0], dp1(30.0,hum[i]/hum[0]),
	  dp2(30.0,hum[i]/hum[0]),math.log(hum[i]/hum[0]))

