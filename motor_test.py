import servo_driver
import time

# A short program to test a motor. Spins it in one
# direction for five seconds, and then switches. 
# It is important to add a keyboard interrupt, as the 
# signal stays "stuck" after the program is shut down
# otherwise.

servo_driver.motorsOn()
try:
    while 1:
        print("clockwise")
        servo_driver.setMotorSpeed(0,1,-.1)
        time.sleep(5)
        print("counter clockwise")
        servo_driver.setMotorSpeed(0,1,.1)
        time.sleep(5)
   # print("still")
   # servo_driver.setMotorSpeed(0,1,0)
   # time.sleep(5)
except:
    servo_driver.motorsOff()
