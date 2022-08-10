import RPi.GPIO as GPIO
from event_mapping.Mapping3Bh2b import Mapping3Bh2b
from controller import *
from time import sleep
import serial
import time
import board
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

#Object created with respect to the bottom and top HAT
actuator/dcmotor_main = Adafruit_MotorHAT(addr=0x60)
steppermotor_main = Adafruit_MotorHAT(addr=0x61)

#Instances created for acccessing individual DC motors
actuator1 = actuator/dcmotor_main.getMotor(1)
actuator2 = actuator/dcmotor_main.getMotor(2)
dcmotor1 = actuator/dcmotor_main.getMotor(3)
dcmotor2 = actuator/dcmotor_main.getMotor(4)

steppermotor1 = steppermotor_main.getStepper(200,1)



class MyController(Controller):
    
     def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

     def on_L1_press(self):
         actuator1.setSpeed(130) #Speed is set for the motors
         actuator2.setSpeed(130)
         actuator1.run(Adafruit.MotorHAT, FORWARD); #Forward Direction is set for the motors
         actuator2.run(Adafruit.MotorHAT, FORWARD);

     def on_L1_release(self):
         actuator1.run(Adafruit.MotorHAT, RELEASE);
         actuator2.run(Adafruit.MotorHAT, RELEASE);

     def on_R1_press(self):
         actuator1.setSpeed(130) #Speed is set for the motors
         actuator2.setSpeed(130)
         actuator1.run(Adafruit.MotorHAT, BACKWARD); #Reverse Direction is set for the motors
         actuator2.run(Adafruit.MotorHAT, BACKWARD);

     def on_R1_release(self):
         actuator1.run(Adafruit.MotorHAT, RELEASE);
         actuator2.run(Adafruit.MotorHAT, RELEASE);

     def on_left_arrow_press(self):
         dcmotor1.setSpeed(50) #Speed is set for the motors
         dcmotor2.setSpeed(50)
         dcmotor1.run(Adafruit.MotorHAT, BACKWARD); #Reverse Direction is set for the motors
         dcmotor2.run(Adafruit.MotorHAT, BACKWARD);

     def on_right_arrow_press(self):
         dcmotor1.setSpeed(50) #Speed is set for the motors
         dcmotor2.setSpeed(50)
         dcmotor1.run(Adafruit.MotorHAT, FORWARD); #Forward Direction is set for the motors
         dcmotor2.run(Adafruit.MotorHAT, FORWARD);
     
     def on_left_right_arrow_release(self):
         dcmotor1.run(Adafruit.MotorHAT, RELEASE);
         dcmotor2.run(Adafruit.MotorHAT, RELEASE);
         
     def on_triangle_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

     def on_circle_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(30, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

     def on_x_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(20, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
        
     def on_square_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(10, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
        
     
     
        
     
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()



