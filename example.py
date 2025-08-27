from Ultra_Sonic import UltraSonic #Import libraies 
from time import sleep

sensor=UltraSonic(18,'Board','mm')#Setup Ultra Sonic Sensor
#sensor=UltraSonic(24,'bcm','mm') # Can use BCM too
while True:
    data=sensor.distance()# sensor.distance() will return a distance value
    print(data)
    sleep(.25)
    if data<300:
        break
    
    
print('object found')#Make sure to read the README.md file