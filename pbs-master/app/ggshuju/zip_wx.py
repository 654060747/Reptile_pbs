# encoding=utf-8
import requests,csv,json,os
from bs4 import BeautifulSoup


def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


def csv_load(csv_load_url, is_xls, file_name,csv_lx):

	headers = {xxx}

	r = requests.get(csv_load_url, headers=headers, stream=True)
	with open('./'+csv_lx+'/'+is_xls+"-"+file_name+".zip", 'wb') as f:
		for data in r.iter_content(chunk_size=1024):
			f.write(data)


def get_csv_load_url(csv_url,csv_lx):


	rs = requests.get(csv_url)
	data_json = json.loads(rs.text)
	data_json = data_json["data"]
	# print(data_json)
	for x in data_json:

		is_xls = x["fileName"]
		print(is_xls)
		if 'csv' in is_xls:
			file_id = x['fileId']
			print(file_id)
			# http://data.wuxi.gov.cn/data/catalog/CatalogDetailDownload.do?method=getFileDownloadAddr&fileId=0bb938778fc144038c87c299fca20d4c
			xls_url = 'http://data.wuxi.gov.cn/data/catalog/CatalogDetailDownload.do?method=getFileDownloadAddr&fileId='+file_id
			csv_load(xls_url,is_xls,file_id,csv_lx)			


# csv路径
csv_path = "./resId.csv"
# 读取csv文件
csv_file = csv.reader(open(csv_path,'r'))
i = 0
for urls in csv_file:	
	i = i+1
	# 循环每一行内容
	for url_one in urls:
		print('第'+str(i)+'条')
		print("======================"+url_one)

		rs = requests.get('http://data.wuxi.gov.cn/data/catalog/catalogDetail.htm?cata_id='+url_one)
		rs.encoding = 'utf-8'
		data = BeautifulSoup(rs.text, "lxml")
		csv_lx = data.select('body > div:nth-child(12) > div.od-main > div.data-content > div > div.left-cont > div.baseInfo.s1 > table > tr:nth-child(2) > td:nth-child(2)')[0].getText().strip()
		# print(csv_lx)
		CheckDir(csv_lx)	
		url = 'http://data.wuxi.gov.cn/data/catalog/CatalogDetail.do?method=getDownLoadPageInfo&cata_id='+url_one+'&file_typs=1&keywords='
		get_csv_load_url(url,csv_lx)