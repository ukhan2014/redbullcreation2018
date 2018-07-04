import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(1)  
    return

b1=1; b5=1; b9=1;  b13=1; b17=1; b21=1; b25=1; b29=1; b33=1; b37=1; b41=1; b45=1; b49=1; 
b2=1; b6=1; b10=1; b14=1; b18=1; b22=1; b26=1; b30=1; b34=1; b38=1; b42=1; b46=1; b50=1; 
b3=1; b7=1; b11=1; b15=1; b19=1; b23=1; b27=1; b31=1; b35=1; b39=1; b43=1; b47=1; b51=1; 
b4=1; b8=1; b12=1; b16=1; b20=1; b24=1; b28=1; b32=1; b36=1; b40=1; b44=1; b48=1; b52=1; 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
    read_ser=ser.readline()
    print(read_ser)
    if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else if(read_ser=="B1" && b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
    else
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0)
        print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        fullBright(1, 22)
