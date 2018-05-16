
import json

from .models import Country,Province,City,Town
from django.views.generic import View
from dss.Serializer import serializer
from django.http import JsonResponse


class CountryView(View):
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        return JsonResponse(serializer(Country.objects.all()),safe=False)


class ProvincesView(View):
    """
        xx?c_id=1
    """
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        country = request.GET.get("c_id",-1)
        if country == -1 or len(country) == 0 or not isinstance(int(country), int):
            return JsonResponse({"info":"请传递c_id参数表示国家id"})
        return JsonResponse(serializer(Province.objects.filter(country=country).all(),exclude_attr=("country_id",)),safe=False)
        pass


class CitysView(View):
    http_method_names = ["get"]

    def get(self,request, *args, **kwargs):
        province = request.GET.get("p_id",-1)
        if province == -1 or len(province) == 0 or  not isinstance(int(province),int):
            return JsonResponse({"info":"请传递p_id参数表示省份"})

        return JsonResponse(serializer(City.objects.filter(province=province).all(),exclude_attr=("province_id",)),safe=False)
