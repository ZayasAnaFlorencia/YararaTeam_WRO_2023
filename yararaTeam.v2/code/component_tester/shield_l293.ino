#define PWMB 5
#define DB 2

void setup() {
  pinMode(PWMB, OUTPUT);
  pinMode(DB, OUTPUT);
}

void loop() {
  digitalWrite(DB, LOW); // set direction to forward
  analogWrite(PWMB, 255); // set speed to maximum
  delay(1000); // wait for 1 second
  analogWrite(PWMB, 0); // set speed to 0
  delay(1000); // wait for 1 second
  digitalWrite(DB, HIGH); // set direction to backward
  analogWrite(PWMB, 255); // set speed to maximum
  delay(1000); // wait for 1 second
  analogWrite(PWMB, 0); // set speed to 0
  delay(1000); // wait for 1 second
}