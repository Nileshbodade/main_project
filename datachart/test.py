import datetime
import os
import serial
import time
while True:
    time.sleep(2)
    device = "COM6"
    print ("Trying...",device)
    arduino = serial.Serial(device, 9600) 

    #time.sleep(1)
    data1 = arduino.readline()  #read the data from the arduino
    c=data1.decode("ASCII")

    data2 = arduino.readline()  #read the data from the arduino
    d=data2.decode("ASCII")

    data3 = arduino.readline()  #read the data from the arduino
    n=data3.decode("ASCII")

    zeit = (datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"))
    datum = (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

    a=str(zeit)
    b=str(datum)
    print(a)
    print(b)


print(c)
print(d)
print(n)

c=float(c)
d=float(d)
n=float(n)