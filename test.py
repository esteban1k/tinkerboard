import ASUS.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

GPIO.output(3,GPIO.HIGH)
time.sleep(2)
GPIO.output(3,GPIO.LOW)
time.sleep(2)
GPIO.output(3,GPIO.HIGH)
time.sleep(2)
GPIO.output(3,GPIO.LOW)
