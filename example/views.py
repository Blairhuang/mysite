from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import *
import sys, os
from bs4 import BeautifulSoup
import requests
import math
from .forms import numberForm
import random as r
# Create your views here.

def example_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def example_post(request):
    log = []
    if request.method == "POST":
        try:
            data = request.POST["data"]
            return JsonResponse({"test":data})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
@csrf_exempt
def example_post1(request):
    jsob = {'demo':'12345',"var":"The count is "}
    log = []
    if request.method == "POST":
        try:
            
            data = request.POST['data']
            received = json.loads(str(data))

            jsob.update(received)

            index = 0
            for i in json['demo']:
                index += -1
                #index = jsob['var']+str(index) ///key + value
            return JsonResponse({"count":index})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")

@csrf_exempt #每一个function 之前都要加 作为security  number
def fib(request):
    jsob = {'startnumber':0,"length":10} #keynumber: value 1
    log = []
    if request.method == "POST":
        try:
            
            data = request.POST['data']
            received = json.loads(str(data))
            jsob.update(received)
#begin function 前面都一样 copy----CUSTOM FUNCTION BELOW 

            startnumber = int(jsob['startnumber'])
            length = int(jsob['length']) #确保所有输入 转化为integers //fibnumbers--loop range
            loop = range(length) #CREATE LISTS OF NUMBER 0.1.2.3.4.5.6.7.8.9.10

            numarray = [] 

            fibno = startnumber #斐波那契一定要两个数字 0+1 1+2
            addno = 1 #每一个数字都要加1 成为新的数字

            for i in loop:
                numarray.append(fibno)
                fibno = fibno+addno
                addno = fibno-addno

            return JsonResponse({"fib":numarray}) #fib = number dictinoary 

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return JsonResponse(jsob)


@csrf_exempt #每一个function 之前都要加 作为security  number
def addSine(request):
    jsob = {'startloop':0,"length":10} #keynumber: value 1
    log = []
    if request.method == "POST":
        try:      
            data = request.POST['data']
            received = json.loads(str(data))
            jsob.update(received)
###############
            startloop = int(jsob['startloop'])
            length = int(jsob['length']) #确保所有输入 转化为integers //fibnumbers--loop range
            
            Z = []
            for i in range(length):
                Z = math.sin(i)
                               
            return HttpResponse(Z)
                #JsonResponse({"Curve_location":Z})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return JsonResponse(jsob)

@csrf_exempt #每一个function 之前都要加 作为security  number
def pointlist(request):
    jsob = {'range':10} #keynumber: value 1
    log = []
    if request.method == "POST":
        try:
            
            data = request.POST['data']
            received = json.loads(str(data))
            jsob.update(received)
#begin function 前面都一样 copy----CUSTOM FUNCTION BELOW 

            length = int(jsob['range'])
            loop = range(length)

            A=[]

            for i in loop:
                for j in loop:
                    if i%2 == 0 and  j%2 !=0:
                        A.append((i,j))

            return HttpResponse(A) #fib = number dictinoary 

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return JsonResponse(jsob)
                



@csrf_exempt
def get(request, city):
    Host = "https://en.wikipedia.org/wiki/" + str(city)
    Request = requests.get(Host)
    soup = BeautifulSoup(Request.content, 'html.parser')

    Latitude = soup.find(class_='latitude')
    Longitude = soup.find(class_='longitude')

    Lat_input = Latitude.get_text()
    Long_input = Longitude.get_text()

    longOG = Long_input
    longA = longOG.split("°")[0].split('′')
    longB = longOG.split('°')[1].split('′')[0]
    longC = longOG.split('°')[1].split('′')[0]
    longD = longOG.split('°')[1].split('′')[1]

    longA = float(longA[0])/1
    longB = float(longB[0])/60

    if longC.isdigit():
        longC = float(longC[0])/3600
    else:
        longC = 0
    if longD == 'W':
        longA = longA*(-1)
    else:
        longA = longA
    
    latOG = Lat_input
    latA = latOG.split("°")[0].split('′')
    latB = latOG.split('°')[1].split('′')[0]
    latC = latOG.split('°')[1].split('′')[0]
    latD = latOG.split('°')[1].split('′')[1]

    latA = float(latA[0])/1
    latB = float(latB[0])/60

    try:
        latC = float(latC[0])/3600
    except ValueError:
        latC == 0
    
    if latD =='S':
        latA = latA*(-1)
    else:
        latA = latA

    lon = str(longA+longB+longC)
    lat = str(latA+latB+latC)

    return HttpResponse('latitude: '+str(lat)+' longtitude: '+str(lon))


