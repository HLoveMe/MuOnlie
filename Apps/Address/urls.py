"""
    author:ZZH
    git:HLoveMe
    date:2018/5/14 下午1:49
"""

from django.conf.urls import url
from .views import CountryView,ProvincesView,CitysView

urlpatterns = [
    url(r"^countrys/$",CountryView.as_view(),name="getCountrys"),
    url(r"^provinces/$",ProvincesView.as_view(),name="getProvinces"),
    url(r"^citys/$",CitysView.as_view(),name="getcitys"),
]