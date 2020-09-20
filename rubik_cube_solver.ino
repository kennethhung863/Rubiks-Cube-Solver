// Arduino code: takes serial input and executes servo commands accordingly

#include <Servo.h> 

const int rotatingServoPin = 9;
const int pushServoPin = 6;
const int holdServoPin = 4;
int inByte;


Servo rotatingServo;
Servo pushServo;
Servo holdServo;

void rotateServo(int num, Servo servo){
  servo.write(num); 
  delay(1000);
}
void rotateServoLessDelay(int num, Servo servo){
  servo.write(num); 
  delay(100);
}

void setup() {
  Serial.begin(115200);
  rotatingServo.attach(rotatingServoPin); 
  pushServo.attach(pushServoPin); 
  holdServo.attach(holdServoPin); 
  rotateServo(133, pushServo);
  rotateServo(92, rotatingServo);
  rotateServo(44, holdServo);

}

void loop() {

  if (Serial.available() > 0) {
    inByte = Serial.read();
    
    if (inByte == '0') {
      rotateServo(10, rotatingServo);
      Serial.write("0");
    }
    else if (inByte == '1') {
      rotateServo(92, rotatingServo);
      Serial.write("1");
    }
    else if (inByte == '2') {
      rotateServo(178, rotatingServo);
      Serial.write("2");
    }
    else if (inByte == '3') {
      rotateServoLessDelay(95, pushServo);
      rotateServoLessDelay(44, pushServo);
      rotateServo(46, pushServo);
      rotateServo(133, pushServo);
      Serial.write("3");
    }
    else if (inByte == '4') {
      rotateServo(103, holdServo);
      Serial.write("4");
    }
    else if (inByte == '5') {
      rotateServo(44, holdServo);
      Serial.write("5");
    }
    // rotate 2 -> 3
    else if (inByte == '6') {
      rotateServo(103, holdServo);      
      rotateServo(179, rotatingServo);
      rotateServo(44, holdServo);
      Serial.write("6");
    }
    // rotate 2 -> 1
    else if (inByte == '7') {
      rotateServo(103, holdServo);   
      rotateServo(5, rotatingServo);      
      rotateServo(44, holdServo);
      Serial.write("7");
    }
    
    

  }
}
