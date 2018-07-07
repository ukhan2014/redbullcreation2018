#include <TimerOne.h>

#include <Adafruit_NeoPixel.h>

#define LED_PIN 48

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers), 800 for others
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2), GRB for others
Adafruit_NeoPixel led = Adafruit_NeoPixel(21, LED_PIN, NEO_RGB + NEO_KHZ400);

int b1State = 1;int b2State = 1;int b3State = 1;int b4State = 1;int b5State = 1;
int b6State = 1;int b7State = 1;int b8State = 1;int b9State = 1;int b10State = 1;
int b11State = 1;int b12State = 1;int b13State = 1;int b14State = 1;int b15State = 1;
int b16State = 1;int b17State = 1;int b18State = 1;int b19State = 1;int b20State = 1;
int b21State = 1;int b22State = 1;int b23State = 1;int b24State = 1;int b25State = 1;
int b26State = 1;int b27State = 1;int b28State = 1;int b29State = 1;int b30State = 1;
int b31State = 1;int b32State = 1;int b33State = 1;int b34State = 1;int b35State = 1;
int b36State = 1;int b37State = 1;int b38State = 1;int b39State = 1;int b40State = 1;
int b41State = 1;int b42State = 1;int b43State = 1;int b44State = 1;int b45State = 1;

String data="Hello From Arduino! msg #: ";
String m;

void setup() {
    //attachInterrupt(digitalPinToInterrupt(19), resetISR, RISING);
    attachInterrupt(digitalPinToInterrupt(19), p1Pressed, RISING);
    attachInterrupt(digitalPinToInterrupt(18), p2Pressed, RISING);

// put your setup code here, to run once:
Serial.begin(115200);
led.begin();
led.show(); // Initialize all pixels to 'off'
pinMode(0, INPUT);pinMode(1, INPUT);pinMode(2, INPUT);pinMode(3, INPUT);pinMode(4, INPUT);
pinMode(5, INPUT);pinMode(6, INPUT);pinMode(7, INPUT);pinMode(8, INPUT);pinMode(9, INPUT);
pinMode(10, INPUT);pinMode(11, INPUT);pinMode(12, INPUT);pinMode(13, INPUT);pinMode(14, INPUT);
pinMode(15, INPUT);pinMode(16, INPUT);pinMode(17, INPUT);pinMode(18, INPUT);
pinMode(22, INPUT);pinMode(23, INPUT);pinMode(24, INPUT);
pinMode(25, INPUT);pinMode(26, INPUT);pinMode(27, INPUT);pinMode(28, INPUT);pinMode(29, INPUT);
pinMode(30, INPUT);pinMode(31, INPUT);pinMode(32, INPUT);pinMode(33, INPUT);pinMode(34, INPUT);
pinMode(35, INPUT);pinMode(36, INPUT);pinMode(37, INPUT);pinMode(38, INPUT);pinMode(39, INPUT);
pinMode(40, INPUT);pinMode(41, INPUT);pinMode(42, INPUT);pinMode(43, INPUT);pinMode(44, INPUT);pinMode(45,INPUT);
pinMode(48, OUTPUT);

startAnimation();
}

void(* resetFunc) (void) = 0; //declare reset function @ address 0

int rx(String msg, String match) { return (msg.indexOf(match) > 0); }

