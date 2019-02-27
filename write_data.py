import csv
import codecs

def write(data,csv_name):
    keys=data.keys()
    #print(keys)
    try:

        with codecs.open(str(csv_name)+'.csv', 'a+','utf_8_sig') as f:#防止在向csv写入数据时发生utf-8乱码问题
          writer = csv.DictWriter(f,fieldnames=keys)
          #writer.writeheader()

          #decode('utf-8')表示把utf-8编码转换为unicode编码；encode('utf-8')表示把unicode编码转换为utf-8编码
          writer.writerow(data)

    except:print('write_error')