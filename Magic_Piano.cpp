// Constants that won't change:
//Buttons
const int b_red = 8 , b_yellow = 9, b_blue = 10, b_green = 12, b_white = 13;
//LEDs
const int red = 2, yellow = 3, blue = 4, green = 5, white = 6;
//Buzzer
const int buzzer = 11;

//Arrays for initialization
int button[5] = {b_red, b_yellow, b_blue, b_green, b_white};
int led[5] = {red, yellow, blue, green, white};

//Notes
int notes[5] = {554, 622, 739, 830, 932};

// Variables that will change:
int lastState[5] = {HIGH, HIGH, HIGH, HIGH, HIGH}; // the previous state from the input pin
int currentState[5];    // the current reading from the input pin

void setup() {
  
  Serial.begin(9600); // initialize serial communication at 9600 bits per second:
  
  for (byte i = 0; i < 5; i = i + 1) { // initialize the pushbutton pin as an pull-up input The pull-up input pin will be HIGH when the switch is open and LOW when the switch is closed.
    pinMode(button[i], INPUT_PULLUP);
  }
  
    for (byte i = 0; i < 5; i = i + 1) { // initialize the pin of the LED as output
    pinMode(led[i], OUTPUT);
  }
  
  pinMode(buzzer,OUTPUT); //defining the pin of the buzzer as output
}

void loop() {
  for (byte i = 0; i < 5; i = i + 1) { // read the state of the buttons

    currentState[i] = digitalRead(button[i]);

    if(lastState[i] == LOW && currentState[i] == HIGH){
      tone(buzzer, notes[i]);       //turn the buzzer on
      digitalWrite(led[i], HIGH);   // turn the led on
      delay(300);                   // wait for 1 second
      noTone(buzzer);               //turn the buzzer down 
      digitalWrite(led[i], LOW);}   // turn the led down 
      lastState[i] = currentState[i];  // save the last state
  }
}
