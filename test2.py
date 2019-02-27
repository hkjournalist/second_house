import requests
import re




url_0 = "https://bj.5i5j.com/ershoufang/b700e900h999l110q1/"
######我爱我家/二手房/700万—900万/999平米-110平米/普通住房

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
         'Referer':'https://bj.5i5j.com/ershoufang/b700e900h999l110q'}
#我爱我家的反爬虫就在Referer里面
html = requests.get(url_0,headers = headers)
url_1s=re.findall('<div class="listImg"><a href="/ershoufang/(.*?).html"',html.text,re.S)
print(url_1s)
url_1 = 'https://bj.5i5j.com/ershoufang/'+url_1s[0]+'.html'
html2 = requests.get(url_1).text
x = re.findall('var community_x = "(.*?)";//获取小区x坐标地址',html2,re.S)
y = re.findall('var community_y = "(.*?)";//获取小区Y坐标地址',html2,re.S)
print(x,y)