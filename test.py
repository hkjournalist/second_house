import requests
import get_cookie
import random_ip

url = 'https://bj.5i5j.com/ershoufang/b700e900h999l110q1r3/'
#cookie = get_cookie.get(url)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
         'Referer':url}


proxies_dict = random_ip.main()
#key=proxies_dict.keys()
print(proxies_dict['https'])
#html = requests.get(url,headers=headers,proxies = proxies_dict)
#print(html.text)