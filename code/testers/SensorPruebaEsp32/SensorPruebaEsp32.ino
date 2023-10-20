  #include <NewPing.h>

#define TRIGGER_PIN_1 12
#define ECHO_PIN_1 13
#define TRIGGER_PIN_2 14
#define ECHO_PIN_2 15

NewPing sonar1(TRIGGER_PIN_1, ECHO_PIN_1);
NewPing sonar2(TRIGGER_PIN_2, ECHO_PIN_2);

volatile unsigned long startTime1 = 0;
volatile unsigned long endTime1 = 0;
volatile bool echoPinState1 = false;

volatile unsigned long startTime2 = 0;
volatile unsigned long endTime2 = 0;
volatile bool echoPinState2 = false;

void setup() {
  Serial.begin(115200);
  
  pinMode(ECHO_PIN_1, INPUT);
  pinMode(ECHO_PIN_2, INPUT);
  
  attachInterrupt(digitalPinToInterrupt(ECHO_PIN_1), echoInterrupt1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(ECHO_PIN_2), echoInterrupt2, CHANGE);
}

void loop() {
  unsigned long distance1;
  unsigned long distance2;

  noInterrupts(); // Desactivar interrupciones para evitar cambios durante las mediciones
  distance1 = sonar1.ping_cm();
  distance2 = sonar2.ping_cm();
  interrupts(); // Reactivar interrupciones

  Serial.print("Distancia Sensor 1: ");
  Serial.print(distance1);
  Serial.print(" cm, Sensor 2: ");
  Serial.print(distance2);
  Serial.println(" cm");

  delay(500);
}

void echoInterrupt1() {
  if (digitalRead(ECHO_PIN_1) == HIGH) {
    startTime1 = micros();
  } else {
    endTime1 = micros();
  }
}

void echoInterrupt2() {
  if (digitalRead(ECHO_PIN_2) == HIGH) {
    startTime2 = micros();
  } else {
    endTime2 = micros();
  }
}
