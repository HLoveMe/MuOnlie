"""
    author:ZZH
    git:HLoveMe
    date:2018/5/14 下午3:14
"""

from enum import Enum



class MessageStatus(Enum):
    Success = (1,"API请求成功")
    Fail = (-1,"API请求失败")


class APIResponseMessage(object):
    status = 0
    data = {}
    info = None

    def __init__(self,data,status = MessageStatus.Success,**kwargs):
        """
        :param data:  消息内容
        :param status: 请求状态
        :param kwargs: {info:解释文字}
        """
        value = status.value
        self.status = value[0]
        self.data = []
        info = kwargs.get("info",None)
        self.info = info if info is not None else (value[1] if value[0] == MessageStatus.Success.value[0] else MessageStatus.Fail.value[1])

    def __call__(self, *args, **kwargs):
        return []
