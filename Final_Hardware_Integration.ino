//Code by Gowtham Dakshnamoorthy
//ASU ID: 1222598585
#include<PS2X_lib.h>
//Defining the ports from Arduino board to L298N Motor Driver
int speed_A1 = 7;
int speed_A2 = 2; 
int input1_A1 = 6;
int input2_A1 = 5;
int input1_A2 = 4;
int input2_A2 = 3;
int ms1 = 46;
int ms2 = 48; 
int ms3 = 50;
int stp = 44;
int dir = 42;
int mot1int1 = 40;
int mot1int2 = 38;
int mot2int1 = 36;
int mot2int2 = 34; 
//Defining the ports from Arduino board to PS2 Wireless Controller
#define PS2_Data 12
#define PS2_Command 11
#define PS2_Attention 10
#define PS2_Clock 9
int Pressure = 0;
int Rumble = 0;
PS2X ps2x; //Creating a class for PS2 Controller
int error=0;
int type=0;


void setup() {
 Serial.begin(9600);
 pinMode(speed_A1, OUTPUT);
 pinMode(speed_A2, OUTPUT);
 pinMode(input1_A1, OUTPUT);
 pinMode(input2_A1, OUTPUT);
 pinMode(input1_A2, OUTPUT);
 pinMode(input2_A2, OUTPUT);
 pinMode(ms1, OUTPUT);
 pinMode(ms2, OUTPUT);
 pinMode(ms3, OUTPUT);
 pinMode(stp, OUTPUT);
 pinMode(dir, OUTPUT);
 //Setting the initial speed values for the actuators as zero
 analogWrite(speed_A1, 0);
 analogWrite(speed_A2, 0);
 //Setting step value as zero and the directiom of rotation as clockwise
 digitalWrite(stp, LOW);
 digitalWrite(dir,HIGH);
 //Setting the  stepper motor to full stepping at the start condition
 digitalWrite(ms1, LOW);
 digitalWrite(ms2, LOW);
 digitalWrite(ms3, LOW);
 //Setting the motor to be stationary 
 digitalWrite(mot1int1, LOW);
 digitalWrite(mot1int2, LOW);
 digitalWrite(mot2int1, LOW);
 digitalWrite(mot2int2, LOW);
 
  error = ps2x.config_gamepad(PS2_Clock, PS2_Command, PS2_Attention, PS2_Data, Pressure, Rumble); // Linking the Arduino Pins with the L298N Motor Driver
 if (error==0)
 {
  Serial.println("Controller Found");
 }
 else
 {
  Serial.println("Controller Not found, check connections");
 }
 type = ps2x.readType();
 if (type==1)
 {
  Serial.println("Dualshock Controller is found");
 }
 else
 {
  Serial.println("Dualshock Controller not found");
 }
}

void loop() {
if(type==1)
{
 ps2x.read_gamepad();
 if(ps2x.Button(PSB_R1)) //Inputs for the pin when the R1 button is being pressed
 {
  digitalWrite(input1_A1, HIGH);
  digitalWrite(input2_A1, LOW);
  digitalWrite(input1_A2, HIGH);
  digitalWrite(input2_A2, LOW);
  analogWrite(speed_A1, 123); //Half of the motor speed is being considered
  analogWrite(speed_A2, 123);
  Serial.println("The actuator is being extended");
 }
 else if(ps2x.Button(PSB_R2)) //Inputs for the pin when the R2 button is pressed
 {
  digitalWrite(input1_A1, LOW);
  digitalWrite(input2_A1, HIGH);
  digitalWrite(input1_A2, LOW);
  digitalWrite(input2_A2, HIGH);
  analogWrite(speed_A1, 123); //Half of the motor speed is being considered
  analogWrite(speed_A2, 123);
  Serial.println("The actuator is being retracted");
 }
 else
 {
  digitalWrite(input1_A1, LOW);
  digitalWrite(input2_A1, LOW);
  digitalWrite(input1_A2, LOW);
  digitalWrite(input2_A2, LOW);
  analogWrite(speed_A1, 0); //Half of the motor speed is being considered
  analogWrite(speed_A2, 0);
  
 }

}
else{
return;
}
if(type==1)
{
 ps2x.read_gamepad();
 if(ps2x.Button(PSB_GREEN)) //Inputs for the pin when the Triangle button is pressed 
 {
  digitalWrite(ms1, HIGH);
  digitalWrite(ms2, LOW);
  digitalWrite(ms3, LOW);
  Serial.println("The motor is microstepped to 1/2 of its resolution");
 }
 else if(ps2x.Button(PSB_RED)) //Inputs for the pin when the Circle button is pressed 
 {
  digitalWrite(ms1, LOW);
  digitalWrite(ms2, HIGH);
  digitalWrite(ms3, LOW);
  Serial.println("The motor is microstepped to 1/4 of its resolution");
 }
 else if(ps2x.Button(PSB_BLUE)) //Inputs for the pin when the X button is pressed
 {
  digitalWrite(ms1, HIGH);
  digitalWrite(ms2, HIGH);
  digitalWrite(ms3, LOW);
  Serial.println("The motor is microstepped to 1/8 of its resolution");
 }
 else if(ps2x.Button(PSB_PINK)) //Inputs for the pin when the Square button is pressed
 {
  digitalWrite(ms1, HIGH);
  digitalWrite(ms2, HIGH);
  digitalWrite(ms3, HIGH);
  Serial.println("The motor is microstepped to 1/16 of its resolution");
 }
else
{
  digitalWrite(ms1, LOW);
  digitalWrite(ms2, LOW);
  digitalWrite(ms3, LOW);
}
}
else{
return;
}
if(type==1)
{
 ps2x.read_gamepad();
if(ps2x.Button(PSB_L1))
{
  digitalWrite(dir,HIGH);
  digitalWrite(stp,HIGH);
  delayMicroseconds(10);
  digitalWrite(stp,LOW);
  Serial.println("The motor is rotated clockwise");
  
}
else if(ps2x.Button(PSB_L2))
{
  digitalWrite(dir,LOW);
  digitalWrite(stp,HIGH);
  delayMicroseconds(10);
  digitalWrite(stp,LOW);
  Serial.println("The motor is rotated anticlockwise");
}
else{
  return;
}
}
else{
  return;
}
if(type==1)
{
 ps2x.read_gamepad();
 if(ps2x.Button(PSB_PAD_UP)) //Inputs for the pin when the R1 button is being pressed
 {
  digitalWrite(mot1int1, LOW);
  digitalWrite(mot1int2, HIGH);
  digitalWrite(mot2int1, HIGH);
  digitalWrite(mot2int2, LOW);
  Serial.println("The robot is moved forward");
 }
 else if(ps2x.Button(PSB_PAD_DOWN)) //Inputs for the pin when the R2 button is pressed
 {
  digitalWrite(mot1int1, HIGH);
  digitalWrite(mot1int2, LOW);
  digitalWrite(mot2int1, LOW);
  digitalWrite(mot2int2, HIGH);
  Serial.println("The robot is moved backward");
 }
 else
 {
  digitalWrite(mot1int1, LOW);
  digitalWrite(mot1int2, LOW);
  digitalWrite(mot2int1, LOW);
  digitalWrite(mot2int2, LOW);
  }

}
else{
return;
}
}
