# encoding=utf-8
import requests
import csv
from bs4 import BeautifulSoup
import threading,time
from contextlib import closing
import urllib.request
import urllib


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


headers = {xxx}	


def csv_load(csv_load_url, file_name):
	# urllib模块下载方式直接下载文件
	# urllib.request.urlretrieve(csv_load_url,path)
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	res = urllib.request.Request(csv_load_url, headers=headers)

	f = urllib.request.urlopen(res) 
	data = f.read() 
	with open(path+file_name, "wb") as code:     
		code.write(data)

    # with open('./教育科技.csv', 'a+', encoding='utf-8') as f:
    #     writer = f.write(csv_load_url+'\n')

	# r = requests.get(csv_load_url, stream=True)
	# with open(path+file_name, 'wb') as f:
	# 	for data in r.iter_content(chunk_size=1024):
	# 		f.write(data)


def get_csv_load_url(csv_url):

	rs = requests.get(csv_url, headers=headers, verify=False)
	data = BeautifulSoup(rs.text, "lxml")
	# print(data)
	css = '#app > div.g-main.catalog-details > div.panel.panel-content > div > ul > li:nth-child(4) > table > tbody > tr'
	tr_list = select_css(1, data, css, '')
	print(len(tr_list))
	for x in range(1,len(tr_list)+1):
		css = '#app > div.g-main.catalog-details > div.panel.panel-content > div > ul > li:nth-child(4) > table > tbody > tr:nth-child('+str(x)+')' 
		csv_name  = select_css(3, data, css, 'fileformat')
		if 'csv' in csv_name:
			css = css + ' > td:nth-child(3) > a'
			id_InRc = select_css(3, data, css, 'id')
			file_name = select_css(2, data, css, '')
			# print(id_InRc)
			cata_Id = csv_url.split('catalog/')[1]
			csv_load_url = 'http://www.cddata.gov.cn/catalog/download?cataId=' + cata_Id + '&idInRc=' + id_InRc
			print(csv_load_url)
			csv_load(csv_load_url, file_name)
		pass


def get_csv_id(url):

	rs = requests.get(url, headers=headers, verify=False)
	data = BeautifulSoup(rs.text, "lxml")
	# print(data)
	css = '#app > div.g-main.catalog-list > div.right-content-catalog > div.bottom-content > ul > li'
	# #app > div.g-main.catalog-list > div.right-content-catalog > div.bottom-content > ul > li:nth-child(2) > div.cata-title > a
	li_list = select_css(1, data, css, '')
	for x in range(1,len(li_list)+1):
		css = '#app > div.g-main.catalog-list > div.right-content-catalog > div.bottom-content > ul > li:nth-child(' + str(x) + ') > div.cata-title > a'
		csv_url_ = select_css(3, data, css, 'href')

		print('第' + str(x) + '条' + csv_url_)

		csv_url = 'http://www.cddata.gov.cn' + csv_url_
		get_csv_load_url(csv_url)



path = './教育文化/'
# for x in range(1,281):
for x in range(1,10):

	print('第' + str(x) + '页')

	url = 'http://www.cddata.gov.cn/oportal/catalog/index?subjectId=sub-1&fileFormat=4&openType=1&page=' + str(x)
	# url = 'http://www.cddata.gov.cn/portal/catalog/index?domainId=domain-8&fileFormat=4&openType=1&page=' + str(x)

	get_csv_id(url)

	pass