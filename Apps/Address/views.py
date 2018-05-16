
import json

from django.http import JsonResponse
from django.views.generic import View
from dss.Serializer import serializer

from .models import Country,Province,City,Town
from tools.APIMessage.JsonMessageResponse import JsonMessageResponse


class CountryView(View):
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        return  JsonMessageResponse.Success(Country.objects.all(),exclude_attr=["desc"])


class ProvincesView(View):
    """
        xx?c_id=1
    """
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        country = request.GET.get("c_id",-1)
        if country == -1 or len(country) == 0 or not isinstance(int(country), int):
            return JsonMessageResponse.Fail(info="请传递c_id参数表示国家id")
        return JsonMessageResponse(Province.objects.filter(country=country).all(), exclude_attr=["desc","country_id"])


class CitysView(View):
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        province = request.GET.get("p_id",-1)
        if province == -1 or len(province) == 0 or  not isinstance(int(province),int):
            return JsonMessageResponse.Fail(info="请传递p_id参数表示省份id")
        return JsonMessageResponse.Success(City.objects.filter(province=province).all(),exclude_attr=("province_id",))
