#!/usr/bin/python3
# read_sense.py
# read data sensors 
# store in csv files

import sys
# import Adafruit_DHT
#sudo pip3 install adafruit-blinka
import board

#sudo pip3 install adafruit_circuitpython_ms6807
from adafruit_ms8607 import MS8607

#import subprocess 
#import re 
import os 
import time 
#import MySQLdb as mdb 
#sudo pip3 install PyMySQL
#import pymysql as mdb 
import datetime

fname="/var/www/html/data/sense.csv"
i2c = board.I2C()
sensor = MS8607(i2c)


def saveToDatabase(temperature,pressure,humidity):

	currentDate=datetime.datetime.now().date()

	now=datetime.datetime.now()
	currentDate = now.date()
	midnight=datetime.datetime.combine(now.date(),datetime.time())
	minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$
#	hours  = ((now-currentDate).seconds)/3600.0 # hours

#	print (now, "  ", currentDate, " \t", minutes/60)

	scmd1 = "INSERT INTO temperatures (temperature,pressure,humidity, dtMeasured,dateMeasured, hourMeasured) "
	scmd2  = "%s,%.2f,%.2f,%.2f,%.2f\n" %(now,temperature,pressure,humidity,minutes)
	print(scmd2)
	f=open(fname,'a')
	f.write(scmd2)
	f.close()
	print ("Saved temperature")
	return ("true")


def readInfo():

#	humidity, temperature = Adafruit_DHT.read_retry(sensor, pinNum)#read_retry - retry getting temperatures for 15 times
	temperature, pressure = sensor.pressure_and_temperature
	humidity = sensor.relative_humidity
	
	
	print ("Temperature: %.1f C" % temperature)
	print ("Humidity:    %.1f %%" % humidity)
	print ("Pressure:    %.1f hpa" % pressure) 

	if humidity is not None and temperature is not None:
		return saveToDatabase(temperature,pressure,humidity) #success, save the readings
	else:
		print ('Failed to get reading. Try again!')
		sys.exit(1)


#check if table is created or if we need to create one

if os.path.exists(fname):  #create file
	print("file ", fname, " exists.")
	
else:
	print("file ", fname, " Does not exist")
	f = open(fname, 'w')
	f.write('Datetime,Temp_C,Pressure_hpa,Humidity_pc,time_m\n')
	f.close()
	print("file ", fname, " Created")

	

#except IOError:
#	pass #table has already been created
	

status=readInfo() #get the readings
