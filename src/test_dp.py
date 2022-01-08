#!/usr/bin/python3
# Test Dew Point routine

import math

def dp1( t,h):
	lamda=5390.0
	K0 = 273.15
	dp = lamda*(t+K0) / (lamda - ((t+K0) * math.log(h/100.0)))
	
	return dp-K0

# there are discrepancies between libreOffice Calc ln()
# and python math.log()
# my HP 33S agrees with python 

def dp2(t,h):
	beta = 17.625
	lamda = 243.04
	dp1 = lamda * (math.log(h/100.0)+((beta*t)/(lamda+t))) 
	dp = dp1/(beta - (math.log(h/100.0)+ ((beta*t)/(lamda+t))))
	return dp

temp = [30.0,25.0,20.0,15.0,10.0,0.0]
hum = [100.0,75.0,55.0,40.0,29.0,14.0]

for i in range(0,6):
	print (i, temp[i], hum[i], dp1(30.0,hum[i]),dp2(30.0,hum[i]),math.log(hum[i]/100.0))

