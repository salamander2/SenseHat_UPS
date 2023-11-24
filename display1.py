#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear(255, 25, 255)
sense.low_light = True
sense.show_letter('3')
sleep(1)
sense.clear()

#event = sense.stick.wait_for_event()
#print("The joystick was {} {}".format(event.action, event.direction))


temp = sense.get_temperature()
print("Temperature: %.1f C" % temp)

humidity = sense.get_humidity()
print("Humidity: %.1f %%rH" % humidity)
