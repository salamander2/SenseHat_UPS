#!/usr/bin/python
import subprocess
from sense_hat import SenseHat
'''
This program reads the battery stats via APCUPS connection (over USB port).
It then displays the following info:

Top row = battery %. Green pixels on red background. Each green pixel = 10%
2nd row = load %     Magenta pixels on pale background. Each magenta pixel = 10%
Printed numbers: 	 Time left in minutes. (I think this is in blue).
Author: Michael Harwood, June 2022
'''
def status():
   proc = subprocess.Popen(["apcaccess", "status"], stdout=subprocess.PIPE)
   proc.wait()
   
   #print (proc)
   #print ([proc])
   
   #variables:
   online=False
   timeleft=-1
   pct=-1
   load=-1
   
   #--- Parse APC Status Output ---
   #apcout = []
   for line in iter(proc.stdout.readline,''):
      #print line  --- this will doublespace the lines
      text = line.rstrip()
      #print text
   
      #apcout.append(text)
      if text.find("STATUS") >=0 :
         if text.find("ONLINE") >=0 : online=True
   
      if text.find("BCHARGE") >=0 :
         x = text.split(" ")
         pct=float(x[3])
   
      if text.find("TIMELEFT") >=0 :
         x = text.split(" ")
         timeleft=int(float(x[2]))
   
      if text.find("LOADPCT") >=0 :
         x = text.split(" ")
         load=float(x[3])
   
   if (online) :
      #round to nearest 10%
      pct = int((pct+5)/10)  
      load = int((load+5)/10)  
   else:
      #DEBUG / DEMO
      pct=7
      load=3
      timeleft=37

   print "\nOutputs:"
   print online
   print "batt=" , pct
   print "time=" , timeleft
   print "load=" , load
   
   sense = SenseHat()
   sense.low_light = True
   sense.clear()
   
   K = (0,0,0)
   R = (255, 0, 0)
   G = (0, 255, 0)
   B = (0, 0, 255)
   Y = (255, 255, 0)
   M = (255, 0, 255)
   C = (0, 255, 255)
   W = (255, 255, 255)
   
   #--- Set the Battery % ----
   #--- across the top row
   #set all pixels red
   for i in range(8):
     sense.set_pixel(i,0, R)
   for i in range(pct):
     sense.set_pixel(i%8, 0, G)
   
   if pct>8: sense.set_pixel(7, 0, W)
   if pct>9: sense.set_pixel(6, 0, W)
   
   #--- Set the Load % ----
   #--- second row across the tope
   for i in range(8):
     sense.set_pixel(i,1, (100,100,100))
   for i in range(load):
     sense.set_pixel(i%8,1, M)
   
   #sense.set_pixel(0,0,C)
   
   def displayDigit(n,xo,yo,c):
     
   #this will clear a digit
   #displayDigit(10,3,5,B)
   #--- print a digit
   # 3x5 digit display. Replace 1 with colour
     digits = [
       [1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
       [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0],
       [1,1,1,0,0,1,1,1,1,1,0,0,1,1,1],
       [1,1,1,0,0,1,1,1,1,0,0,1,1,1,1],
       [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1],
       [1,1,1,1,0,0,1,1,1,0,0,1,1,1,1],
       [1,1,1,1,0,0,1,1,1,1,0,1,1,1,1],
       [1,1,1,0,0,1,0,0,1,0,0,1,0,0,1],
       [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
       [1,1,1,1,0,1,1,1,1,0,0,1,1,1,1]
     ]
     
     K=(0,0,0)
     cnt=0
     for y in range(5):
       for x in range(3):
         if n>9 :
           sense.set_pixel(x+xo, (y+yo), K )
         else:
           sense.set_pixel(x+xo, (y+yo), (K,c)[digits[n][cnt]] )
           cnt+=1
   
   
   displayDigit(timeleft/10,1,3,B)
   displayDigit(timeleft%10,5,3,B)
   
   
   #DEBUG
   #sense.set_pixel(0,0,red)
   #displayDigit(4,1,3,R)
   
   #event = sense.stick.wait_for_event()
   #sense.clear()