void loop() {
  m = Serial.readString();
  int mlen = strlen(m);

  Serial.print("message: ");
  Serial.println(m);
      Serial.print("strlen: ");
  Serial.println(mlen);
    
  if(rx(m, "p1ready")){ } else if(rx(m, "p2ready")){ } else if(rx(m, "reset")){ resetFunc(); }
  else if(rx(m, "F1,22")){setSpecificLedPairGreen(1,22);} else if(rx(m, "F2,23")){setSpecificLedPairGreen(2,23);} else if(rx(m, "F3,24")){setSpecificLedPairGreen(3,24);}
   else if(rx(m, "F4,25")){setSpecificLedPairGreen(4,25);} else if(rx(m, "F5,26")){setSpecificLedPairGreen(5,26);} else if(rx(m, "F6,27")){setSpecificLedPairGreen(6,27);}
    else if(rx(m, "F7,28")){setSpecificLedPairGreen(7,28);} else if(rx(m, "F8,29")){setSpecificLedPairGreen(8,29);} else if(rx(m, "F9,30")){setSpecificLedPairGreen(9,30);}
     else if(rx(m, "F10,31")){setSpecificLedPairGreen(10,31);} else if(rx(m, "F11,32")){setSpecificLedPairGreen(11,32);} else if(rx(m, "F12,33")){setSpecificLedPairGreen(12,33);}
      else if(rx(m, "F13,34")){setSpecificLedPairGreen(13,34);} else if(rx(m, "F14,35")){setSpecificLedPairGreen(14,35);} else if(rx(m, "F15,36")){setSpecificLedPairGreen(15,36);}
       else if(rx(m, "F16,37")){setSpecificLedPairGreen(16,37);} else if(rx(m, "F17,38")){setSpecificLedPairGreen(17,38);} else if(rx(m, "F18,39")){setSpecificLedPairGreen(18,39);}
        else if(rx(m, "F19,40")){setSpecificLedPairGreen(19,40);} else if(rx(m, "F20,41")){setSpecificLedPairGreen(20,41);} else if(rx(m, "F21,42")){setSpecificLedPairGreen(21,42);}
         else if(rx(m, "F22,1")){setSpecificLedPairGreen(22,1);} else if(rx(m, "F23,2")){setSpecificLedPairGreen(23,2);} else if(rx(m, "F24,3")){setSpecificLedPairGreen(24,3);}
          else if(rx(m, "F25,4")){setSpecificLedPairGreen(25,4);} else if(rx(m, "F26,5")){setSpecificLedPairGreen(26,5);} else if(rx(m, "F27,6")){setSpecificLedPairGreen(27,6);}
           else if(rx(m, "F28,7")){setSpecificLedPairGreen(28,7);} else if(rx(m, "F29,8")){setSpecificLedPairGreen(29,8);} else if(rx(m, "F30,9")){setSpecificLedPairGreen(30,9);}
            else if(rx(m, "F31,10")){setSpecificLedPairGreen(31,10);} else if(rx(m, "F32,11")){setSpecificLedPairGreen(32,11);} else if(rx(m, "F33,12")){setSpecificLedPairGreen(33,12);}
             else if(rx(m, "F34,13")){setSpecificLedPairGreen(34,13);} else if(rx(m, "F35,14")){setSpecificLedPairGreen(35,14);} else if(rx(m, "F36,15")){setSpecificLedPairGreen(36,15);}
              else if(rx(m, "F37,16")){setSpecificLedPairGreen(37,16);} else if(rx(m, "F38,17")){setSpecificLedPairGreen(38,17);} else if(rx(m, "F39,18")){setSpecificLedPairGreen(39,18);}
               else if(rx(m, "F40,19")){setSpecificLedPairGreen(40,19);} else if(rx(m, "F41,20")){setSpecificLedPairGreen(41,20);} else if(rx(m, "F42,21")){setSpecificLedPairGreen(42,21);}

  b1State = digitalRead(49);b2State = digitalRead(45);b3State = digitalRead(2);b4State = digitalRead(3);b5State = digitalRead(4);
  b6State = digitalRead(5);b7State = digitalRead(6);b8State = digitalRead(7);b9State = digitalRead(8);b10State = digitalRead(9);
  b11State = digitalRead(10);b12State = digitalRead(11);b13State = digitalRead(12);b14State = digitalRead(13);b15State = digitalRead(14);
  b16State = digitalRead(15);b17State = digitalRead(16);b18State = digitalRead(17);b19State = digitalRead(18);b20State = digitalRead(42);
  b21State = digitalRead(43);b22State = digitalRead(44);b23State = digitalRead(22);b24State = digitalRead(23);b25State = digitalRead(24);
  b26State = digitalRead(25);b27State = digitalRead(26);b28State = digitalRead(27);b29State = digitalRead(28);b30State = digitalRead(29);
  b31State = digitalRead(30);b32State = digitalRead(31);b33State = digitalRead(32);b34State = digitalRead(33);b35State = digitalRead(34);
  b36State = digitalRead(35);b37State = digitalRead(36);b38State = digitalRead(37);b39State = digitalRead(38);b40State = digitalRead(39);
  b41State = digitalRead(40);b42State = digitalRead(41);b43State = digitalRead(46);b44State = digitalRead(47);
  
  if(b1State) { Serial.println("B01"); } else if(b2State) { Serial.println("B02"); } else if(b3State) { Serial.println("B03"); } 
  else if(b4State) { Serial.println("B04"); } else if(b5State) { Serial.println("B05");  } else if(b6State) { Serial.println("B06");
  } else if(b7State) { Serial.println("B07"); } else if(b8State) { Serial.println("B08"); } else if(b9State) { Serial.println("B09");
  } else if(b10State) { Serial.println("B10"); } else if(b11State) { Serial.println("B11"); } else if(b12State) { Serial.println("B12");
  } else if(b13State) { Serial.println("B13"); } else if(b14State) { Serial.println("B14"); } else if(b15State) { Serial.println("B15");
  } else if(b16State) { Serial.println("B16"); } else if(b17State) { Serial.println("B17"); } else if(b18State) { Serial.println("B18");
  } else if(b19State) { Serial.println("B19"); } else if(b20State) { Serial.println("B20"); } else if(b21State) { Serial.println("B21");
  } else if(b22State) { Serial.println("B22"); } else if(b23State) { Serial.println("B23"); } else if(b24State) { Serial.println("B24");
  } else if(b25State) { Serial.println("B25"); } else if(b26State) { Serial.println("B26"); } else if(b27State) { Serial.println("B27");
  } else if(b28State) { Serial.println("B28"); } else if(b29State) { Serial.println("B29"); } else if(b30State) { Serial.println("B30");
  } else if(b31State) { Serial.println("B31"); } else if(b32State) { Serial.println("B32"); } else if(b33State) { Serial.println("B33");
  } else if(b34State) { Serial.println("B34"); } else if(b35State) { Serial.println("B35"); } else if(b36State) { Serial.println("B36");
  } else if(b37State) { Serial.println("B37"); } else if(b38State) { Serial.println("B38"); } else if(b39State) { Serial.println("B39");
  } else if(b40State) { Serial.println("B40"); } else if(b41State) { Serial.println("B41"); } else if(b42State) { Serial.println("B42");
  }  
  else { 
    Serial.println("NIL"); 

  }
}

