"""
    author:ZZH
    git:HLoveMe
    date:2018/5/14 下午2:34
"""

from django.db import models
from django.db.models.query import QuerySet


def extraJson(model,*args,**kwargs):
    return dict([(fieldName,getattr(model,fieldName)) for fieldName in [f.name for f in model._meta.fields]])


def toJSON(source):
    if isinstance(source,QuerySet):
        return [extraJson(one) for one in source]
    elif isinstance(source,models.Model):
        return source.extraJson()
    elif source is dict:
        return source
    elif source is list:
        return source
    elif isinstance(source,object):
        return dict([(_key,getattr(source,_key,None)) for _key in [key for key in dir(source) if not (key.endswith("__") and key.startswith("__"))]]);

    pass

