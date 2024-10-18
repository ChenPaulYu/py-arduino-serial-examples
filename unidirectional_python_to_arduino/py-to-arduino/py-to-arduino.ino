void setup() { 
  Serial.begin(115200); // Initialize serial communication at 9600 baud rate
}

void loop() {

  if (Serial.available()) {
    char userInput = Serial.read();
    Serial.println(userInput);

  } 


  delay(100); // Wait for 1 second
}