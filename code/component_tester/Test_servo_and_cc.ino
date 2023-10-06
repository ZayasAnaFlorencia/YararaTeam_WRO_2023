#include <Servo.h>
const int motor1 = 7;
const int motor2 = 5;
const int pwm = 6;

// Definir pines para el servo SG90
const int pinServo = 11;
Servo servo;
void setup() {
  Serial.begin(9600);
  pinMode(motor1,OUTPUT);
  pinMode(motor2,OUTPUT);
  pinMode(pwm,OUTPUT);
  servo.attach(pinServo);
}

void loop() {
if(Serial.available()>0){
  //it reads until detects "newline"
  String input = Serial.readStringUntil('\n'); 
  // Lee una línea completa desde la comunicación serial
  if(input == "a"){
    Serial.println("avanzanding");
    servo.write(180);
    avanzar(255);
    
    detener();
  }else{
    int pos = input.toInt();
    Serial.println(pos);
    servo.write(pos);
    }
  }
}

void avanzar(int pot) {
  analogWrite(pwm,pot);
  digitalWrite(motor1,HIGH);  
  digitalWrite(motor2,LOW);
  delay(3000);
}
void detener() {
  digitalWrite(motor1,LOW);  
  digitalWrite(motor2,LOW);  
}