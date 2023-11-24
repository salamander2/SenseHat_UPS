#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

def showTemp():
	sense = SenseHat()

	temp = sense.get_temperature()
	humidity = sense.get_humidity()

#	print("Temperature: %.1fC" % temp)
#	print("Humidity: %.1f%%" % humidity)

	temp = int(temp+0.5);
	humidity = int(humidity+0.5)

	sense.show_message(str(temp) + "C", text_colour=[155, 255, 255])
	sleep(0.5)
	sense.show_message("H=" + str(humidity) + "%", text_colour=[0, 0, 200])
	sleep(0.5)
