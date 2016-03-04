import serial
import time
import string
#define ON=0400;
#define OFF=0000;
#define REV=1424;
DEVICE = '/dev/ttyACM0'
BAUD = 9600
ser= serial.Serial(DEVICE, BAUD)
while int c<30:
	Data=ser.readline()
	print Data
	#(s2, s3, s1)=[int(s) for s in Data.split(',')]
	s1= Data[0]
	s2= Data[1]
	s3= Data[2]
	if(s3!=0):
		if s1==0: 
			if s2==0:
				ser.write('ON','OFF')
			
		else if s1==0 :
				if s2==1 :
					ser.write('OFF','ON')
			
		else if s1=1 : 
				if s2=0 :
					ser.write('ON','OFF')
			
		else s1=1 : 
			if s2=1: 
			ser.write('ON','OFF')
			
	else 
		for(int i=0;i<50;i++):
			ser.write('REV','REV')
		ser.write('OFF','OFF')
		
	
	
	
