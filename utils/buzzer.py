#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys

BUZZER_PIN = 11

def tuneOn(frequency):
    GPIO.setmode(GPIO.BOARD)                # Numbers GPIOs by physical location
    GPIO.setup(BUZZER_PIN, GPIO.OUT)    # Set pins' mode is output
    global Buzz                                             # Assign a global variable to replace GPIO.PWM
    Buzz = GPIO.PWM(BUZZER_PIN, frequency)      # 440 is initial frequency.
    Buzz.start(50)                                  # Start BUZZER_PIN pin with 50% duty ration

def tuneOff():
    Buzz.stop()                                     # Stop the buzzer
    GPIO.output(BUZZER_PIN, 1)          # Set BUZZER_PIN pin to High
    GPIO.cleanup()                          # Release resource

def beep(duration, frequency = 3000):
    tuneOn(frequency)
    time.sleep(duration)
    tuneOff()

if __name__ == '__main__':              # Program start from here
    frequency = float(sys.argv[1])
    try:
        beep(0.07, frequency)
    except KeyboardInterrupt:       # When 'Ctrl+C' is pressed, the child program tuneOff() will be  executed.
        tuneOff()
