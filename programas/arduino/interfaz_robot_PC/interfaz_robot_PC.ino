#include <Servo.h>

Servo eje1;  // crea el objeto servo
Servo eje2;  // crea el objeto servo
Servo eje3;  // crea el objeto servo
Servo eje4;  // crea el objeto servo

int pwm1 = 2;        // uso la pata D2 para enviar el PWM al servo 1
int pwm2 = 3;        // uso la pata D3 para enviar el PWM al servo 2
int pwm3 = 4;        // uso la pata D4 para enviar el PWM al servo 3
int pwm4 = 5;        // uso la pata D5 para enviar el PWM al servo 4

const int pinLED = 13;
int Q[] = {90,90,90,90,0};

const byte buffSize = 40;
char inputBuffer[buffSize];
const char startMarker = '<';
const char endMarker = '>';
byte bytesRecvd = 0;
boolean readInProgress = false;
boolean newDataFromPC = false;

float inicio =0;
float fin = 0;

void setup(){
  eje1.attach(pwm1);  // vinculo los servos
  eje2.attach(pwm2);
  eje3.attach(pwm3);
  eje4.attach(pwm4);
   
  Serial.begin(115200);
  
  pinMode(pinLED, OUTPUT);
  }

void loop(){
  inicio=millis();                              // establesco un Ts de 10ms
  fin= inicio+1;

  Serial.write(".");
  
  if (Serial.available()>0) 
  {
    digitalWrite(pinLED, HIGH);
    SerialEvent();
    digitalWrite(pinLED, LOW);
    // actualizo los servos 
  }
  eje1.write(Q[1]); 
  eje2.write(Q[2]); 
  eje3.write(Q[3]); 
  eje4.write(Q[4]);
  while (fin > millis())  {}
}
