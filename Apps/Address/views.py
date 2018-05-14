from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Country,Province,City,Town
from tools.APIMessage.JSONMessage import  APIResponseMessage,MessageStatus

class Animation(object):
    type = "Animation"
    pass



def getCountrys(request):
    return JsonResponse()

def getProvinces(requests):
    try:
        c_id = int(requests.GET.get("country",[]).pop())

    except IndexError as err:
        return JsonResponse({})

    return JsonResponse({})
    pass
