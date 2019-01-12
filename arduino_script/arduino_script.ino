int inputPins[] = {2, 3, 4, 5, 6, 7};
int outputPins[] = {A2, A3, A4, A5, A6, A7};

/*

Daniel Kouchekinia - 2019
Team 1458 Driver Station Button Interface Arduino Script
 
Protocol:

Controlling LEDs:
 - Send analog pin followed immediately by 1 (on) or 0 (off) and a new line. (Ex. b'51\n' would turn on LED 5)

Retreiving Button States:
 - The Arduino will send the digital pin which is grounded immediately followed by a 1 (on) or 0 (off) and a new line. (Ex. b'51\n' signifies button 5 has just been pushed down)
*/

int inputPinPreviousStates[sizeof(outputPins)/sizeof(int)];

void setup() {
  for(int i = 0; i < sizeof(outputPins)/sizeof(int); i++){
    pinMode(outputPins[i], OUTPUT);
  }

  for(int i = 0; i < sizeof(inputPins)/sizeof(int); i++){
    pinMode(inputPins[i], INPUT_PULLUP);
  }

  for(int i = 0; i < sizeof(inputPinPreviousStates)/sizeof(int); i++){
    inputPinPreviousStates[i] = HIGH;
  }

  Serial.begin(9600);
}

void loop() {

  // Helps remove duplicate presses
  delay(50);
  
  for(int i = 0; i < sizeof(inputPins)/sizeof(int); i++){
    int value = digitalRead(inputPins[i]);
    if(value != inputPinPreviousStates[i]){
      Serial.print(inputPins[i]);
      Serial.println(value == 0 ? 1 : 0);
    }
    
    inputPinPreviousStates[i] = value;
  }

  while (Serial.available() > 0) {
    String raw = Serial.readStringUntil('\n');
    
    int pin = (raw.charAt(0) - '0') + A0;
    int state = raw.charAt(1) - '0';
    
    digitalWrite(pin, state == 0 ? LOW : HIGH);
  }
  
}
