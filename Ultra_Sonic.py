import RPi.GPIO as pins
import time

class UltraSonic():
    def __init__(self,pin,mode,unit):
        self.pin=pin
        self.mode=mode
        self.unit=unit
        
    def distance(self): #Gets distance 
        Mode=self.mode
        Sig=self.pin
        Mode=Mode.lower()
        
        if Mode=='board':#Set Gpio mode BCM or BOARD
            pins.setmode(pins.BOARD)
        else: pins.setmode(pins.BCM)
        
        
        pins.setup(Sig,pins.OUT)
        pins.output(Sig,0)
        
        time.sleep(0.000002)
        
        pins.output(Sig,1)
        
        time.sleep(0.000005)
        
        pins.output(Sig,0)
        
        pins.setup(Sig,pins.IN)
        
        while pins.input(Sig)==0:
            starttime=time.time()
            
        while pins.input(Sig)==1:
            endtime=time.time()
            
        duration=endtime-starttime
        
#CONVERT PULSE DURATION INTO MEASUREMENT
        unit=self.unit
        unit=unit.lower()
        if unit=='cm' or unit=='centimeter':#Metric-Centimeters
            duration=duration*18250
        
        elif unit=='m' or unit=='meter':#Metric-Meters
            duration=duration*182.5
        
        elif unit=='mm' or unit=='milimeter':#Metric- Milimeters
            duration=duration*182500
        
        elif unit=='in' or unit=='inch': #Imperial- Inches
            duration=duration*6792
        
        elif unit=='f' or unit=='ft' or unit=='feet':#Imperial-Feet
            duration=duration*566
        
        elif unit=='yd' or unit=='yds' or unit=='yard': #Imperial-Yards
            duration=duration*188
        
        output=round(duration,2)#Round to 2 decimal places
        return output
