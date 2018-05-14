# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
"""
import json,os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"citys.json")
from Apps.Address.models import Country,Province,City,Town,Village

def loadCitysAndInserts():
    Country.objects.all().delete()
    Province.objects.all().delete()
    City.objects.all().delete()
    Town.objects.all().delete()
    Village.objects.all().delete()
    # 国家
    country = Country.objects.create(name="China")
    country.save()
    with open(path, "rb") as file:
        data = json.load(file)
        provinces = data["provinces"]
        for province in provinces:

            _province = Province.objects.create(name=province["provinceName"],country=country)
            # 城市provinceName
            _province.save()
            citys = province["citys"]
            for city in citys:
                _city = City.objects.create(name=city["citysName"],province=_province)
                _city.save()
                pass
        return data
    pass


