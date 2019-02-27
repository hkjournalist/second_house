import requests
import re
import write_data #数据写入csv
import time
import baidu_to_google #百度坐标转谷歌坐标
import random_ip
import get_cookie
import random

headers = {}
url_0 = ''
csv_name = '11'
proxys_list = random_ip.get_proxys(1)
#print(proxys_list)

def spider(price,square,room_num):
    #url_0 = "https://bj.5i5j.com/ershoufang/b700e900h999l110q1/"
    a = price[0]
    b = price[1]
    global url_0
    url_0 = "https://bj.5i5j.com/ershoufang/b"+a+"e"+b+\
            "h999l"+square+"q1"+room_num
    #print(url_0)

    global headers
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
             'Referer':url_0}
             #'Cookie':'morCon=open; _pzfxuvpc=1475049475865%7C8446215284802640340%7C6%7C1475049670649%7C1%7C%7C8242877926752885613; yfx_c_g_u_id_10000001=_ck18070722150010416771754551687; yfx_f_l_v_t_10000001=f_t_1530972900026__r_t_1540442170253__v_t_1540481976668__r_c_16; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1540398908,1540402832,1540438154,1540456575; _ga=GA1.2.1559820043.1475049489; yfx_c_g_u_id_10000079=_ck18070722443218951475317413725; yfx_f_l_v_t_10000079=f_t_1530974672888__r_t_1530974672888__v_t_1530974672888__r_c_0; _Jo0OQK=6E9C31DB6A2862DC1C95C95AFA2BBB80485F29D5D1A5F6D9B570119BFD1E5306E02BDD3425ABF50A67A249B2B1A003878E0C7AAB13E51AD6A123AA77CF4E000A8B924E69D7AC460EFE6409CA2DE14625AE1A5453455108E9D1EC7AAB13E51AD6A124176BEAF053CC5ACAA52C66EA7B0B0A6GJ1Z1Iw==; yfx_mr_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; yfx_key_10000001=%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6; ershoufang_cookiekey=%5B%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E6%2525AC%2525A7%2525E9%252599%252586%2525E7%2525BB%25258F%2525E5%252585%2525B8%253Fzn%253D%2525E6%2525AC%2525A7%2525E9%252599%252586%2525E7%2525BB%25258F%2525E5%252585%2525B8%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E6%25AC%25A7%25E9%2599%2586%25E7%25BB%258F%25E5%2585%25B8%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E7%25258F%2525A0%2525E6%2525B1%25259F%2525E7%2525BD%252597%2525E9%2525A9%2525AC%253Fzn%253D%2525E7%25258F%2525A0%2525E6%2525B1%25259F%2525E7%2525BD%252597%2525E9%2525A9%2525AC%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E7%258F%25A0%25E6%25B1%259F%25E7%25BD%2597%25E9%25A9%25AC%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E6%2525B3%2525BD%2525E4%2525B8%2525B0%2525E8%25258B%252591%253Fzn%253D%2525E6%2525B3%2525BD%2525E4%2525B8%2525B0%2525E8%25258B%252591%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E6%25B3%25BD%25E4%25B8%25B0%25E8%258B%2591%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E5%25258D%252583%2525E9%2525B9%2525A4%2525E5%2525AE%2525B6%2525E5%25259B%2525AD%253Fzn%253D%2525E5%25258D%252583%2525E9%2525B9%2525A4%2525E5%2525AE%2525B6%2525E5%25259B%2525AD%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E5%258D%2583%25E9%25B9%25A4%25E5%25AE%25B6%25E5%259B%25AD%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252Fsubway%252Fss231%253Fzn%253D%25E8%258F%259C%25E5%25B8%2582%25E5%258F%25A3%2522%252C%2522x%2522%253A%2522116.380518%2522%252C%2522y%2522%253A%252239.895352%2522%252C%2522name%2522%253A%2522%25E8%258F%259C%25E5%25B8%2582%25E5%258F%25A3%2522%252C%2522total%2522%253A7%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E7%2525BD%252597%2525E9%2525A9%2525AC%2525E8%25258A%2525B1%2525E5%25259B%2525AD%253Fzn%253D%2525E7%2525BD%252597%2525E9%2525A9%2525AC%2525E8%25258A%2525B1%2525E5%25259B%2525AD%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E7%25BD%2597%25E9%25A9%25AC%25E8%258A%25B1%25E5%259B%25AD%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E5%25258D%252583%2525E9%2525B9%2525A4%2525E5%2525AE%2525B6%2525E5%25259B%2525AD%253Fzn%253D%25E5%258D%2583%25E9%25B9%25A4%25E5%25AE%25B6%25E5%259B%25AD%252F%2526searchtype%253D3%2522%252C%2522x%2522%253A%2522116.4261%2522%252C%2522y%2522%253A%252239.99351%2522%252C%2522name%2522%253A%2522%25E5%258D%2583%25E9%25B9%25A4%25E5%25AE%25B6%25E5%259B%25AD%2522%252C%2522total%2522%253Anull%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E5%252585%2525AC%2525E5%25259B%2525AD5%2525E5%25258F%2525B7%253Fzn%253D%2525E5%252585%2525AC%2525E5%25259B%2525AD5%2525E5%25258F%2525B7%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E5%2585%25AC%25E5%259B%25AD5%25E5%258F%25B7%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E5%25259B%2525BD%2525E8%2525B4%2525B8%253Fzn%253D%2525E5%25259B%2525BD%2525E8%2525B4%2525B8%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E5%259B%25BD%25E8%25B4%25B8%2522%252C%2522total%2522%253A%25220%2522%257D%22%2C%22%257B%2522url%2522%253A%2522%252Fershoufang%252F_%2525E7%25258E%2525B0%2525E4%2525BB%2525A3%2525E5%25259F%25258E%253Fzn%253D%2525E7%25258E%2525B0%2525E4%2525BB%2525A3%2525E5%25259F%25258E%2522%252C%2522x%2522%253A%25220%2522%252C%2522y%2522%253A%25220%2522%252C%2522name%2522%253A%2522%25E7%258E%25B0%25E4%25BB%25A3%25E5%259F%258E%2522%252C%2522total%2522%253A%25220%2522%257D%22%5D; ershoufang_BROWSES=41228093%2C41505119%2C41115929%2C41117597%2C41331497%2C41213264%2C37115758%2C41117422%2C35764267%2C40561629%2C40268755%2C37585774%2C41341954%2C40028286%2C39395123%2C40394659%2C39728332%2C38829821%2C41441196%2C40109826%2C37860907%2C41454906%2C40069808%2C41477729%2C40805089%2C40636024%2C41254015%2C41174968%2C41278831%2C39438725%2C41066529%2C32537999%2C40369960%2C41101239%2C40276993%2C37988235%2C40884306%2C41652129%2C40484475%2C41117970%2C37432717%2C39976201%2C40093411%2C38915504%2C41090821%2C37603266%2C40990399%2C37966774%2C40318629%2C39166013%2C39250498%2C41533332%2C40914558%2C38289330%2C38714814%2C40908668%2C38585066%2C41175675%2C40179165%2C37471236%2C39720149%2C40882804%2C39732922%2C39632786%2C38989177%2C38632042%2C40103715%2C39546889%2C39502635%2C37721597%2C39891954%2C41438979%2C41113262%2C41138967%2C41624373%2C41550864%2C41487207%2C40808111%2C38572501%2C38012390%2C38546745%2C41045367%2C37760082%2C41583375%2C37708916%2C41170282%2C40967030%2C36415403%2C40712634%2C39188071%2C38361560%2C41439337%2C41242310%2C41450866%2C41224771%2C40255962%2C41178957%2C41484396%2C40623472%2C40944882%2C40983915%2C39909979%2C36250734%2C34524142%2C41558742%2C38210598%2C40978048%2C40724801%2C38374443%2C40588293%2C40408968%2C40634822%2C41484638%2C41366090%2C41579168%2C38879892%2C38652054%2C39170561%2C41258968%2C38967420%2C40539267%2C41153878%2C41167840%2C40376596%2C40945797%2C37947345%2C41705435%2C40350381%2C41445862; yfx_s_u_id_10000001=4555218; yfx_s_u_name_10000001=oRms1swtzC2HijgFasAoUFf_TCck; yfx_mr_f_n_10000001=baidu%3A%3Amarket_type_ppzq%3A%3A%3A%3Abaidu_ppc%3A%3A%25e6%2588%2591%25e7%2588%25b1%25e6%2588%2591%25e5%25ae%25b6%3A%3A%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3Awww.baidu.com%3A%3A%3A%3A%3A%3A%25E5%25B7%25A6%25E4%25BE%25A7%25E6%25A0%2587%25E9%25A2%2598%3A%3A%25E6%25A0%2587%25E9%25A2%2598%3A%3A160%3A%3Apmf_from_adv%3A%3Abj.5i5j.com%2F; _gid=GA1.2.715690226.1540398912; PHPSESSID=grsumbq9qja9dk59kke56700ud; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1540483666; domain=bj'}

    ######我爱我家/二手房/700万—900万/999平米-110平米/普通住房/三居室

    cookie(url_0)

    proxys_dict = choice_ip()
    html = requests.get(url_0,headers = headers,proxies = proxys_dict)
    #print(html.text)
    #print(html.text)
    #next_page=re.findall('class="cPage">(.*?)</a><a href="',html.text,re.S)

    print(html.text)
    page_num = 0
    #print(html.text.find('下一页'))
    page_flag=html.text.find('下一页')
    while(page_flag!=-1):#不止一页
        page_num = page_num+1
        print('第',page_num,'页开始抓取于',time.asctime( time.localtime(time.time()) ))
        page_flag=spider_0(page_num)
        print('第',page_num,'页抓取完成于',time.asctime( time.localtime(time.time()) ))

    print('抓取完成，共计抓取'+str(page_num)+'页数据',time.asctime( time.localtime(time.time()) ))

