#include <Servo.h>

Servo srv;
int pos;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  srv.attach(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()){
      pos = Serial.parseInt();
      srv.write(pos);
      Serial.print("Açı:");
      Serial.println(pos);
  }
}
