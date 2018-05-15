"""
    author:ZZH
    git:HLoveMe
    date:2018/5/14 下午1:49
"""

from django.conf.urls import url
from .views import getCountrys,getProvinces,CountryView

urlpatterns = [
    url(r"^countrys/$",CountryView.as_view(),name="getCountrys"),
    url(r"^provinces/$",getProvinces,name="getProvinces")
]