# sensor_page
raspberry pi project to develop web page for MS8607 PHT sensor

plan to develop an Apache2 web page to graph MS8607 sensor logs
Check for additional documentation at
https://stratohio.wordpress.com/
Hopefully this will be updatad soon.

read_sense.py in the src directory uses the 
adafruit_circuitpython_ms6807 library to log Pressure, Humidity, and Temperature, 
as well as DateTime of the readings.  The user runs the file periodically using 
crontab.  The user needs write access to /var/www/html/data to write and append 
data to the sense.csv file. 
