"""MuOnlie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.views.generic import TemplateView


import xadmin
from Address.urls import urlpatterns as AddressURLs
# from LocalData.citys.citysInserts import loadCitysAndInserts

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r"^$",TemplateView.as_view(template_name="index.html"),name="home"),
    url(r"^index/$",TemplateView.as_view(template_name="index.html"),name="home"),
    #登入注册
    url(r"^",include("Users.urls")),



    url(r'^address/',include(AddressURLs)),
    # url(r"^insertcitys/$", lambda a: JsonResponse(loadCitysAndInserts()), name="citysinsert"),

]