void resetISR() {
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  Serial.println("RESET");
  resetFunc();
}


void p1Pressed() {
  Serial.println("START_P1");
}

void p2Pressed() {
  Serial.println("START_P2");
}

void startAnimation() {
  setLEDs100();delay(200);setLEDs0();delay(200);
  setLEDs100();delay(200);setLEDs0();delay(200);
  setLEDs100();delay(200);setLEDs0();delay(200);
  setLEDs100();delay(200);setLEDs0();delay(200);
  setLEDs100();delay(200);setLEDs0();delay(200);
  setLEDs0();
}

void setLEDs50() {
    led.setPixelColor(0,  0, 128, 0);  led.setPixelColor(13,  0, 128, 0);  led.setPixelColor(26,  0, 128, 0); led.setPixelColor(39,  0, 128, 0);
    led.setPixelColor(1,  0, 128, 0);  led.setPixelColor(14,  0, 128, 0);  led.setPixelColor(27,  0, 128, 0); led.setPixelColor(40,  0, 128, 0);
    led.setPixelColor(2,  0, 128, 0);  led.setPixelColor(15,  0, 128, 0);  led.setPixelColor(28,  0, 128, 0); led.setPixelColor(41,  0, 128, 0);
    led.setPixelColor(3,  0, 128, 0);  led.setPixelColor(16,  0, 128, 0);  led.setPixelColor(29,  0, 128, 0); led.setPixelColor(42,  0, 128, 0);
    led.setPixelColor(4,  0, 128, 0);  led.setPixelColor(17,  0, 128, 0);  led.setPixelColor(30,  0, 128, 0); led.setPixelColor(43,  0, 128, 0);
    led.setPixelColor(5,  0, 128, 0);  led.setPixelColor(18,  0, 128, 0);  led.setPixelColor(31,  0, 128, 0); led.setPixelColor(44,  0, 128, 0);
    led.setPixelColor(6,  0, 128, 0);  led.setPixelColor(19,  0, 128, 0);  led.setPixelColor(32,  0, 128, 0); led.setPixelColor(45,  0, 128, 0);
    led.setPixelColor(7,  0, 128, 0);  led.setPixelColor(20,  0, 128, 0);  led.setPixelColor(33,  0, 128, 0); led.setPixelColor(46,  0, 128, 0);
    led.setPixelColor(8,  0, 128, 0);  led.setPixelColor(21,  0, 128, 0);  led.setPixelColor(34,  0, 128, 0); led.setPixelColor(47,  0, 128, 0);
    led.setPixelColor(9,  0, 128, 0);  led.setPixelColor(22,  0, 128, 0);  led.setPixelColor(35,  0, 128, 0); led.setPixelColor(48,  0, 128, 0);
    led.setPixelColor(10, 0, 128, 0);  led.setPixelColor(23, 0, 128, 0);  led.setPixelColor(36, 0, 128, 0); led.setPixelColor(49, 0, 128, 0);
    led.setPixelColor(11, 0, 128, 0);  led.setPixelColor(24, 0, 128, 0);  led.setPixelColor(37, 0, 128, 0); led.setPixelColor(50, 0, 128, 0);
    led.setPixelColor(12, 0, 128, 0);  led.setPixelColor(25, 0, 128, 0);  led.setPixelColor(38, 0, 128, 0); led.setPixelColor(51, 0, 128, 0);
    led.show();
}

