import serial
import os
import time
import datetime
import MySQLdb

db = MySQLdb.connect("localhost","root","","chart_db")
cursor= db.cursor()
# # if __name__ == '__main__':
#     try:
#         db = MySQLdb.connect("localhost","root","test","DB_CPU")
#         c= db.cursor()
#     except:
#         # print ("Keine Verbindung zum Server...")
#         pass

device = 'COM6' #this will have to be changed to the serial port you are using
try:
  print ("Trying...",device)
  arduino = serial.Serial(device, 9600) 
  # print ("Trying...",arduino)
except: 
  print ("Failed to connect on",device ) 

 
             
# def getCPUtemperature():
# t_cpu = os.popen('vcgencmd measure_temp').readline()
# t_cpu = t_cpu.replace("temp=","").replace("'C\n","")
# return(t_cpu)
while 1:
    # try:
    time.sleep(1)
    data1 = arduino.readline()  #read the data from the arduino
    c=data1.decode("ASCII")

    data2 = arduino.readline()  #read the data from the arduino
    d=data2.decode("ASCII")
    
    data3 = arduino.readline()  #read the data from the arduino
    n=data3.decode("ASCII")
    

# def insert_to_db():
# temperatur = t_cpu
    zeit = (datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S "))
    datum = (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
# print ( zeit + " - " + datum)
# sql =  "INSERT INTO weatherdata ( V_data,V_time) VALUES (%s, %s)",(datum,zeit) 
# try:
#     c.execute(sql,( str(datum), str(zeit)))
#     db.commit()
# except:
#     pass
    a=str(zeit)
    b=str(datum)
    print(a)
    print(b)
    
    
    print(c)
    print(d)
    print(n)
    # a=str(a)

    c=float(c)
    d=float(d)
    n=float(n)

    # a=cursor.execute(""" INSERT INTO   datachart_parameter(timestamp,time,Speed,Temperature,Voltage)VALUES (%s,%s,%s,%s,%s)""",[b,a,c,d,n])

    # db.commit() 
    # cursor.close()

#     #     db.rollback()
#     #db.close()

# def read_from_db():
#     try:
        #c.execute("SELECT * FROM TAB_CPU WHERE ID = (SELCET MAX(ID) FROM TAB_CPU)")
# c.execute("SELECT * FROM  weatherdata ORDER BY ID DESC LIMIT 1")      
# result = c.fetchall()
# # if result is not None:
# print ('CPU temperature: ' , result[0][1], '| time: ' , result[0][3], ' | datum: ' , result[0][2])
#     # except:
    #     print ("read error")
    
# def main():
    # while 1:
    #     insert_to_db()
    #     read_from_db()
    #     time.sleep(10)
    
        
# if __name__ == '__main__':
#     try:
#         db = MySQLdb.connect("localhost","root","test","DB_CPU")
#         c= db.cursor()
#     except:
#         print ("Keine Verbindung zum Server...")
             
#     try:
#       main()
#     except KeyboardInterrupt:
#       print ("bye bye...")
#       pass    
        
