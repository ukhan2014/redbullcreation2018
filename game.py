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
    if(read_ser=="B1" and b1==1):
        b1=0
        print("Button 1 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(1, 22)
    elif(read_ser=="B2" and b2==1):
        b2=0
        print("Button 2 was pressed")
        if(b23 == 0):
        	print("Corresponding button 23 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(2, 23)
    elif(read_ser=="B3" and b3==1):
        b3=0
        print("Button 3 was pressed")
        if(b24 == 0):
        	print("Corresponding button 24 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(3, 24)
    elif(read_ser=="B4" and b4==1):
        b4=0
        print("Button 4 was pressed")
        if(b25 == 0):
        	print("Corresponding button 25 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(4, 25)
    elif(read_ser=="B5" and b5==1):
        b5=0
        print("Button 5 was pressed")
        if(b26 == 0):
        	print("Corresponding button 26 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(5, 26)
    elif(read_ser=="B6" and b6==1):
        b6=0
        print("Button 6 was pressed")
        if(b27 == 0):
        	print("Corresponding button 27 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(6, 27)
    elif(read_ser=="B7" and b7==1):
        b7=0
        print("Button 7 was pressed")
        if(b28 == 0):
        	print("Corresponding button 28 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(7, 28)
    elif(read_ser=="B8" and b8==1):
        b8=0
        print("Button 8 was pressed")
        if(b29 == 0):
        	print("Corresponding button 29 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(8, 29)
    elif(read_ser=="B9" and b9==1):
        b9=0
        print("Button 9 was pressed")
        if(b30 == 0):
        	print("Corresponding button 30 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(9, 30)
    elif(read_ser=="B10" and b10==1):
        b10=0
        print("Button 10 was pressed")
        if(b31 == 0):
        	print("Corresponding button 31 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(10, 31)
    elif(read_ser=="B11" and b11==1):
        b11=0
        print("Button 11 was pressed")
        if(b32 == 0):
        	print("Corresponding button 32 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(11, 32)
    elif(read_ser=="B12" and b12==1):
        b12=0
        print("Button 12 was pressed")
        if(b33 == 0):
        	print("Corresponding button 33 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(12, 33)
    elif(read_ser=="B13" and b13==1):
        b13=0
        print("Button 13 was pressed")
        if(b34 == 0):
        	print("Corresponding button 34 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(13, 34)
    elif(read_ser=="B14" and b14==1):
        b14=0
        print("Button 14 was pressed")
        if(b35 == 0):
        	print("Corresponding button 35 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(14, 35)
    elif(read_ser=="B15" and b15==1):
        b15=0
        print("Button 15 was pressed")
        if(b36 == 0):
        	print("Corresponding button 36 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(15, 36)
    elif(read_ser=="B16" and b16==1):
        b16=0
        print("Button 16 was pressed")
        if(b37 == 0):
        	print("Corresponding button 37 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(16, 37)
    elif(read_ser=="B17" and b17==1):
        b17=0
        print("Button 17 was pressed")
        if(b38 == 0):
        	print("Corresponding button 38 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(17, 38)
    elif(read_ser=="B18" and b18==1):
        b18=0
        print("Button 18 was pressed")
        if(b39 == 0):
        	print("Corresponding button 39 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(18, 39)
    elif(read_ser=="B19" and b19==1):
        b19=0
        print("Button 19 was pressed")
        if(b40 == 0):
        	print("Corresponding button 40 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(19, 40)
    elif(read_ser=="B20" and b20==1):
        b20=0
        print("Button 20 was pressed")
        if(b41 == 0):
        	print("Corresponding button 41 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(20, 41)
    elif(read_ser=="B21" and b21==1):
        b21=0
        print("Button 21 was pressed")
        if(b42 == 0):
        	print("Corresponding button 42 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(21, 42)
    elif(read_ser=="B22" and b22==1):
        b22=0
        print("Button 22 was pressed")
        if(b1 == 0):
        	print("Corresponding button 1 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(22, 1)
    elif(read_ser=="B23" and b23==1):
        b23=0
        print("Button 23 was pressed")
        if(b2 == 0):
        	print("Corresponding button 2 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(23, 2)
    elif(read_ser=="B24" and b24==1):
        b24=0
        print("Button 24 was pressed")
        if(b3 == 0):
        	print("Corresponding button 3 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(24, 3)
    elif(read_ser=="B25" and b25==1):
        b25=0
        print("Button 25 was pressed")
        if(b4 == 0):
        	print("Corresponding button 4 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(25, 4)
    elif(read_ser=="B26" and b26==1):
        b26=0
        print("Button 26 was pressed")
        if(b5 == 0):
        	print("Corresponding button 5 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(26, 5)
    elif(read_ser=="B27" and b27==1):
        b27=0
        print("Button 27 was pressed")
        if(b6 == 0):
        	print("Corresponding button 6 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(27, 6)
    elif(read_ser=="B28" and b28==1):
        b28=0
        print("Button 28 was pressed")
        if(b7 == 0):
        	print("Corresponding button 7 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(28, 7)
    elif(read_ser=="B29" and b29==1):
        b29=0
        print("Button 29 was pressed")
        if(b8 == 0):
        	print("Corresponding button 8 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(29, 8)
    elif(read_ser=="B30" and b30==1):
        b30=0
        print("Button 30 was pressed")
        if(b9 == 0):
        	print("Corresponding button 9 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(30, 9)
    elif(read_ser=="B31" and b31==1):
        b31=0
        print("Button 31 was pressed")
        if(b10 == 0):
        	print("Corresponding button 10 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(31, 10)
    elif(read_ser=="B32" and b32==1):
        b32=0
        print("Button 32 was pressed")
        if(b11 == 0):
        	print("Corresponding button 11 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(32, 11)
    elif(read_ser=="B33" and b33==1):
        b33=0
        print("Button 33 was pressed")
        if(b12 == 0):
        	print("Corresponding button 12 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(33, 12)
    elif(read_ser=="B34" and b34==1):
        b34=0
        print("Button 34 was pressed")
        if(b13 == 0):
        	print("Corresponding button 13 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(34, 13)
    elif(read_ser=="B35" and b35==1):
        b35=0
        print("Button 35 was pressed")
        if(b14 == 0):
        	print("Corresponding button 14 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(35, 14)
    elif(read_ser=="B36" and b36==1):
        b36=0
        print("Button 36 was pressed")
        if(b15 == 0):
        	print("Corresponding button 15 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(36, 15)
    elif(read_ser=="B37" and b37==1):
        b37=0
        print("Button 37 was pressed")
        if(b16 == 0):
        	print("Corresponding button 16 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(37, 16)
    elif(read_ser=="B38" and b38==1):
        b38=0
        print("Button 38 was pressed")
        if(b17 == 0):
        	print("Corresponding button 17 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(38, 17)
    elif(read_ser=="B39" and b39==1):
        b39=0
        print("Button 39 was pressed")
        if(b18 == 0):
        	print("Corresponding button 18 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(39, 18)
    elif(read_ser=="B40" and b40==1):
        b40=0
        print("Button 40 was pressed")
        if(b19 == 0):
        	print("Corresponding button 19 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(40, 19)
    elif(read_ser=="B41" and b41==1):
        b41=0
        print("Button 41 was pressed")
        if(b20 == 0):
        	print("Corresponding button 20 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(41, 20)
    elif(read_ser=="B42" and b42==1):
        b42=0
        print("Button 42 was pressed")
        if(b21 == 0):
       	 	print("Corresponding button 21 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(42, 21)
    elif(read_ser=="B43" and b43==1):
        b43=0
        print("Button 43 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(43, 22)
    elif(read_ser=="B44" and b44==1):
        b44=0
        print("Button 44 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(44, 22)
    elif(read_ser=="B45" and b45==1):
        b45=0
        print("Button 45 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(45, 22)
    elif(read_ser=="B46" and b46==1):
        b46=0
        print("Button 46 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(46, 22)
    elif(read_ser=="B47" and b47==1):
        b47=0
        print("Button 47 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(47, 22)
    elif(read_ser=="B48" and b48==1):
        b48=0
        print("Button 48 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(48, 22)
    elif(read_ser=="B49" and b49==1):
        b49=0
        print("Button 49 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	fullBright(49, 22)