void setLEDs100() {
      led.setPixelColor(0,  0, 255, 0);  led.setPixelColor(13,  0, 255, 0);  led.setPixelColor(26,  0, 255, 0); led.setPixelColor(39,  0, 255, 0);
    led.setPixelColor(1,  0, 255, 0);  led.setPixelColor(14,  0, 255, 0);  led.setPixelColor(27,  0, 255, 0); led.setPixelColor(40,  0, 255, 0);
    led.setPixelColor(2,  0, 255, 0);  led.setPixelColor(15,  0, 255, 0);  led.setPixelColor(28,  0, 255, 0); led.setPixelColor(41,  0, 255, 0);
    led.setPixelColor(3,  0, 255, 0);  led.setPixelColor(16,  0, 255, 0);  led.setPixelColor(29,  0, 255, 0); led.setPixelColor(42,  0, 255, 0);
    led.setPixelColor(4,  0, 255, 0);  led.setPixelColor(17,  0, 255, 0);  led.setPixelColor(30,  0, 255, 0); led.setPixelColor(43,  0, 255, 0);
    led.setPixelColor(5,  0, 255, 0);  led.setPixelColor(18,  0, 255, 0);  led.setPixelColor(31,  0, 255, 0); led.setPixelColor(44,  0, 255, 0);
    led.setPixelColor(6,  0, 255, 0);  led.setPixelColor(19,  0, 255, 0);  led.setPixelColor(32,  0, 255, 0); led.setPixelColor(45,  0, 255, 0);
    led.setPixelColor(7,  0, 255, 0);  led.setPixelColor(20,  0, 255, 0);  led.setPixelColor(33,  0, 255, 0); led.setPixelColor(46,  0, 255, 0);
    led.setPixelColor(8,  0, 255, 0);  led.setPixelColor(21,  0, 255, 0);  led.setPixelColor(34,  0, 255, 0); led.setPixelColor(47,  0, 255, 0);
    led.setPixelColor(9,  0, 255, 0);  led.setPixelColor(22,  0, 255, 0);  led.setPixelColor(35,  0, 255, 0); led.setPixelColor(48,  0, 255, 0);
    led.setPixelColor(10, 0, 255, 0);  led.setPixelColor(23,  0, 255, 0);  led.setPixelColor(36,  0, 255, 0); led.setPixelColor(49,  0, 255, 0);
    led.setPixelColor(11, 0, 255, 0);  led.setPixelColor(24,  0, 255, 0);  led.setPixelColor(37,  0, 255, 0); led.setPixelColor(50,  0, 255, 0);
    led.setPixelColor(12, 0, 255, 0);  led.setPixelColor(25,  0, 255, 0);  led.setPixelColor(38,  0, 255, 0); led.setPixelColor(51,  0, 255, 0);
    led.show();
}

