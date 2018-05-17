"""
    author:ZZH
    git:HLoveMe
    date:2018/5/17 下午4:24
"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"success!"]