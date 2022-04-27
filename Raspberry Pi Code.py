import RPi.GPIO as GPIO
from pyPS4Controller.controller import Controller
from time import sleep
#Defining ports from Raspberry Pi to L298N Motor Driver
inp1 = 11  
inp2 = 13
en1 = 15
inp3 = 16
inp4 = 18
en2 = 22
ms1 = 29
ms2 = 31
ms3 = 33
stp = 35
direction = 37

#Setting the numbering system for pins as Board format
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 

#Setting up the pin types as output
GPIO.setup(inp1, GPIO.OUT)
GPIO.setup(inp2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(inp3, GPIO.OUT)
GPIO.setup(inp4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(ms1, GPIO.OUT)
GPIO.setup(ms2, GPIO.OUT)
GPIO.setup(ms3, GPIO.OUT)
GPIO.setup(stp, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)

#Setting the initial values of the inputs as zero for actuators
GPIO.output(inp1, False)
GPIO.output(inp2, False)
GPIO.output(en1, False)
GPIO.output(inp3, False)
GPIO.output(inp4, False)
GPIO.output(en2, False)
#Setting the initial values of the inputs for NEMA-17 stepper motor

#Setting the step value as zero and direction as clockwise
GPIO.output(stp, False)
GPIO.output(direction, True)

class MyController(Controller):
    
     def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
     
     def on_L1_press(self):
        #When moved backward
        for a in range(10):
                GPIO.output(inp1, False)
                GPIO.output(inp2, True)
                GPIO.output(en1, True)
                GPIO.output(inp3, False)
                GPIO.output(inp4, True)
                GPIO.output(en2, True)
                print("Backward")

     def on_L1_release(self):
                GPIO.output(en1, False)
                GPIO.output(en2, False)
                
     def on_R1_press(self):
        
        #When moved forward
        for b in range(10):
                GPIO.output(inp1, True)
                GPIO.output(inp2, False)
                GPIO.output(en1, True)
                GPIO.output(inp3, True)
                GPIO.output(inp4, False)
                GPIO.output(en2, True)
                print("Forward")

     def on_R1_release(self):
                GPIO.output(en1, False)
                GPIO.output(en2, False)
                        
     def on_triangle_press(self):
        #When stepped to 1/2 of its resolution
        for k in range(500):
                GPIO.output(ms1, True)
                GPIO.output(ms2, False)
                GPIO.output(ms3, False)
                print("Step resolution - 0.5")

     def on_triangle_release(self):
        GPIO.output(ms1, False)
        GPIO.output(ms2, False)
        GPIO.output(ms3, False)

     def on_circle_press(self):
        #When stepped to 1/4 of its resolution
        GPIO.output(ms1, False)
        GPIO.output(ms2, True)
        GPIO.output(ms3, False)
        print("Step resolution - 0.25") 

     def on_circle_release(self):
        GPIO.output(ms1, False)
        GPIO.output(ms2, False)
        GPIO.output(ms3, False)
        
     def on_x_press(self):
        #When stepped to 1/8 of its resolution
        GPIO.output(ms1, True)
        GPIO.output(ms2, True)
        GPIO.output(ms3, False)
        print("Step resolution - 0.125")
        
     def on_x_release(self):
        GPIO.output(ms1, False)
        GPIO.output(ms2, False)
        GPIO.output(ms3, False)
        
     def on_square_press(self):
        #When stepped to 1/16 of its resolution
        GPIO.output(ms1, True)
        GPIO.output(ms2, True)
        GPIO.output(ms3, True)
        print("Step resolution - 0.0625") 
        
     def on_square_release(self):
        GPIO.output(ms1, False)
        GPIO.output(ms2, False)
        GPIO.output(ms3, False)
        
     def on_up_arrow_press(self):
        #When clockwise rotation is being selected
        for i in range(500):
                GPIO.output(direction, GPIO.LOW)
                GPIO.output(stp, GPIO.HIGH)
                sleep(0.0001)
                GPIO.output(stp, GPIO.LOW)
                sleep(0.0001)
                print("Clockwise")
     
    
                
     def on_down_arrow_press(self):
         #When anticlockwise rotation is being selected
         for j in range(500):
                 GPIO.output(direction, False)
                 GPIO.output(stp, True)
                 sleep(0.0001)
                 GPIO.output(stp, False)
                 sleep(0.0001)
                 print("Anticlockwise")
     
     
         
      

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
