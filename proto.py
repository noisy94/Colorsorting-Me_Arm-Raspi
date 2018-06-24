#Prototyp
import time
import RPi.GPIO as IO
import sys
import os

IO.setmode (IO.BCM)
IO.setwarnings(False) 

servo1PIN = 8
servo2PIN = 24
servo3PIN = 7
servo4PIN = 25

IO.setmode(IO.BCM)
IO.setup(servo1PIN, IO.OUT)
IO.setup(servo2PIN, IO.OUT)
IO.setup(servo3PIN, IO.OUT)
IO.setup(servo4PIN, IO.OUT)

p1 = IO.PWM(servo1PIN, 50) # GPIO 8 als PWM mit 50Hz	
p1.start(6)                # Initialisierung

p2 = IO.PWM(servo2PIN, 50)
p2.start(7)

p3 = IO.PWM(servo3PIN, 50) # GPIO 7 als PWM mit 50Hz
p3.start(5.5)              # Initialisierung

p4 = IO.PWM(servo4PIN, 50) # GPIO 25 als PWM mit 50Hz
p4.start(7.5)              # Initialisierung

x=0

IO.setup(18,IO.OUT) #Green
IO.setup(23,IO.OUT) #Blau
IO.setup(24,IO.OUT) #Rot

IO.setup(19,IO.OUT)   #rs
IO.setup(26,IO.OUT)   #e
IO.setup(12,IO.OUT)   #d4
IO.setup(16,IO.OUT)   #d5
IO.setup(20,IO.OUT)   #d6
IO.setup(21,IO.OUT)   #d7

IO.setup(5,IO.OUT)   #s2
IO.setup(6,IO.OUT)   #s3
IO.setup(13,IO.OUT)  #oe
IO.setup(11,IO.OUT)  #reset

IO.setup(2,IO.IN)    #q1
IO.setup(3,IO.IN)    #q2
IO.setup(4,IO.IN)    #q3
IO.setup(17,IO.IN)   #q4
IO.setup(27,IO.IN)   #q5
IO.setup(22,IO.IN)   #q6
IO.setup(10,IO.IN)   #q7
IO.setup(9,IO.IN)    #q8

LINE=[0x00,0x40]
SETCURSOR=0x80

def send_a_command (command):                
    pin=command
    PORT(pin)                                                
    IO.output(19,0)                                           
    IO.output(26,1)                                         
    time.sleep(0.005)
    IO.output(26,0)
    pin=((command<<4)& 0xF0)    
    PORT(pin)
    IO.output(26,1)
    time.sleep(0.005)
    IO.output(26,0)                                    
    pin=0
    PORT(pin)                                               

def send_a_character (character):                
    pin=character
    PORT(pin)
    IO.output(19,1)
    IO.output(26,1)
    time.sleep(0.005)
    IO.output(26,0)
    pin=((character<<4)& 0xF0)    
    PORT(pin)
    IO.output(26,1)
    time.sleep(0.005)
    IO.output(26,0)                                    
    pin=0
    PORT(pin)

def GotoLine (row):
    addr=LINE[row]
    a=SETCURSOR+addr
    send_a_command(a)

def PORT(pin):                                     
    if(pin&0x10 == 0x10):
        IO.output(12,1)
    else:
        IO.output(12,0)
    if(pin&0x20 == 0x20):
        IO.output(16,1)
    else:
        IO.output(16,0)
    if(pin&0x40 == 0x40):
        IO.output(20,1)
    else:
        IO.output(20,0)
    if(pin&0x80 == 0x80):
        IO.output(21,1)                        
    else:
        IO.output(21,0)                       

def lcd_init():
    send_a_command(0x29); # 39					
    send_a_command(0x1C); # 1C
    send_a_command(0x52); # 52
    send_a_command(0x69); # 69
    send_a_command(0x74); # 74
    send_a_command(0x28); # 38
    send_a_command(0x0C); # 0F
    send_a_command(0x01); # 01
    send_a_command(0x06); # 06
    send_a_command(0x80); # 06

def sendChar(ch):
    send_a_character(ord(ch))

def show(string):
    for charac in string:
        sendChar(charac)	

