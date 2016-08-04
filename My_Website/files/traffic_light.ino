/*
Computer Science 4.4 Arduino: Push Buttons 
*/
int redPin = 2;
int yellowPin = 3;
int greenPin = 4;
int button = 5; // switch is on pin 5
int buttonValue = 0; // switch defaults to 0 or LOW
int yellowFlashRate = 500;
int yellowFlashTimes = 10;
int redDelay = 5000;

void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(yellowPin, OUTPUT); 
  pinMode(greenPin, OUTPUT); 
  pinMode(button, INPUT_PULLUP);
  digitalWrite(greenPin,HIGH);
}
void loop(){
  // read the value of the switch
  buttonValue = digitalRead(button);
  // if the switch is HIGH, ie. pushed down - change the lights!
  if (buttonValue == LOW){
    changeLights();
  }
}
void changeLights() {
  digitalWrite(greenPin,LOW);
  for (int i = 0; i < yellowFlashTimes; i++) {
    digitalWrite(yellowPin,HIGH);
    delay(yellowFlashRate);
    digitalWrite(yellowPin,LOW);
    delay(yellowFlashRate);
  }
  digitalWrite(redPin,HIGH);
  delay(redDelay);
  digitalWrite(redPin,LOW);
  digitalWrite(greenPin,HIGH);
  
}

