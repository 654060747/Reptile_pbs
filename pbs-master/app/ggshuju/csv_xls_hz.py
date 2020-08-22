# encoding=utf-8
import requests,os
import csv,json


def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


def csv_load(file_dir,file_name,download_path,zui_name):
	# urllib模块下载方式直接下载文件
	# urllib.request.urlretrieve(csv_load_url,path)
	# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	# res = urllib.request.Request(csv_load_url, headers=headers)

	# f = urllib.request.urlopen(res) 
	# data = f.read() 
	# with open(path+file_name, "wb") as code:     
	# 	code.write(data)

    # with open('./教育科技.csv', 'a+', encoding='utf-8') as f:
    #     writer = f.write(csv_load_url+'\n')

	r = requests.get(download_path, stream=True)
	if ',' in file_dir:
		file_dir = file_dir.split(',')[0]
	print(file_dir+"/"+file_name+"."+zui_name)
	CheckDir(file_dir)
	with open(file_dir+"/"+file_name+"."+zui_name, 'wb') as f:
		for data in r.iter_content(chunk_size=1024):
			f.write(data)


def get_csv_load_url(file_id,file_dir):
	url = 'https://data.hz.zjzwfw.gov.cn/dop/dataOpen/dataFileList.action'
	data = {

		'postData': '{"resId":'+str(file_id)+',"pageSplit":{"pageNumber":1,"pageSize":10}}'
	}
	rs = requests.get(url, data, verify=False)
	data_json = json.loads(rs.text)
	csv_list = data_json["fileList"]
	lx = []
	for x in csv_list:
		csv_ = x['fileType']
		lx.append(csv_)
		if 'csv' in csv_ or 'Csv' in csv_ or 'CSV' in csv_:
			print(csv_)
			file_name = x['fileName']
			download_path = x['downloadPath']
			csv_load(file_dir,file_name,download_path,csv_.lower())

	if 'csv' not in lx and 'Csv' not in lx and 'CSV' not in lx:
		print(lx)
		print("=============")
		if 'xls' in lx or 'Xls' in lx or 'XLS' in lx:
			for x in csv_list:
				csv_ = x['fileType']
				print(csv_)
				if 'xls' in csv_ or 'Xls' in csv_ or 'XLS' in csv_:
					file_name = x['fileName']
					download_path = x['downloadPath']
					csv_load(file_dir,file_name,download_path,csv_.lower())


def get_csv_id(url,x):

	data = {

	'postData': '{"source_id":"","dept_id":"0","fieldId":"0","score":"","ability":"","source_type":"DATA","searchKey":"","sort":"","flag":false,"code":"","city_code":"001008001026","pageSplit":{"pageNumber":'+str(x)+',"pageSize":10}}'
	}

	rs = requests.post(url, data, verify=False)
	# print(rs.status_code)
	data_json = json.loads(rs.text)
	csv_list = data_json["rows"]
	for x in csv_list:
		file_dir = x['type_name']
		file_id = x['id']

		if file_dir != None:
			get_csv_load_url(file_id,file_dir)


# 循环页数
for x in range(0,59):

	print('第' + str(x) + '页')

	url = 'https://data.hz.zjzwfw.gov.cn/dop/dataOpen/list.action'
	# url = 'http://www.cddata.gov.cn/portal/catalog/index?domainId=domain-8&fileFormat=4&openType=1&page=' + str(x)

	get_csv_id(url,x)

	pass