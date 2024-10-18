void setup() { 
  Serial.begin(115200); // Initialize serial communication at 9600 baud rate
}

void loop() {

  Serial.println("This is arduino.");
  delay(1000); // Wait for 1 second
}