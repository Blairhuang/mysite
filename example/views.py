from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import *

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
            jsob = json.loads(data)
            # or 代替---received = json.loads(data)
            #jsob.update(reveived) 将received 连入jsob 
            index = 0
            for i in json['demo']:
                index += -1
                #index = jsob['var']+str(index) ///key + value
            return JsonResponse({"log":log})
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")