void setLEDs0() {
      led.setPixelColor(0,  0, 0, 0);  led.setPixelColor(13,  0, 0, 0);  led.setPixelColor(26,  0, 0, 0); led.setPixelColor(39,  0, 0, 0);
    led.setPixelColor(1,  0, 0, 0);  led.setPixelColor(14,  0, 0, 0);  led.setPixelColor(27,  0, 0, 0); led.setPixelColor(40,  0, 0, 0);
    led.setPixelColor(2,  0, 0, 0);  led.setPixelColor(15,  0, 0, 0);  led.setPixelColor(28,  0, 0, 0); led.setPixelColor(41,  0, 0, 0);
    led.setPixelColor(3,  0, 0, 0);  led.setPixelColor(16,  0, 0, 0);  led.setPixelColor(29,  0, 0, 0); led.setPixelColor(42,  0, 0, 0);
    led.setPixelColor(4,  0, 0, 0);  led.setPixelColor(17,  0, 0, 0);  led.setPixelColor(30,  0, 0, 0); led.setPixelColor(43,  0, 0, 0);
    led.setPixelColor(5,  0, 0, 0);  led.setPixelColor(18,  0, 0, 0);  led.setPixelColor(31,  0, 0, 0); led.setPixelColor(44,  0, 0, 0);
    led.setPixelColor(6,  0, 0, 0);  led.setPixelColor(19,  0, 0, 0);  led.setPixelColor(32,  0, 0, 0); led.setPixelColor(45,  0, 0, 0);
    led.setPixelColor(7,  0, 0, 0);  led.setPixelColor(20,  0, 0, 0);  led.setPixelColor(33,  0, 0, 0); led.setPixelColor(46,  0, 0, 0);
    led.setPixelColor(8,  0, 0, 0);  led.setPixelColor(21,  0, 0, 0);  led.setPixelColor(34,  0, 0, 0); led.setPixelColor(47,  0, 0, 0);
    led.setPixelColor(9,  0, 0, 0);  led.setPixelColor(22,  0, 0, 0);  led.setPixelColor(35,  0, 0, 0); led.setPixelColor(48,  0, 0, 0);
    led.setPixelColor(10, 0, 0, 0);  led.setPixelColor(23,  0, 0, 0);  led.setPixelColor(36,  0, 0, 0); led.setPixelColor(49,  0, 0, 0);
    led.setPixelColor(11, 0, 0, 0);  led.setPixelColor(24,  0, 0, 0);  led.setPixelColor(37,  0, 0, 0); led.setPixelColor(50,  0, 0, 0);
    led.setPixelColor(12, 0, 0, 0);  led.setPixelColor(25,  0, 0, 0);  led.setPixelColor(38,  0, 0, 0); led.setPixelColor(51,  0, 0, 0);
    led.show();
}

void setSpecificLedPairGreen(int first, int second) {
  led.setPixelColor(first,  0, 255, 0);
  led.setPixelColor(second,  0, 255, 0);
  led.show();
}
