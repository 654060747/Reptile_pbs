import csv
import time
import os
from bs4 import BeautifulSoup
import requests
import codecs



# csv路径
csv_path = "./che.csv"
# 读取csv文件
csv_file = csv.reader(open(csv_path,'r',encoding='UTF-8'))

# 设置一个集合
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# xxx in data 判断xxx是否在集合中存在
# data = set()
# 循环文件所有内容http://www.haicj.com/carinfo.jsp?clxh=SVW7183MJi&typeid=2

headers = {
	
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "max-age=0",
	"Connection": "keep-alive",
	"Cookie": "JSESSIONID=3FA99C0F0B9142674B0C162B3B6E63D3; UM_distinctid=16caf506bc914-03929b60a4363e-5f123917-1fa400-16caf506bca293; CNZZDATA652138=cnzz_eid%3D1520979631-1566308780-%26ntime%3D1566308780",
	"Host": "www.haicj.com",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",

}

# 写 csv
def write_csv(data):
	file = "bbb.csv"

	with codecs.open(file,'a',encoding='utf-8') as f:
		f.write(data+"\n")
		f.close()

def get_haicj(url,xh,cjh):

	rs = requests.get(url, headers=headers, verify=False)
	rs.encoding = 'utf-8'

	data = BeautifulSoup(rs.text, "lxml")
	i = data.select("#carInfoBox > div.header > i")
	if len(i) > 0:

		string = i[0].getText().strip()
		data = string.split("（")[1].split("）")[0].split(" ")
		print("品牌::"+data[0])
		print("车系::"+data[1])
		cx_all = ""
		for x in range(2,len(data)):
			cx = data[x]
			cx_all = cx_all+cx+" "
		print("型号::"+cx_all)
		data = xh+","+cjh+","+data[0]+","+data[1]+","+cx_all
		write_csv(data)

	else:
		data = xh+","+cjh+","
		write_csv(data)



	


for line in csv_file:
	xh = line[0]
	print(xh)
	cjh = line[1]
	print(cjh)

	url = "http://www.haicj.com/carinfo.jsp?clxh="+xh+"&typeid=2"
	get_haicj(url,xh,cjh)

# get_haicj(url,"","")
	# print(data)
	# # 循环每一行集合数据
	# for su in data:
	# 	print(su)
	# # 清空集合
	# data.clear()