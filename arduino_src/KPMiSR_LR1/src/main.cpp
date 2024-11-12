#include <Arduino.h>

// put function declarations here:
int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  int result = myFunction(2, 3);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, 1);
  Serial.println("Зажжен");
  delay(300);
  digitalWrite(LED_BUILTIN, 0);
  Serial.println("Погашен");
  delay(300);
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}