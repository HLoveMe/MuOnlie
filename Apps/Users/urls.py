# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:2018/6/3 下午5:37
"""
from django.conf.urls import url

from Users.views import LoginView


urlpatterns = [
    url(r"login/$",LoginView.as_view(),name="login")
]