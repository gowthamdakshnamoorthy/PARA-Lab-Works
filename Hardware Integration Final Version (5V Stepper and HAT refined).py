import RPi.GPIO as GPIO
import board
from event_mapping.Mapping3Bh2b import Mapping3Bh2b
from controller import *
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

#Object created with respect to the bottom and top HAT
dcmotor_actuator = MotorKit()
steppers = MotorKit(address=0x61)

class MyController(Controller):
    
     def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

     def on_L1_press(self):
         dcmotor_actuator.motor1.throttle = 0.5
         dcmotor_actuator.motor1.decay_mode = 1
         dcmotor_actuator.motor2.throttle = 0.5
         dcmotor_actuator.motor2.decay_mode = 1

     def on_L1_release(self):
         dcmotor_actuator.motor1.throttle = 0
         dcmotor_actuator.motor2.throttle = 0

         
     def on_R1_press(self):
         dcmotor_actuator.motor1.throttle = -0.5
         dcmotor_actuator.motor1.decay_mode = 1
         dcmotor_actuator.motor2.throttle = -0.5
         dcmotor_actuator.motor2.decay_mode = 1

     def on_R1_release(self):
         dcmotor_actuator.motor1.throttle = 0
         dcmotor_actuator.motor2.throttle = 0
         

     def on_left_arrow_press(self):
         dcmotor_actuator.motor3.throttle = 1
         dcmotor_actuator.motor3.decay_mode = 0
         dcmotor_actuator.motor4.throttle = 1
         dcmotor_actuator.motor4.decay_mode = 0

     def on_right_arrow_press(self):
         dcmotor_actuator.motor3.throttle = -1
         dcmotor_actuator.motor3.decay_mode = 0
         dcmotor_actuator.motor4.throttle = -1
         dcmotor_actuator.motor4.decay_mode = 0
     
     def on_left_right_arrow_release(self):
         dcmotor_actuator.motor3.throttle = 0
         dcmotor_actuator.motor4.throttle = 0

    
     def on_triangle_press(self):
         steppers.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)

     def on_circle_press(self):
         steppers.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

     def on_x_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(20, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
        
     def on_square_press(self):
         steppermotor1.setSpeed(100)
         steppermotor1.step(10, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

     
     
       
     
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()