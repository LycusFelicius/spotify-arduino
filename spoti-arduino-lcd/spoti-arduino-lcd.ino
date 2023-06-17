/*
* Arduino LCD Tutorial
*
* Crated by Dejan Nedelkovski,
* www.HowToMechatronics.com
*
*/

#include <LiquidCrystal.h> // includes the LiquidCrystal Library 
LiquidCrystal lcd(2, 3, 4, 5, 6, 7); // Creates an LCD object. Parameters: (rs, enable, d4, d5, d6, d7) 

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
}

void loop() {
  // when characters arrive over the serial port...
  if (Serial.available()) {
    lcd.clear();
    lcd.setCursor(0, 0);  
    // wait a bit for the entire message to arrive
    // clear the screen
    String song_name = Serial.readString();  //read until timeout
    song_name.trim();
    lcd.print(song_name);
    delay(100);
    lcd.setCursor(0, 1);
    String artist_name = Serial.readString();
    artist_name.trim();
    lcd.print(artist_name);  
    // read all the available characters
  }
}
