# encoding=utf-8
import requests,csv,json,os
from bs4 import BeautifulSoup

def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


def csv_load(csv_load_url, file_name,csv_lx):

	r = requests.get(csv_load_url, stream=True)
	with open('./'+csv_lx+'/'+file_name, 'wb') as f:
		for data in r.iter_content(chunk_size=1024):
			f.write(data)


def down_csv(video_url):      

		rs = requests.get(video_url,  verify=False)
		data_json = json.loads(rs.text)
		return data_json['subjectName']


def get_csv_load_url(csv_url,url_one,csv_lx):


	rs = requests.post(csv_url)
	data_json = json.loads(rs.text)
	# print(data_json)
	for x in data_json:

		is_xls = x["sourceSuffix"]
		print(is_xls)
		if 'xlsx' in is_xls or 'xls' in is_xls:
			url_id = x['id']
			file_url = x['fileUrl']
			print(url_id)
			print(file_url)
			xls_url = 'http://gddata.gd.gov.cn/downloadFiles/open-file/'+url_one.replace('/','_')+'/'+file_url+'?filekey='+url_id
			csv_load(xls_url,file_url,csv_lx)			


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
		print(url_one)

		csv_lx = down_csv('https://gddata.gd.gov.cn/data/catalog/selectDataCatalogByResId?resId='+url_one)
		CheckDir(csv_lx)
		url = 'https://gddata.gd.gov.cn/data/dataSet/getFileList?resId='+url_one+'&sourceSuffix=&beginDate=&endDate='
		get_csv_load_url(url,url_one,csv_lx)
    
