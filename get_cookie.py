from urllib import request
from http import cookiejar

def get(url):
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler=request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    response = opener.open(url)
    # 打印cookie信息
    #for item in cookie:
    #    print('Name = %s' % item.name)
    #    print('Value = %s' % item.value)
    #print(cookie)
    return cookie
#---------------------
