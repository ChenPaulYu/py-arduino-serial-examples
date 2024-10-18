void setup() { 
  Serial.begin(115200); // Initialize serial communication at 9600 baud rate
}

void loop() {

  if (Serial.available()) {
    char userInput = Serial.read();
    
    while (Serial.available() > 0) {
      Serial.read();
    }

    if (userInput == '1') {
      // Serial.println("Greeting from arduino1."); // Send data    
      Serial.println("Greeting from arduino2"); // Send data    
    }

  } 


  delay(100); // Wait for 1 second
}