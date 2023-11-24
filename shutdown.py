#!/usr/bin/python
#import subprocess
import os

def shutdown():
  #proc = subprocess.Popen(["sudo", "shutdown", "-P", "now"])
  os.system('sudo /home/corona/mypi/shutdown.sh')


