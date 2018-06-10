
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):

        return redirect("/")
        pass


class OutLoginView(TemplateView):

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        p = request.user.has_perm("Users.aaa")
        logout(request)
        return redirect("/")

