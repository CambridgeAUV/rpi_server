import time
import RPi.GPIO as GPIO
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)
p.start(7.3)
#p.start(7.5)
time.sleep(20)
p.start(9.5)

#a = input('waiting...') 
#time.sleep(15)
#p.start(9.5)
b = input('waiting...')
p.stop()
GPIO.cleanup()
