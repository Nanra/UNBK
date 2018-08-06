import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

while True:
    GPIO.output(16, True)
    time.sleep(1)
    GPIO.output(16, False)
    time.sleep(1)
