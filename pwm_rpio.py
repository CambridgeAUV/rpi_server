from RPIO import PWM
import time

s = PWM.Servo()
s.set_servo(12, 1500)
input('stop')
s.stop_servo(12)

#time.sleep(3)
#s.set_servo(12, 1900)
#time.sleep(10)
#s.stop_servo(12)
