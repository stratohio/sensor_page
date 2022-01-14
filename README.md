# sensor_page
This is a raspberry pi project to develop web page for MS8607 PHT sensor

It develops an Apache2 web page to graph MS8607 sensor logs. 
Temperature.html can nearly be used as a template to draw line graphs by changing 
titles, csv file references, and the data pointers.
Check for additional documentation at
https://stratohio.wordpress.com/2021/12/23/ms8607-weather-station-graphs/
A version of that post is in the docs directory as a .pdf file.

Relevent files are is the src directory. Most important are: read_sense.py, 
Temperature.html, Pressure.html, Humidity.html, and  MS8607_sensors.html.

read_sense.py in the src directory uses the 
adafruit_circuitpython_ms6807 library to log Pressure, Humidity, and Temperature, 
as well as DateTime of the readings.  The user runs the file periodically using 
crontab.  The user needs write access to /var/www/html/data to write and append 
data to the sense.csv file. 

Temperature.html is the code to generate a plot.  It uses D3,  
<script src=
        "https://d3js.org/d3.v7.js">
    </script>
 library, installed locally in the ../src directory.
 
 I assume the web structure is 
 
 /var/www/html/html/Temperature.html
 
 /var/www/html/html/Pressure.html
 
 /var/www/html/html/Humidity.html
 
 /var/www/html/html/MS8607_sensors.html
  
 /var/www/html/src/d3.v7.min.js (or d3.v7.js)
 
 /var/www/html/data/sense.csv  - sample data
 
 /var/www/html/css/main.css - my css file, for formating local web pages.
 Yours is probably better.
 
 update 22-01-05
 read_sense.py has been updated to include a dew point calculation.
 sense.csv sample data has been updated to include dew point.
 DewPoint.html has been added to plot DewPoint data.
 
 Documentation:
 Humidity_220104.pdf discusses how to calculate water vapor saturation pressures and Dew Points.
 
 update 22-01-08
 read_sense.py updated to Alduchov & Eskridge formula and coefficients
 test_dp.py check/verify dew point calculation.  
  
 update 22-01-10
 added Temp_DP.html
 plot both temperature and dew point on save graph
 
 Contact:
 If you try to use this code, please let me know of your experience.
 stratohio40 (at) gmail.com
