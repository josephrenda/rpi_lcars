import RPi.GPIO as GPIO
from time import sleep

"""
Relay is connected to pin 32 (IN), and 4 for VCC and 6 from Ground
"""

def AlarmOn():
    relayPin = 32
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin, GPIO.HIGH)
    return

def AlarmOff():
    relayPin = 32
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.OUT)
    GPIO.output(relayPin, GPIO.LOW)
    return



