
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        return redirect("/")
        pass

