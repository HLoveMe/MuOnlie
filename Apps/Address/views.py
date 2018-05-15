
import json


from .models import Country,Province,City,Town
from tools.APIMessage.JSONMessage import  APIResponseMessage,MessageStatus
from django.views.generic import View,DetailView,ListView,TemplateView
from dss.Serializer import serializer
from dss.Mixin import JsonResponseMixin,MultipleJsonResponseMixin


class CountryView(MultipleJsonResponseMixin,ListView):
    model = Country
    paginate_by = 10
    datetime_type = 'string'

def getCountrys(request):
    pass

def getProvinces(requests):

    pass
