#include <Servo.h>

Servo servoMotor;
int ma = 2;
int mpwm = 5;
int servoPin = 14;

void setup() {
  Serial.begin(115200); // Inicializa la comunicación serial a 9600 baudios
  servoMotor.attach(servoPin);
  
  pinMode(ma, OUTPUT);
  pinMode(mpwm, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String palabra = Serial.readStringUntil('\n'); // Lee una palabra hasta que se reciba una nueva línea
    int separatorIndex = palabra.indexOf(',');
    
  if (separatorIndex != -1) {
    String servoData = palabra.substring(0, separatorIndex);
    String motorData = palabra.substring(separatorIndex + 1);
    int servoValue = servoData.toInt();
    int motorValue = motorData.toInt();
    Serial.print(servoValue);
    Serial.print("  ");
    Serial.println(motorValue);
    Direccion(servoValue);
    Motor(motorValue);
  }
 }
}

void Direccion(int servoValue) {
  servoMotor.write(servoValue);
}

void Motor(int motorValue) {
  if (motorValue < 0){
    digitalWrite(ma, LOW);
    analogWrite(mpwm, abs(motorValue));
  } else {
    digitalWrite(ma, HIGH);
    analogWrite(mpwm, motorValue);
  }
  
}