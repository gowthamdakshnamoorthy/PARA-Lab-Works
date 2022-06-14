//Code by Gowtham Dakshnamoorthy
//ASU ID: 1222598585
int m0 = 29;
int m1 = 31; 
int stp = 33;
int dir = 35;


void setup() 
{
 Serial.begin(9600);
 pinMode(m0, OUTPUT);
 pinMode(m1, OUTPUT);
 pinMode(stp, OUTPUT);
 pinMode(dir, OUTPUT);
 //Setting step value as zero and the directiom of rotation as clockwise
 digitalWrite(stp, LOW);
 digitalWrite(dir,HIGH);
}
void loop()
{
for(int i=0; i<100; i++)
{
 //digitalWrite(m0, LOW);
  digitalWrite(m1, HIGH);
  digitalWrite(stp,HIGH);
  delayMicroseconds(100000000000);
  digitalWrite(stp,LOW);
  digitalWrite(dir, HIGH);
  }
}
