#include <Arduino.h>
#include <Servo.h>
#include <Stepper.h>

#define RED_PIN 2
#define GREEN_PIN 13
#define BLUE_PIN 7

#define START 1
#define END 0

// servo
Servo myServo;
int servoPin = 6;

// stepper
const int stepsPerRevolution = 360;
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

// DPT
#define PIN_ENA 3
#define PIN_IN1 4
#define PIN_IN2 5
int power = 0;

void setup() {
  // pinMode(LED_BUILTIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  pinMode(PIN_ENA, OUTPUT);
  pinMode(PIN_IN1, OUTPUT);
  pinMode(PIN_IN2, OUTPUT);
  digitalWrite(PIN_IN1, LOW);
  digitalWrite(PIN_IN2, LOW);

  pinMode(START, INPUT);
  pinMode(END, INPUT);

  myServo.attach(servoPin);
  myStepper.setSpeed(30);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readString();
    int spaceIndex = input.indexOf(' ');
    String command = input.substring(0, spaceIndex);
    if (command == "SetLed") {
      // Serial.println("Светодиод");
      // digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      String buff = input.substring(spaceIndex+1, input.length());
      Serial.println(buff);
      
      spaceIndex = buff.indexOf(' ');
      String color = buff.substring(0, spaceIndex);
      int state = buff.substring(spaceIndex+1, buff.length()).toInt();

      if (color == "red") {
        digitalWrite(RED_PIN, state);
      } else if (color == "green") {
        digitalWrite(GREEN_PIN, state);
      } else if (color == "blue") {
        digitalWrite(BLUE_PIN, state);
      }
    } else if (command == "Test") {
      Serial.println("Test 2\0");
    } else if (command == "ServoSet") {
      int angle = input.substring(spaceIndex+1, input.length()).toInt();
      myServo.write(angle);
    } else if (command == "StepperSet") {
      int steps = input.substring(spaceIndex+1, input.length()).toInt();
      Serial.print("steps ");
      Serial.println(steps);
      myStepper.step(steps);
    } else if (command == "DPTSet") {
      // if ((digitalRead(START) == LOW) || (digitalRead(END) == LOW)) {
      //   power = 0;
      //   Serial.println("datchik");
      // } else {
        power = input.substring(spaceIndex+1, input.length()).toInt();
        Serial.print("speed ");
        Serial.println(power);
        if (power < 0) {
          digitalWrite(PIN_IN1, LOW);
          digitalWrite(PIN_IN2, HIGH);
        } else {
          digitalWrite(PIN_IN1, HIGH);
          digitalWrite(PIN_IN2, LOW);
        }
        analogWrite(PIN_ENA, abs(power));
      // }
    }
  }
  // if ((digitalRead(START) == LOW) || (digitalRead(END) == LOW)) {
  //   power = 0;
  //   analogWrite(PIN_ENA, abs(power));
  //   Serial.println("Drop");
  // }
}
