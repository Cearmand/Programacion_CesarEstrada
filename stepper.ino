#include <Stepper.h>//biblioteca que maneja el motor steper

const int stepsPerRevolution = 500;  // pasos por revolucion
const int pin1 = 8;  // Conecta el pin 1 a la terminal 8
const int pin2 = 9;  // Conecta el pin 1 a la terminal 9
const int pin3 = 10; // Conecta el pin 1 a la terminal 10
const int pin4 = 11; // Conecta el pin 1 a la terminal 11

Stepper myStepper(stepsPerRevolution, pin1, pin2, pin3, pin4);//crea una clase con sus parametros con el uso de la biblioteca
int speed = 60;  // Velocidad inicial en RPM

void setup() {
  Serial.begin(9600); // Inicia la comunicación serial a 9600 baudios
}

void loop() {
  if (Serial.available() > 0) {//comprueba si hay datos en el puerto serial
    char command = Serial.read();//lee los byte y lo guarda en command
    switch (command) {//ejecuta difernetes bloques del codigo dependiendo de command
      case '1':
        // Gira el motor en ambos sentidos
        Serial.println("Girando en sentido horario");
        myStepper.setSpeed(speed);
        myStepper.step(stepsPerRevolution);
        delay(1000);
        Serial.println("Girando en sentido antihorario");
        myStepper.setSpeed(speed);
        myStepper.step(-stepsPerRevolution);
        break;
      case '2':
        // Controla la velocidad
        speed = Serial.parseInt();
        Serial.print("Velocidad establecida a: ");
        Serial.println(speed);
        break;
      case '3':
        // Gira 90 grados en sentido horario (asumiendo 200 pasos por revolución)
        Serial.println("Girando 90 grados en sentido horario");
        myStepper.setSpeed(speed);
        myStepper.step(stepsPerRevolution / 4);
        break;
    }
  }
}
