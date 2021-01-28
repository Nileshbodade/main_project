from django.shortcuts import render, HttpResponse
# from django.utils import 
from django.http import JsonResponse
from .models import Par
from django.db.models import Sum
import datetime
import os
import serial
import time
import json
import MySQLdb




def index(request):
    # return render(request, "test.html")
    date = Parameter.objects.raw("SELECT * FROM datachart_parameter WHERE timestamp = 'timestamp' ")
    # for a in date:
        # print("timestamp:-", timestamp)
    datetime_query = Parameter.objects.raw("SELECT * FROM datachart_parameter WHERE time BETWEEN '08:00:00' AND '16:00:00'")

    value_query = Parameter.objects.raw("SELECT * , SUM(parameter_value) as sum FROM datachart_parameter  group by id")
    # print(value_query[0].sum)
    lis = []
    for a in datetime_query:
        time_int = str(a.time)


        V_str = str(a.Voltage )
        print('value:-' + V_str + 'time:-' + time_int)

        value_str = int(a.Voltage)
        lis.append(value_str)
    # print(sum(lis))
    a = sum(lis)
    # print(sum(add))

    return render(request, 'index.html', {'value_query': value_query, 'datetime_query': datetime_query, 'a': a})


def result(request):
    # print("df")
    from datetime import datetime
    if request.method == "POST":
        from_date = datetime.strptime(request.POST["from_date"],"%Y-%m-%d")
        to_date = datetime.strptime(request.POST["to_date"],"%Y-%m-%d")
        data = Parameter.objects.filter(current_datetime__gte = from_date, current_datetime__lte = to_date)
        return render(request, 'result.html', {'datetime_query': "datetime_query", 'a':data})
    return render(request, 'result.html')

def live_data(request):
   
    return render(request,"live_data.html")
    # a=cursor.execute(""" INSERT INTO   datachart_parameter(timestamp,time,Speed,Temperature,Voltage)VALUES (%s,%s,%s,%s,%s)""",[b,a,c,d,n])
# 
    # db.commit()
    # 
    # a=cursor.execute(""" INSERT INTO   datachart_parameter(current_datetime,time,Speed,Temperature,Voltage)VALUES (%s,%s,%s,%s,%s)""",[b,a,c,d,n])

    # db.commit() 
def get_live_data(request):

       #### return render(request, "line_chart.html")

        db = MySQLdb.connect("localhost","root","","chart_db")
        cursor= db.cursor()
  
        device = "COM6"
        try:
            print("Trying...", device)
            arduino = serial.Serial(device, 9600)

        except: 
            print ("Failed to connect on",device ) 
        while 1:
            time.sleep(1)
            data1 = arduino.readline()  # read the data from the arduino
            c = data1.decode("ASCII")

            data2 = arduino.readline()  # read the data from the arduino
            d = data2.decode("ASCII")

            data3 = arduino.readline()  # read the data from the arduino
            n = data3.decode("ASCII")

            zeit = (datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S"))
            datum = (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))

            a = str(zeit)
            b = str(datum)
            print(a)
            print(b)

            print(c)
            print(d)
            print(n)

            c = float(c)
            d = float(d)
            n = float(n)

            # a=cursor.execute(""" INSERT INTO   datachart_parameter(timestamp,time,Speed,Temperature,Voltage)VALUES (%s,%s,%s,%s,%s)""",[b,a,c,d,n])
            # db.commit()
          # import random
            data = {"speed":c, "temprature":d, "voltage":n}
            meta_data = {
                "data":
                [
                    {
                        "name": "speed",
                        "value":c
                    },
                    {
                        "name": "temprature",
                        "value":d 
                    },
                    {
                        "name": "voltage",
                        "value":n
                    }
                ]
            }
            return JsonResponse(meta_data)

           
  
    # except:
    #     meta_data = {
    #         "data":
    #         [
    #             {
    #                 "name": "speed",
    #                 "value":1
    #             }
    #         ]
        # }
     #   return JsonResponse(meta_data)

def get_live_line_chart(request):
    return render(request, "line_chart.html")
  
# Create your views here.


def show_data(request):

    #//c = request.GET.get('q3')
   # data= Parameter.objects.raw("SELECT  id,timestamp,time,Speed,Temperature,Voltage FROM datachart_parameter") 
    # data= Parameter.objects.all() 
    # data= Parameter.objects.all() 
    db = MySQLdb.connect("localhost","root","","chart_db")
    cursor= db.cursor()
    cursor.execute("SELECT * FROM datachart_parameter")
    data=cursor.fetchall()
    # 
    # print(data)
    return render(request, "data_show.html",{'data':data})

    