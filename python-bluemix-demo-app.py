import time
import datetime
import requests
import pytz
import demjson
import os
import sys

woeid = '2487956'#Sanfrancisco where on earth identification 

while(1):
	
	try:	
		weather_api = requests.get("https://query.yahooapis.com/v1/public/yql?q=select item.condition from weather.forecast where woeid= \'"+str(woeid)+"\'&format=json")
		weather_data = weather_api.text
		weather = demjson.decode(weather_data)
	except Exception as error_weatherapi:
		print "The error_weatherapi Exception is %s,%s"%(error_weatherapi,type(error_weatherapi))

	
	print '\n\t\tThis is python bluemix Demo app\n'
	
	print  datetime.datetime.now(pytz.timezone('US/Pacific'))
	
	if (weather_api.status_code == 200 and weather_api.reason == 'OK'):
		print "\nweather api call was successfully executed"
		print "\nThe Sanfrancisco Temparature is %s"%(weather['query']['results']['channel']['item']['condition']['temp'])
		print "\nThe Sanfrancisco Weather is %s"%(weather['query']['results']['channel']['item']['condition']['text'])
	else:
		print 'weather api call was not successfull'
		print 'reason',weather_api.reason
		print 'status_code',weather_api.status_code
	
	time.sleep(600)







