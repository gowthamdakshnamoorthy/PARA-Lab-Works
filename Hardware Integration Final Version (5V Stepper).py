import RPi.GPIO as GPIO
from event_mapping.Mapping3Bh2b import Mapping3Bh2b
from controller import *
from time import sleep
import serial
import time
global x
x = 0;
#Defining ports from Raspberry Pi to L298N Motor Driver for actuators
inp1 = 38  
inp2 = 40
en1 = 36
inp3 = 16
inp4 = 18
en2 = 22
sda = 3
sdl = 5
#Defining ports  from Raspberry Pi to DRV8834 Motor Driver
m0 = 29
m1 = 31
stp = 35
direction = 37  

'''
#Defining ports from Raspberry Pi to L298N Motor Driver for Motors
inp1dash = 28
inp2dash = 32
en1dash = 34
inp3dash = 36
inp4dash = 38
en2dash = 40
''' 

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
GPIO.setup(m0, GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(stp, GPIO.OUT)
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(sda, GPIO.IN)
GPIO.setup(sdl, GPIO.IN)

#Setting the initial values of the inputs as zero for actuators
GPIO.output(inp1, False)
GPIO.output(inp2, False)
GPIO.output(en1, False)
GPIO.output(inp3, False)
GPIO.output(inp4, False)
GPIO.output(en2, False)
'''
#Setting the initial values of the inputs as zero for motors
GPIO.output(inp1dash, False)
GPIO.output(inp2dash, False)
GPIO.output(en1dash, False)
GPIO.output(inp3dash, False)
GPIO.output(inp4dash, False)
GPIO.output(en2dash, False)
''' 
#Setting the initial values of the inputs for NEMA-17 stepper motor
GPIO.output(m0, False)
GPIO.output(m1, False)


#Setting the step value as zero and direction as clockwise
GPIO.output(stp, False)
GPIO.output(direction, True)


def recv_msg():
        ser.reset_input_buffer()
        start_time = time.time()
        i = 0
        while i < 10:
                if ser.in_waiting > 0:
                        print(ser.in_waiting)
                        line = ser.readline().decode('utf-8').rstrip()
                        print("Arduino: ", line)
                        i = i + 1
                        

def functionality_check(a, b, c, d, e, f):
        Tuple_1 = (GPIO.input(a), GPIO.input(b), GPIO.input(c), GPIO.input(d), GPIO.input(e), GPIO.input(f));
        return Tuple_1

class MyController(Controller):
    
     def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
     
     def on_L1_press(self):
        #When moved backward
        pwm1 = GPIO.PWM(36, 30)
        pwm1.start(100)
        pwm1.ChangeDutyCycle(100)
        pwm2 = GPIO.PWM(22, 30)
        pwm2.start(100)
        pwm2.ChangeDutyCycle(100)  
        for a in range(10):
                GPIO.output(inp1, False)
                GPIO.output(inp2, False)
                GPIO.output(en1, True)
                GPIO.output(inp3, False)
                GPIO.output(inp4, True)
                GPIO.output(en2, True)
                print("Backward")
        bb = functionality_check(inp1, inp2, en1, inp3, inp4, en2);
        print(bb)
        if bb == (0,1,1,0,1,1):
                print("L1 configuration is good")
        else:
                print("Configuration is not good")


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
        aa = functionality_check(inp1, inp2, en1, inp3, inp4, en2);
        print(aa)
        if aa == (1,0,1,1,0,1):
                print("R1 configuration is good")
        else:
                print("Configuration is not good")


     def on_R1_release(self):
                GPIO.output(en1, False)
                GPIO.output(en2, False)
     
     '''
     def on_left_arrow_press(self):
        ser=serial.Serial('/dev/ttyACM0', 9600)
        ser.write(b"left_press\n")
        recv_msg()

                
     def on_right_arrow_press(self):
        ser=serial.Serial('/dev/ttyACM0', 9600)
        ser.write(b"right_press\n")
        recv_msg()
     
     def on_left_right_arrow_release(self):
         ser=serial.Serial('/dev/ttyACM0', 9600)
         ser.write(b"release\n")
         recv_msg()             
     
         
      
     def on_right_arrow_release(self):
         ser=serial.Serial('/dev/ttyACM0', 9600)
         ser.write(b"release\n")
         recv_msg()
     '''     
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
