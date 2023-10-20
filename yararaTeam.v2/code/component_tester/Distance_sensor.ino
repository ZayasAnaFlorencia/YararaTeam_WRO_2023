#include <NewPing.h>

// Define los pines de los sensores de ultrasonido
//define echo and trigger pins for ultrasonic sensors
const int TRIG_PIN_1 = 12;
const int ECHO_PIN_1 = 13;
const int TRIG_PIN_2 = 8;
const int ECHO_PIN_2 = 9;

// Define los objetos de los sensores de ultrasonido
//Defines the objects instances for ultrasonic sensors
NewPing s_Izq(TRIG_PIN_1, ECHO_PIN_1, 400);  // Sensor Izquierdo
NewPing s_Der(TRIG_PIN_2, ECHO_PIN_2, 400);  // Sensor Derecho

void setup() {
  // Inicializa la comunicación serial
  //Initializes Serial comunication
  Serial.begin(9600);
}

void loop() {
  // Realizar mediciones de ultrasonido
  //Measure distances
  int dIzq = s_Izq.ping_cm();
  int dDer = s_Der.ping_cm();

  // Imprimir los resultados en una tabla mediante Serial
  //Print the results...
  Serial.print("Sensor Izquierdo: ");
  Serial.print(dIzq);
  Serial.print(" cm\t\tSensor Derecho: ");
  Serial.print(dDer);
  Serial.print(" cm");
  Serial.print(" cm\t\tdiff: ");
  Serial.print(abs(dDer-dIzq));
  Serial.println(" cm");

  delay(1000);  // Esperar 1 segundo antes de la siguiente medición
  //waits for 1 sec before next readings
}