try:

    while True:   
    
 	   lcd_init();
			   	   	
	   IO.output(5,1)   #s2 clear array
	   IO.output(6,0)   #s3
	   time.sleep(0.01)
	   IO.output(11,1)
	   time.sleep(0.02)
	   IO.output(11,0)
	   IO.output(13,0)
	   time.sleep(0.01)
	   IO.output(13,1)
      	   if(IO.input(2)==True):
       		 x=1
   	   if(IO.input(3)==True):
        	 x=x+2
    	   if(IO.input(4)==True):
        	 x=x+4
    	   if(IO.input(17)==True):
        	 x=x+8
   	   if(IO.input(27)==True):
        	 x=x+16
    	   if(IO.input(22)==True):
        	 x=x+32
   	   if(IO.input(10)==True):
        	 x=x+64
   	   if(IO.input(9)==True):
        	 x=x+128
    	   C=x
    	   x=0

	   IO.output(5,0)     #s2 red array
	   IO.output(6,0)     #s3
	   time.sleep(0.01)
	   IO.output(11,1)    #reset counter
	   time.sleep(0.02)
	   IO.output(11,0)    #reset counter
	   IO.output(13,0)    #OE  enable output of module for 10ms
	   time.sleep(0.01)
	   IO.output(13,1)    #OE
	   if(IO.input(2)==True):
	         x=1
	   if(IO.input(3)==True):
	         x=x+2
	   if(IO.input(4)==True):
	         x=x+4
	   if(IO.input(17)==True):
	         x=x+8
	   if(IO.input(27)==True):
	         x=x+16
	   if(IO.input(22)==True):
	         x=x+32
	   if(IO.input(10)==True):
	         x=x+64
	   if(IO.input(9)==True):
	         x=x+128
	   R=x
	   x=0
 
	   IO.output(5,0)    #s2 choose blue array
	   IO.output(6,1)    #s3
	   time.sleep(0.01)
	   IO.output(11,1)   #reset counter one time
	   time.sleep(0.02)
	   IO.output(11,0)
	   IO.output(13,0)   #enable output of module for 100ms
	   time.sleep(0.01)
	   IO.output(13,1)
	   if(IO.input(2)==True):
	         x=1
	   if(IO.input(3)==True):
	         x=x+2
	   if(IO.input(4)==True):
	         x=x+4
	   if(IO.input(17)==True):
	         x=x+8
	   if(IO.input(27)==True):
	         x=x+16
	   if(IO.input(22)==True):
	         x=x+32
	   if(IO.input(10)==True):
	         x=x+64
	   if(IO.input(9)==True):
	         x=x+128
	   B=x
	   x=0

	   IO.output(5,1)    #s2 choose green array
	   IO.output(6,1)    #s3
	   time.sleep(0.01)
	   IO.output(11,1)   #reset counter one time
	   time.sleep(0.02)
	   IO.output(11,0) 
	   IO.output(13,0)   #enable output of module for 100ms
	   time.sleep(0.01)
	   IO.output(13,1)
	   if(IO.input(2)==True):
	         x=1
	   if(IO.input(3)==True):
	         x=x+2
	   if(IO.input(4)==True):
	         x=x+4
	   if(IO.input(17)==True):
	         x=x+8
	   if(IO.input(27)==True):
	         x=x+16
	   if(IO.input(22)==True):
	         x=x+32
	   if(IO.input(10)==True):
	         x=x+64
	   if(IO.input(9)==True):
	         x=x+128
	   G=x
    	   x=0

    
	   show('RGB ')
	   show(str(R));
	   show(' ');
	   show(str(G));
	   show(' ');
	   show(str(B))
	   show('  ')
 	   
	   send_a_command(0x80+0x40);   
   
	   print "Clear: " + str(C) + " Red: " + str(R) + " Blue: " + str(B) + " Green: " + str(G)

	   if (R>120):
         	print("RED")
	 	show('RED             ')
	 	IO.output(24,0)
	 	IO.output(23,0)
         	IO.output(18,1)
				
		p2.ChangeDutyCycle(8.5)
		time.sleep(0.5)
		
		p1.ChangeDutyCycle(8) # up-forward
                time.sleep(0.5)

    		p3.ChangeDutyCycle(10) 
    		time.sleep(0.5)

    		p1.ChangeDutyCycle(5.75)
    		time.sleep(0.5)

    		p4.ChangeDutyCycle(6.5)
    		time.sleep(0.5)

    		p1.ChangeDutyCycle(6.8)
    		time.sleep(0.5)

    		p3.ChangeDutyCycle(5.5)
    		time.sleep(0.5)

    		p1.ChangeDutyCycle(4.8)
    		time.sleep(0.5)

    		p4.ChangeDutyCycle(7.5)
    		time.sleep(0.5)

    	   elif (C>190):
#		send_a_command(0x40)
         	print("NICHT ERKANNT")
	 	show('NICHT ERKANNT   ')
	 					
		IO.output(24,1)
         	IO.output(23,1)
         	IO.output(18,1)

		
   	   elif (G>90):
#		send_a_command(0x40)
         	print("GREEN")
	 	show('GREEN           ')
	 	IO.output(24,1)
         	IO.output(23,0)
         	IO.output(18,0)

		p2.ChangeDutyCycle(8.5)
		time.sleep(0.5)

		p1.ChangeDutyCycle(8) # up-forward
                time.sleep(0.5)

   		p3.ChangeDutyCycle(10) #
   		time.sleep(0.5)

   		p1.ChangeDutyCycle(5.75)
   		time.sleep(0.5)

   		p4.ChangeDutyCycle(7.6)
   		time.sleep(0.5)

   		p3.ChangeDutyCycle(4.5)
   		time.sleep(0.5)

   		p4.ChangeDutyCycle(7.5)
   		time.sleep(0.5)

     	   elif (B>120):

         	print("BLUE")
         	show('BLUE            ')
	 	IO.output(24,0)
         	IO.output(23,1)
         	IO.output(18,0)

                p2.ChangeDutyCycle(8.5)
                time.sleep(0.5)

   		p1.ChangeDutyCycle(8) # up-forward
   		time.sleep(0.5)

   		p3.ChangeDutyCycle(10) #
   		time.sleep(0.5)

   		p1.ChangeDutyCycle(5.75)
   		time.sleep(0.5)

   		p4.ChangeDutyCycle(9)
   		time.sleep(0.5)

   		p1.ChangeDutyCycle(7.2)
   		time.sleep(0.5)

   		p3.ChangeDutyCycle(5.5)
   		time.sleep(0.5)

   		p1.ChangeDutyCycle(5.5)
   		time.sleep(0.5)

   		p4.ChangeDutyCycle(7.5)
   		time.sleep(0.5)
 	 
		
		#p2.ChangeDutyCycle(8.5)
	   time.sleep(1);
	   #send_a_command(0x01);
except KeyboardInterrupt:
	send_a_command(0x01)
	#IO.cleanup()