def cookie(url):
    cookie = get_cookie.get(url)
    cookies=''
    for item in cookie:
        cookies=cookies+item.name+'='+item.value+';'

    global headers
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
             'Referer':url,
             'Cookie':cookies}


def choice_ip():
    #初始化正则表达式
    lose_time, waste_time = random_ip.initpattern()
    #print(proxys_list)
    #如果平均时间超过200ms重新选取ip
    while True:
          #若ip池为空
          global proxys_list
          if len(proxys_list)==0:
              #构建ip池
              proxys_list=random_ip.get_proxys(1)
          #print(proxys_list)
          #从100个IP中随机选取一个IP作为代理进行访问
          proxy = random.choice(proxys_list)
          split_proxy = proxy.split('#')
          #获取IP
          ip = split_proxy[1]
          #检查ip
          average_time = random_ip.check_ip(ip, lose_time, waste_time)
          if average_time > 200:
              #去掉不能使用的IP
              proxys_list.remove(proxy)
              #print("ip连接超时, 重新获取中!")
          if average_time < 200:
              break

    #去掉已经使用的IP

    proxys_list.remove(proxy)
    proxy_dict = {split_proxy[0]:split_proxy[1] + ':' + split_proxy[2]}
    #print("使用代理:", proxy_dict)
    print('开始使用ip：',proxy_dict)
    return proxy_dict

