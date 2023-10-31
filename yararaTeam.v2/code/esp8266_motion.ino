#include <Servo.h>

Servo servoMotor;
int ma = 1;
int mpwm = 3;
int servoPin = 5;

void setup() {
  Serial.begin(115200);
  servoMotor.attach(servoPin);

  pinMode(ma, OUTPUT);
  pinMode(mb, OUTPUT);
  pinMode(mpwm, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    int separatorIndex = data.indexOf(',');
    if (separatorIndex != -1) {
      String servoData = data.substring(0, separatorIndex);
      String motorData = data.substring(separatorIndex + 1);


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

  digitalWrite(ma, HIGH);
  analogWrite(mpwm, motorValue);
}