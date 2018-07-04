import serial
import time

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600


b01=1; b05=1; b09=1;  b13=1; b17=1; b21=1; b25=1; b29=1; b33=1; b37=1; b41=1; b45=1; b49=1; 
b02=1; b06=1; b10=1; b14=1; b18=1; b22=1; b26=1; b30=1; b34=1; b38=1; b42=1; b46=1; b50=1; 
b03=1; b07=1; b11=1; b15=1; b19=1; b23=1; b27=1; b31=1; b35=1; b39=1; b43=1; b47=1; b51=1; 
b04=1; b08=1; b12=1; b16=1; b20=1; b24=1; b28=1; b32=1; b36=1; b40=1; b44=1; b48=1; b52=1; 

while True:
    read_ser=ser.readline()
    if("B01" in read_ser and b01==1):
        b01=0
        print("Button 1 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(1, 22)
    elif("B02" in read_ser and b02==1):
        b02=0
        print("Button 2 was pressed")
        if(b23 == 0):
        	print("Corresponding button 23 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(2, 23)
    elif("B03" in read_ser and b03==1):
        b03=0
        print("Button 3 was pressed")
        if(b24 == 0):
        	print("Corresponding button 24 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(3, 24)
    elif("B04" in read_ser and b04==1):
        b04=0
        print("Button 4 was pressed")
        if(b25 == 0):
        	print("Corresponding button 25 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(4, 25)
    elif("B05" in read_ser and b05==1):
        b05=0
        print("Button 5 was pressed")
        if(b26 == 0):
        	print("Corresponding button 26 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(5, 26)
    elif("B06" in read_ser and b06==1):
        b06=0
        print("Button 6 was pressed")
        if(b27 == 0):
        	print("Corresponding button 27 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(6, 27)
    elif("B07" in read_ser and b07==1):
        b07=0
        print("Button 7 was pressed")
        if(b28 == 0):
        	print("Corresponding button 28 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(7, 28)
    elif("B08" in read_ser and b08==1):
        b08=0
        print("Button 8 was pressed")
        if(b29 == 0):
        	print("Corresponding button 29 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(8, 29)
    elif("B09" in read_ser and b09==1):
        b09=0
        print("Button 9 was pressed")
        if(b30 == 0):
        	print("Corresponding button 30 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(9, 30)
    elif("B10" in read_ser and b10==1):
        b10=0
        print("Button 10 was pressed")
        if(b31 == 0):
        	print("Corresponding button 31 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(10, 31)
    elif("B11" in read_ser and b11==1):
        b11=0
        print("Button 11 was pressed")
        if(b32 == 0):
        	print("Corresponding button 32 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(11, 32)
    elif("B12" in read_ser and b12==1):
        b12=0
        print("Button 12 was pressed")
        if(b33 == 0):
        	print("Corresponding button 33 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(12, 33)
    elif("B13" in read_ser and b13==1):
        b13=0
        print("Button 13 was pressed")
        if(b34 == 0):
        	print("Corresponding button 34 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(13, 34)
    elif("B14" in read_ser and b14==1):
        b14=0
        print("Button 14 was pressed")
        if(b35 == 0):
        	print("Corresponding button 35 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(14, 35)
    elif("B15" in read_ser and b15==1):
        b15=0
        print("Button 15 was pressed")
        if(b36 == 0):
        	print("Corresponding button 36 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(15, 36)
    elif("B16" in read_ser and b16==1):
        b16=0
        print("Button 16 was pressed")
        if(b37 == 0):
        	print("Corresponding button 37 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(16, 37)
    elif("B17" in read_ser and b17==1):
        b17=0
        print("Button 17 was pressed")
        if(b38 == 0):
        	print("Corresponding button 38 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(17, 38)
    elif("B18" in read_ser and b18==1):
        b18=0
        print("Button 18 was pressed")
        if(b39 == 0):
        	print("Corresponding button 39 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(18, 39)
    elif("B19" in read_ser and b19==1):
        b19=0
        print("Button 19 was pressed")
        if(b40 == 0):
        	print("Corresponding button 40 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(19, 40)
    elif("B20" in read_ser and b20==1):
        b20=0
        print("Button 20 was pressed")
        if(b41 == 0):
        	print("Corresponding button 41 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(20, 41)
    elif("B21" in read_ser and b21==1):
        b21=0
        print("Button 21 was pressed")
        if(b42 == 0):
        	print("Corresponding button 42 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(21, 42)
    elif("B22" in read_ser and b22==1):
        b22=0
        print("Button 22 was pressed")
        if(b01 == 0):
        	print("Corresponding button 1 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(22, 1)
    elif("B23" in read_ser and b23==1):
        b23=0
        print("Button 23 was pressed")
        if(b02 == 0):
        	print("Corresponding button 2 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(23, 2)
    elif("B24" in read_ser and b24==1):
        b24=0
        print("Button 24 was pressed")
        if(b03 == 0):
        	print("Corresponding button 3 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(24, 3)
    elif("B25" in read_ser and b25==1):
        b25=0
        print("Button 25 was pressed")
        if(b04 == 0):
        	print("Corresponding button 4 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(25, 4)
    elif("B26" in read_ser and b26==1):
        b26=0
        print("Button 26 was pressed")
        if(b05 == 0):
        	print("Corresponding button 5 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(26, 5)
    elif("B27" in read_ser and b27==1):
        b27=0
        print("Button 27 was pressed")
        if(b06 == 0):
        	print("Corresponding button 6 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(27, 6)
    elif("B28" in read_ser and b28==1):
        b28=0
        print("Button 28 was pressed")
        if(b07 == 0):
        	print("Corresponding button 7 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(28, 7)
    elif("B29" in read_ser and b29==1):
        b29=0
        print("Button 29 was pressed")
        if(b08 == 0):
        	print("Corresponding button 8 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(29, 8)
    elif("B30" in read_ser and b30==1):
        b30=0
        print("Button 30 was pressed")
        if(b09 == 0):
        	print("Corresponding button 9 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(30, 9)
    elif("B31" in read_ser and b31==1):
        b31=0
        print("Button 31 was pressed")
        if(b10 == 0):
        	print("Corresponding button 10 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(31, 10)
    elif("B32" in read_ser and b32==1):
        b32=0
        print("Button 32 was pressed")
        if(b11 == 0):
        	print("Corresponding button 11 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(32, 11)
    elif("B33" in read_ser and b33==1):
        b33=0
        print("Button 33 was pressed")
        if(b12 == 0):
        	print("Corresponding button 12 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(33, 12)
    elif("B34" in read_ser and b34==1):
        b34=0
        print("Button 34 was pressed")
        if(b13 == 0):
        	print("Corresponding button 13 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(34, 13)
    elif("B35" in read_ser and b35==1):
        b35=0
        print("Button 35 was pressed")
        if(b14 == 0):
        	print("Corresponding button 14 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(35, 14)
    elif("B36" in read_ser and b36==1):
        b36=0
        print("Button 36 was pressed")
        if(b15 == 0):
        	print("Corresponding button 15 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(36, 15)
    elif("B37" in read_ser and b37==1):
        b37=0
        print("Button 37 was pressed")
        if(b16 == 0):
        	print("Corresponding button 16 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(37, 16)
    elif("B38" in read_ser and b38==1):
        b38=0
        print("Button 38 was pressed")
        if(b17 == 0):
        	print("Corresponding button 17 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(38, 17)
    elif("B39" in read_ser and b39==1):
        b39=0
        print("Button 39 was pressed")
        if(b18 == 0):
        	print("Corresponding button 18 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(39, 18)
    elif("B40" in read_ser and b40==1):
        b40=0
        print("Button 40 was pressed")
        if(b19 == 0):
        	print("Corresponding button 19 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(40, 19)
    elif("B41" in read_ser and b41==1):
        b41=0
        print("Button 41 was pressed")
        if(b20 == 0):
        	print("Corresponding button 20 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(41, 20)
    elif("B42" in read_ser and b42==1):
        b42=0
        print("Button 42 was pressed")
        if(b21 == 0):
       	 	print("Corresponding button 21 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(42, 21)
    elif("B43" in read_ser and b43==1):
        b43=0
        print("Button 43 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(43, 22)
    elif("B44" in read_ser and b44==1):
        b44=0
        print("Button 44 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(44, 22)
    elif("B45" in read_ser and b45==1):
        b45=0
        print("Button 45 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(45, 22)
    elif("B46" in read_ser and b46==1):
        b46=0
        print("Button 46 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(46, 22)
    elif("B47" in read_ser and b47==1):
        b47=0
        print("Button 47 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(47, 22)
    elif("B48" in read_ser and b48==1):
        b48=0
        print("Button 48 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(48, 22)
    elif("B49" in read_ser and b49==1):
        b49=0
        print("Button 49 was pressed")
        if(b22 == 0):
        	print("Corresponding button 22 pressed too, FULL BRIGHTNESS to both!")
        	#fullBright(49, 22) 