import math 

@csrf_exempt #每一个function 之前都要加 作为security  number
def curve(request):
    jsob = {'r':170,"gens":1870,'a':-15,'d':-15,'c':1,'b':1} #keynumber: value 1
    log = []
    if request.method == "POST":
        try:
            
            data = request.POST['data']
            received = json.loads(str(data))
            jsob.update(received)

            r = int(jsob['r'])
            gens = int(jsob['gens'])
            a  = int(jsob['a'])
            d  = int(jsob['d'])
            c  = int(jsob['c'])
            b  = int(jsob['b'])

            points=[]

            for i in range(int(gens)):
                f=r*math.sin(a*i/r)

                g=r*math.cos(b*i/r)

                h=r*math.sin(c*i/r)

                j=r*math.cos(d*i/r)

                #point1=[r*math.sin(a*i/r),r*math.cos(b*i/r),0]

                #point2=[r*math.sin(c*i/r),r*math.cos(d*i/r),0]

                Dis=math.sqrt(((h-f)*(h-f)+(j-g)*(j-g)))

                #point3=[0.5*r*math.sin(a*i/r)+0.5*r*math.sin(c*i/r),0.5*r*math.cos(b*i/r)+0.5*r*math.cos(d*i/r),Dis]

                x = 0.5*r*math.sin(a*i/r)+0.5*r*math.sin(c*i/r)
                y = 0.5*r*math.cos(b*i/r)+0.5*r*math.cos(d*i/r)
                z = Dis
                
                
                points.append((x,y,z))            

            return HttpResponse(points)  #JsonResponse({'curve_point':points})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return JsonResponse(jsob)  

def number(requests):
    jsob = {'r':170,"gens":1870,'a':-15,'d':-15,'c':1,'b':1} #keynumber: value 1
    log = []
    if requests.method == "POST":
        try:
            
            data = requests.POST['data']
            received = json.loads(str(data))
            jsob.update(received)

            r = int(jsob['r'])
            gens = int(jsob['gens'])
            a  = int(jsob['a'])
            d  = int(jsob['d'])
            c  = int(jsob['c'])
            b  = int(jsob['b'])

            points=[]

            for i in range(int(gens)):
                f=r*math.sin(a*i/r)

                g=r*math.cos(b*i/r)

                h=r*math.sin(c*i/r)

                j=r*math.cos(d*i/r)

                #point1=[r*math.sin(a*i/r),r*math.cos(b*i/r),0]

                #point2=[r*math.sin(c*i/r),r*math.cos(d*i/r),0]

                Dis=math.sqrt(((h-f)*(h-f)+(j-g)*(j-g)))

                #point3=[0.5*r*math.sin(a*i/r)+0.5*r*math.sin(c*i/r),0.5*r*math.cos(b*i/r)+0.5*r*math.cos(d*i/r),Dis]

                x = 0.5*r*math.sin(a*i/r)+0.5*r*math.sin(c*i/r)
                y = 0.5*r*math.cos(b*i/r)+0.5*r*math.cos(d*i/r)
                z = Dis
                
                
                points.append((x,y,z))            

            return render(requests,'number.html')  #JsonResponse({'curve_point':points})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return JsonResponse(jsob)








