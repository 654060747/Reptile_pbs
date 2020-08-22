# encoding=utf-8
import requests
import csv,json
from bs4 import BeautifulSoup
import threading,time
from contextlib import closing
import urllib.request
import urllib




def csv_load(csv_load_url, file_name):
	# urllib模块下载方式直接下载文件
	# urllib.request.urlretrieve(csv_load_url,path)
	# res = urllib.request.Request(csv_load_url, headers=headers)

	# f = urllib.request.urlopen(res) 
	# data = f.read() 
	# with open(path+file_name+".zip", "wb") as code:     
	# 	code.write(data)

	headers = {xxx}

	r = requests.get(csv_load_url, headers=headers, stream=True)
	with open(path+file_name+".zip", 'wb') as f:
		for data in r.iter_content(chunk_size=1024):
			f.write(data)


def get_csv_load_url(csv_url):

	headers = {xxx}

	data = {
		"draw": "1",
		"columns[0][data]": "fileName",
		"columns[0][name]": "",
		"columns[0][searchable]": "true",
		"columns[0][orderable]": "false",
		"columns[0][search][value]": "",
		"columns[0][search][regex]": "false",
		"columns[1][data]": "formattedFileSize",
		"columns[1][name]": "",
		"columns[1][searchable]": "true",
		"columns[1][orderable]": "false",
		"columns[1][search][value]": "",
		"columns[1][search][regex]": "false",
		"columns[2][data]": "updateTime",
		"columns[2][name]": "",
		"columns[2][searchable]": "true",
		"columns[2][orderable]": "false",
		"columns[2][search][value]": "",
		"columns[2][search][regex]": "false",
		"columns[3][data]": "fileId",
		"columns[3][name]": "",
		"columns[3][searchable]": "true",
		"columns[3][orderable]": "false",
		"columns[3][search][value]": "",
		"columns[3][search][regex]": "false",
		"order[0][column]": "0",
		"order[0][dir]": "asc",
		"start": "0",
		"length": "10",
		"search[value]": "",
		"search[regex]": "false",
	}

	rs = requests.post(csv_url, data, headers=headers)
	# print(rs.status_code)
	# data = BeautifulSoup(rs.text, "lxml")
	data_json = json.loads(rs.text)
	# print(data_json)
	file_id = data_json["data"][0]["fileId"]
	# print(file_id)
	file_name = data_json["data"][0]["fileName"].split("_csv")[0]
	print(file_name)

	url = "http://data.harbin.gov.cn/odweb/catalog/CatalogDetailDownload.do?method=getFileDownloadAddr&fileId=" + file_id

	csv_load(url, file_name)



path = "./财税金融/"


id_list = [数据id]

for x in id_list:
	print(x)
	# xxxx哈尔滨URL
	get_csv_load_url('http://data.harbin.gov.cn/odweb/catalog/CatalogDetail.do?method=getDownLoadPageInfo&cata_id='+str(x)+'&file_typs=1&keywords=csv')