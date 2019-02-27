import requests
import re


def baidu_to_google(lat0,long0):
        #百度坐标转谷歌坐标,经度在前，纬度在后
        result = requests.get('http://api.map.baidu.com/geoconv/v1/'
                              '?coords='+str(long0)+','+str(lat0)+
                              '&from=5&to=3&'
                              'ak=ynyM0yQLspIeWf7Fdw39GMZka1BPFq2d')

        tmp = re.findall('"x":(.*?),"y":(.*?)}',result.text,re.S)
        tmp=tmp[0]

        #纬度
        lat = tmp[1]

        #经度
        long = tmp[0]

        return(lat,long)
        #print(lat,long)