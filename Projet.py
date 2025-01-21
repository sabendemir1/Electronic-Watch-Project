from flask import flask
app = Flask(__name__)
@app.route('/Downloads/Projet.py')
def hello():
    return 'Hello, World!'
import time
from datetime import datetime
from datetime import time as t
import RPi.GPIO as GPIO
"""
from grove.grove_button import GroveButton
BuzzerPin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT)
button = GroveBUtton(22)

import math
import sys
import time
from grove.adc import ADC

import numpy import interp
from grove.factory import Factory

while True:
    if sensor = GroveRotaryAngleSensor(int(sys.argv[1]))

while True
r=sensor.value
time.sleep(.2)
if r <180
num_of_secs =
m, s = divmod(num_of_secs, 60)
min_sec_format = '{:02d}:{:02d}'.format(m, s)
print(min_sec_format)

if r <372:
    print(00 ':'00)
if r <558:  
    print(heure())
if r <744:
    print(temp())
if r <932:
    print(h ':' m)

"""
def heure():
    d = datetime.now().time()
    h = t(d.hour, d.minute,d.second)
    printcœur
    h = 20
    m = 00
def alarme(h,m):
    while True:
        z = datetime.now()
        if z.minute == m and z.hour == h:
            return ('Driiiing')
#buzz = GPIO.PMW(BuzzerPIN,30)
#buzz.start(5.0)
#time.sleep(10)
#buzz = GPIO.PMW(BuzzerPIN,30)
#buzz.stop()

def c():
    num_of_secs = 0
    while True:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format)
        time.sleep(1)
    num_of_secs += 1

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
    print(min_sec_format)
time.sleep(1)
num_of_secs -= 1
#buzz = GPIO.PMW(BuzzerPIN,30)
#buzz.start(5.0)
#time.sleep(10)
#buzz = GPIO.PMW(BuzzerPIN,30)
#buzz.stop()

"""
def temp():
    from grove.helper import helper
    sh = SlotHelper(SlotHelper.ADC)
    pin = 2
    sensor = Factory.getTemper
    while True:
        time.sleep(2)
    print(sensor.temperature)
"""

#def on_press(t):
    #buzz = GPIO.PMW(BuzzerPIN,30)
    #buzz.stop()
    #if rotary angle < 180:
        #print(c())
    #if sensor.value < 372:
        #print countdown()


print(alarme(13,5))
#print(heure())
#print(countdown(250))
#print(c())