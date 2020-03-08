import RPi.GPIO as GPIO

import time

import pyttsx3
engine = pyttsx3.init()

GPIO.setmode(GPIO.BOARD)

def Button1 ():
    engine.say("Hello, I am a robot")
    engine.runAndWait()
    driving_gesagt()
    Motorstart()
    warten()
    Motorstop()
    information_gesagt()
def Button2 ():
    engine.say("Ble")
    engine.runAndWait()
def warten():
    time.sleep(1.5)
def driving_gesagt():
    engine = pyttsx3.init()
    engine.setProperty('rate',115)
    engine.say("driving")
    engine.runAndWait()
def information_gesagt():
    engine = pyttsx3.init()
    engine.setProperty('rate',115)
    engine.say("this is the color red. I have a button in this color too.")
    engine.runAndWait()
def Motorstart():
    GPIO.setup(7, GPIO.OUT) #1
    GPIO.output(7, GPIO.LOW)#1

    GPIO.setup(11, GPIO.OUT)#1
    GPIO.output(11, GPIO.HIGH)#1 gleiche Richtung

    GPIO.setup(13, GPIO.OUT)#2
    GPIO.output(13, GPIO.HIGH)#2 gleiche Richtung

    GPIO.setup(15, GPIO.OUT)#2
    GPIO.output(15, GPIO.LOW)#2

def Motorstop():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(7, GPIO.OUT) #1
    GPIO.output(7, GPIO.LOW)#1

    GPIO.setup(11, GPIO.OUT)#1
    GPIO.output(11, GPIO.LOW)#1

    GPIO.setup(13, GPIO.OUT)#2
    GPIO.output(13, GPIO.LOW)#2

    GPIO.setup(15, GPIO.OUT)#2
    GPIO.output(15, GPIO.LOW)#2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

LastState1 = GPIO.LOW
LastState2 = GPIO.LOW

while True:
    if GPIO.input(10) == GPIO.HIGH:
        if LastState1 == GPIO.LOW:
            Button1 ()
    LastState1 = GPIO.input(10)
    
    if GPIO.input(11) == GPIO.HIGH:
        if LastState2 == GPIO.LOW:
            Button2 ()
    LastState2 = GPIO.input(11)