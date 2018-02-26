int vel = 0;  // velocity
int pos = 0;  // position

void setup() {
  Serial.begin(19200);
}

void loop() {
  Serial.print(String(vel++) + ", " + String(++pos)+ "\n");
  delay(300);
}
