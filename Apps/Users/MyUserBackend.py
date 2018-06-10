# -*- coding:utf-8 -*-  
"""
    Author:Zzh
    Github:HLoveMe
    time:2018/6/10 下午3:13
"""

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.hashers import check_password

from Users.models import UserProfile


class HUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user and user.check_password(password):
                return user

        except Exception as e:

            return None
        pass



class DefaultUserBackend(object):
    def authenticate(self, request, username=None, password=None):
        name_va = settings.DEFAULT_USER_NAME == username
        pass_va = check_password(password,settings.DEFAULT_USER_PWD)
        if name_va and pass_va:
            try:
                user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            except Exception as e:
                user = UserProfile(username=username)
                setattr(user,"is_staff",True)
                setattr(user, "is_active", True)
                setattr(user, "is_superuser", True)
                setattr(user, "email", "1039194460@qq.com")
                user.save()

            return user
        return  None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None