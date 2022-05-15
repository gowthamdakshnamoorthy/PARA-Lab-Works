import RPi.GPIO as GPIO
from pyPS4Controller.controller import Controller
from time import sleep
#Defining ports from Raspberry Pi to L298N Motor Driver for actuators
inp1 = 11  
inp2 = 13
en1 = 15
inp3 = 16
inp4 = 18
en2 = 22


#Defining ports from Raspberry Pi to L298N Motor Driver for Motors
inp1dash = 29
inp2dash = 31
en1dash = 33
inp3dash = 36
inp4dash = 37
en2dash = 35
 

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
GPIO.setup(inp1dash, GPIO.OUT)
GPIO.setup(inp2dash, GPIO.OUT)
GPIO.setup(en1dash, GPIO.OUT)
GPIO.setup(inp3dash, GPIO.OUT)
GPIO.setup(inp4dash, GPIO.OUT)
GPIO.setup(en2dash, GPIO.OUT)

#Setting the initial values of the inputs as zero for actuators
GPIO.output(inp1, False)
GPIO.output(inp2, False)
GPIO.output(en1, False)
GPIO.output(inp3, False)
GPIO.output(inp4, False)
GPIO.output(en2, False)

#Setting the initial values of the inputs as zero for motors
GPIO.output(inp1dash, False)
GPIO.output(inp2dash, False)
GPIO.output(en1dash, False)
GPIO.output(inp3dash, False)
GPIO.output(inp4dash, False)
GPIO.output(en2dash, False)


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
     
     def on_left_arrow_press(self):
        #When moved backward
        #The speed of the motor could be varied by the pwm signal
        pwm1 = GPIO.PWM(33, 20)
        pwm1.start(100)
        pwm1.ChangeDutyCycle(99)
        pwm2 = GPIO.PWM(35, 20)
        pwm2.start(100)
        pwm2.ChangeDutyCycle(99)
        for c in range(10):
                GPIO.output(inp1dash, False)
                GPIO.output(inp2dash, True)
                GPIO.output(en1dash, True)
                GPIO.output(inp3dash, True)
                GPIO.output(inp4dash, False)
                GPIO.output(en2dash, True)
                print("Forward")

     def on_left_arrow_release(self):
                GPIO.output(en1dash, False)
                GPIO.output(en2dash, False)
                
     def on_right_arrow_press(self):
        
        #When moved forward
        #The speed of the motor could be varied by the pwm signal
        pwm1 = GPIO.PWM(33, 20)
        pwm1.start(100)
        pwm1.ChangeDutyCycle(99)
        pwm2 = GPIO.PWM(35, 20)
        pwm2.start(100)
        pwm2.ChangeDutyCycle(99)
        for d in range(10):
                GPIO.output(inp1dash, True)
                GPIO.output(inp2dash, False)
                GPIO.output(en1dash, True)
                GPIO.output(inp3dash, False)
                GPIO.output(inp4dash, True)
                GPIO.output(en2dash, True)
                print("Forward")

     def on_right_arrow_release(self):
                GPIO.output(en1dash, False)
                GPIO.output(en2dash, False)  
                       

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
