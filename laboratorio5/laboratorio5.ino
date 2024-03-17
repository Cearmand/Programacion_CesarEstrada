void setup() {
  //Estos son los pines que utilizaremos en la placa de arduino
pinMode(3,OUTPUT);
pinMode(5,OUTPUT);
pinMode(8,OUTPUT);
Serial.begin(9600);//Se inicializa la comunicación serial 
}

void loop() {
  // Se crea el codigo para encender los leds
if(Serial.available()>0){//Verifica si hay datos disponibles en el puerto serial
  int estadoMonitor = Serial.read();//Indica el estado deseado para los leds
  if(estadoMonitor=='1'){//Verifica si el estado es 1, enciende todos los leds
    digitalWrite(3,HIGH);
    Serial.println("Led encendidio azul");

    digitalWrite(5,HIGH);
    Serial.println("Led encendidio verde");

    digitalWrite(8,HIGH);
    Serial.println("Led encendidio rojo");

  }else if(estadoMonitor=='0'){//si el estado es 0, se apagan todos los leds
    digitalWrite(3,LOW);
    Serial.println("Led apagado");

    digitalWrite(5,LOW);
    Serial.println("Led encendidio");

    digitalWrite(8,LOW);
    Serial.println("Led encendidio");
  }
}
}
