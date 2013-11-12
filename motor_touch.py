import RPi.GPIO as GPIO
import mpr121
from Adafruit_PWM_Servo_Driver import PWM
import time
import servo_driver

# Initialise the PWM device using the default address                                                           
servoMin = 150  # Min pulse length out of 4096                              
servoMax = 600  # Max pulse length out of 4096 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x30
mpr121.setup(0x5a)

touches = [0,0,0]

while 1:

    if (GPIO.input(7)): # Interupt pin is high
        pass
    else:
        touchData = mpr121.readData(0x5a)
        
        for i in range(3):
            if (touchData & (1<<i)):
                if (touches[i] == 0):
                    print 'Pin ' + str(i) + ' was just touched.'
                touches[i] = 1
                if i == 0:
                    servo_driver.setPosition(0,0)
                if i == 1:
                    servo_driver.setPosition(0,90)
                if i == 2:
                    servo_driver.setPosition(0,180)
            else:
                if (touches[i] == 1):
                    print 'Pin ' + str(i) + ' was just released.'
                touches[i] = 0


#while (True):
  # Change speed of continuous servo on channel O                                                                 
#  pwm.setPWM(0, 0, servoMin)
#  time.sleep(1)
#  pwm.setPWM(0, 0, servoMax)
#  time.sleep(1)

