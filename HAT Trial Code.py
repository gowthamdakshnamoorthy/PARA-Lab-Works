import RPi.GPIO as GPIO
from event_mapping.Mapping3Bh2b import Mapping3Bh2b
from controller import *
from time import sleep
import serial
import time
import board
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

#Object created with respect to the bottom HAT
actuator/dcmotor_main = Adafruit_MotorHAT(addr=0x60)
steppermotor_main = Adafruit_MotorHAT(addr=0x61)

#Instances created for acccessing individual DC motors
actuator1 = actuator/dcmotor_main.getMotor(1)
actuator2 = actuator/dcmotor_main.getMotor(2)
dcmotor1 = actuator/dcmotor_main.getMotor(3)
dcmotor2 = actuator/dcmotor_main.getMotor(4)

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

     def on_right_arrow_release(self):
         ser=serial.Serial('/dev/ttyACM0', 9600)
         ser.write(b"release\n")
         recv_msg()
         
     def on_triangle_press(self):
        #When stepped to 1/4 of its resolution
        GPIO.output(m1, False)
        print("Step resolution - 0.25")


     def on_circle_press(self):
        #When stepped to 1/8 of its resolution
        GPIO.output(m0, False)
        GPIO.output(m1, True)
        print("Step resolution - 0.125")
        ''' 
        ser=serial.Serial('/dev/ttyUSB0', 9600)
        ser.write(b"left_press\n")
        recv_msg()
'''

  
        
     def on_x_press(self):
        #When stepped to 1/16 of its resolution
        GPIO.output(m0, True)
        GPIO.output(m1, True)
        print("Step resolution - 0.0625")
        
    
        
     def on_square_press(self):
        #When stepped to 1/32 of its resolution
        GPIO.output(m1, True)
        print("Step resolution - 0.03125") 
        
     
     
        
     def on_up_arrow_press(self):
        #When clockwise rotation is being selected
        for j in range(8):
                GPIO.output(direction, GPIO.HIGH)
                GPIO.output(stp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(stp, GPIO.LOW)
                sleep(0.0001)
                # print("Clockwise")
                '''
        ser =serial.Serial('/dev/ttyACM0', 9600)
        #recv_msg()
    '''
                
     def on_down_arrow_press(self):
         #When anticlockwise rotation is being ed
         for j in range(8):
                 GPIO.output(direction, GPIO.LOW)
                 GPIO.output(stp, GPIO.HIGH)
                 sleep(0.0001)
                 GPIO.output(stp, GPIO.LOW)
                 sleep(0.0001)
                 # print("Anticlockwise")
         # ser =serial.Serial('/dev/ttyACM0', 9600)
         # recv_msg()
                 

     def on_up_down_arrow_release(self):
        GPIO.output(direction, GPIO.LOW)
        GPIO.output(stp, GPIO.LOW)
    
     def on_share_press(self):
        '''
        def read_events():
            try:
                return _file.read(self.event_size)
            except IOError:
                print("Interface lost. Device disconnected?")
                on_disconnect_callback()
                exit(1)

        def check_for(sub, full, start_index):
            return [start for start in range(start_index, len(full) - len(sub) + 1) if
                    sub == full[start:start + len(sub)]]

        def unpack():
            __event = struct.unpack(self.event_format, event)
            return (__event[3:], __event[2], __event[1], __event[0])
        print(self.current_value)
        
        #while True:

        _file = open(self.interface, "rb")
        event = read_events()
        (overflow, value, button_type, self.button_id) = unpack()
        print(overflow, value, button_type, self.button_id)
        '''
        GPIO.output(ms1, True)
        GPIO.output(ms2, True)
        GPIO.output(ms3, True)
        GPIO.output(direction, GPIO.LOW)
        GPIO.output(stp, GPIO.HIGH)
        sleep(0.01)
        GPIO.output(stp, GPIO.LOW)
        sleep(0.01)
        # if x == 1:
                # break

'''
        on_options_press()
                
     
     def on_options_press(self):
             print("Hi");
             # x = x+1;
      '''
                


      
        
                
     
             

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
#(on_sequence = [{"inputs": ['down','options'],
   #                               "callback": controller.on_options_press}])



