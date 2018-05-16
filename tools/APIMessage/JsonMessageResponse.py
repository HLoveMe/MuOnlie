"""
    author:ZZH
    git:HLoveMe
    date:2018/5/16 下午4:30
"""

from django.http import JsonResponse
from dss.Serializer import serializer

from .JSONMessage import APIResponseMessage,MessageStatus,SuccessStatus,ErrorStatus,FailStatus


class JsonMessageResponse(JsonResponse):

    @classmethod
    def Success(cls,*args,**kwargs):
        return cls((args[0] if len(args) >= 1 else {}),status=SuccessStatus,**kwargs)

    @classmethod
    def Error(cls,*args,**kwargs):
        return cls(args[0] if len(args) >= 1 else {},status=ErrorStatus,  **kwargs)

    @classmethod
    def Fail(cls,*args,**kwargs):
        return cls(args[0] if len(args) >= 1 else {},status=FailStatus, **kwargs)

    def __init__(self, data,status = SuccessStatus ,**kwargs):
        """
        :param data:查询的数据
        :param status: 状态
        :param kwargs: {
            info:表示该请求的状态
            ...serializer的参数
        }
        """
        info = kwargs.get("info",None)
        _status = status
        if info is not None:
            _status = MessageStatus(status.status,info)
        message = APIResponseMessage(serializer(data,**kwargs),status=_status)
        super(JsonMessageResponse,self).__init__(message(),safe=False)

