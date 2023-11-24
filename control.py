#!/usr/bin/python
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
import showTemp, rainbow, apcups, shutdown
#import subprocess

#sense.set_rotation(90)
#sense.stick.rotation(90)

# Set up main display
# Left = X (shutdown)
# up = U (UPS status)
# right = rainbow
# down = Temp, humidity
# centre = end program
def mainDisplay():
   pixels = [
       [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [255,   0, 255], [  0,   0,   0], [255,   0, 255], [  0,   0,   0],
       [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [255,   0, 255], [255,   0, 255], [255,   0, 255], [  0,   0,   0],
       [255,   0,   0], [120,  80,  80], [255,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0],
       [120,  80,  80], [255,   0,   0], [120,  80,  80], [  0,   0,   0], [255, 255, 255], [  0,   0,   0], [  0,   0,   0], [255,   0,   0],
       [255,   0,   0], [120,  80,  80], [255,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [255, 200,   0],
       [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0, 255,   0],
       [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0, 222, 222], [  0, 222, 222], [  0, 222, 222], [  0,   0,   0], [  0,   0, 255],
       [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0, 222, 222], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0]
   ]
   sense.clear()
   sense.set_pixels(pixels)
#---------------------------------

#event = sense.stick.wait_for_event()

mainDisplay()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
         apcups.status()	 
         sleep(1)
         sense.stick.wait_for_event(emptybuffer=True)
         mainDisplay()
         continue
#        sense.show_letter("U")      # Up arrow
      elif event.direction == "down":
        showTemp.showTemp()
      elif event.direction == "left":         
        sense.clear()
        shutdown.shutdown()
      elif event.direction == "right":
        rainbow.rainbow()
        sleep(2)
      elif event.direction == "middle":
        sense.clear()
        exit()      # Enter key
      
      # Wait a while and then clear the screen
      sleep(0.7)
      mainDisplay()