def spider_0(page_num):
    proxy_dict = choice_ip()
    #print(html.cookies.get_dict())
    #print(proxy_dict)
    html = requests.get(url_0+'n'+str(page_num),headers = headers,proxies=proxy_dict)
    #print((url_0+'n'+str(page_num)))
    #print(html.text)
    url_1s=re.findall('<div class="listImg"><a href="/ershoufang/(.*?).html"',html.text,re.S)
    #print(url_1s)
    page_flag=html.text.find('下一页')
    for each in url_1s:
      try:
        time.sleep(0.1)
        spider_1(each,proxy_dict)
      except:print('第',page_num,'页','编号',each,'错误')
    #print(page_flag)
    return page_flag


def spider_1(each_url,proxy_dict):
    #each_url = url_1s[0]
    url_1 = 'https://bj.5i5j.com/ershoufang/'+each_url+'.html'

    html2 = requests.get(url_1,headers=headers,proxies = proxy_dict).text

    #经度
    x = re.findall('var community_x = "(.*?)";//获取小区x坐标地址',html2,re.S)

    #纬度
    y = re.findall('var community_y = "(.*?)";//获取小区Y坐标地址',html2,re.S)

    yx = baidu_to_google.baidu_to_google(y[0],x[0])
    #坐标转换，纬度在前，经度在后
    #print(yx)


    id = re.findall('房源ID：(.*?)</p>',html2,re.S)
    house_tit = re.findall('<h1 class="house-tit">(.*?)</h1>',html2,re.S)

    #square = re.findall('<li><label>房屋户型</label><span>(.*?)</span></li><li><label>建筑面积</label><span>(.*?)</span>',html2,re.S)
    total_price = re.findall('<p class="jlinfo">(.*?)</p>',html2,re.S)
    #average_price = re.findall('',html2,re.S)
    #build_time = re.findall('',html2,re.S)

    #总价，id，简介，坐标
    data = {'total_price':total_price[0],
    'id':id[0],
    'tit':house_tit[0],
    'x':yx[1],'y':yx[0]}

    info = ['房屋户型','所在楼层','建筑面积','供暖方式','挂牌时间','建筑年代']
    for each in info:
       try:
           detail0 = re.findall('<li><label>'+each+'</label><span>(.*?)</span></li>',html2,re.S)
           detail =detail0[0]
       except:
           detail = ''
       data[each]=detail


    #print(data,'写入')
    write_data.write(data,csv_name)

