"""
    author:ZZH
    git:HLoveMe
    date:2018/5/14 下午3:14
"""



class MessageStatus(object):
    status = -999
    info = ""

    def __init__(self,status,info):
        self.status = status
        self.info = info
        super(MessageStatus,self).__init__()


SuccessStatus = MessageStatus(1,"API请求成功")
FailStatus = MessageStatus(-1,"API请求失败")
ErrorStatus = MessageStatus(0,"服务器错误")


class APIResponseMessage(object):
    status = 0
    data = None
    info = None

    def __init__(self,data,status = SuccessStatus,**kwargs):
        """
        :param data:  消息内容
        :param status: 请求状态
        :param kwargs: {info:解释文字 替换MessageStatus 默认解释}
        """

        self.status = status
        self.data = data
        self.info = kwargs.get("info",None)

    def __call__(self, *args, **kwargs):
        return {
            "data": self.data,
            "status": self.status.status,
            "info": self.status.info if self.info is None else self.info
        }


def Message(data,status=SuccessStatus,**kwargs):
    """
    JsonResponse(Message(serializer(Country.objects.all())),safe=False)
    :param data:
    :param status:
    :param kwargs: {info:xx}
    :return:
    """
    return APIResponseMessage(data,status=status,**kwargs)()