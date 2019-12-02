# coding=utf-8
import requests,json,sys,os
from bs4 import BeautifulSoup


# # 当前文件的路径
# pwd = os.getcwd()
# project_path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
# sys.path.append(project_path)

# from api.rest_api import RestApi

# import urllib3
# urllib3.disable_warnings()
# api = RestApi()


# def create_che300_url(data):
# 	try:
# 		api.che300_url(data)
# 	except Exception as e:
# 		print (" api request fail 	. 	.		. ", format(e)) # 接口请求失败




def request_series_id(series_id,series_group_name,series_name):

	series_url = "https://ssl-meta.che300.com/meta/model/model_series"+str(series_id)+".json?v=1560129818"

	rs = requests.get(series_url, verify=False)
	rs.encoding = 'utf-8'
	# print(rs.status_code)
	if rs.status_code == 200:
		series_data = json.loads(rs.text)
		for series_one in series_data:
			# url需要拼接的参数
			model_id = series_one['model_id']
			# print(model_id)
			# 车型
			model_name = series_one['model_name']
			# print(model_name)
			# 最小年份
			min_reg_year = series_one['min_reg_year']
			# print(min_reg_year)
			# 最大年份
			max_reg_year = series_one['max_reg_year']
			# print(max_reg_year)

			string_buffer = ''
			# 循环年份
			for j in range(int(min_reg_year),int(max_reg_year)+1):
				if j == 2019:
					# 月份
					for z in range(1,7):
						model_url = "https://www.che300.com/pinggu/v3c3m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10?click=homepage&rt=1560168449752"
						string_buffer = string_buffer + model_url + ","

				else:
					for z in range(1,13):
						model_url = "https://www.che300.com/pinggu/v3c3m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10?click=homepage&rt=1560168449752"
						string_buffer = string_buffer + model_url + ","

			print(series_group_name+","+series_name+","+model_name+","+string_buffer)

			# data_all = {'series_group_name': series_group_name, 'series_name': series_name, 'model_name': model_name, 'model_urls': string_buffer}
			# create_che300_url(data_all)
			# print('====================================上传成功==============================================')



def request_id(i):

	search_url = "https://ssl-meta.che300.com/meta/series/series_brand"+str(i)+".json?v=1560129818"

	rs = requests.get(search_url, verify=False)
	rs.encoding = 'utf-8'
	# print(rs.status_code)
	if rs.status_code == 200:
		search_data = json.loads(rs.text)
		for search_one in search_data:
			# 参数
			series_id = search_one['series_id']
			# print(series_id)
			# 品牌
			series_group_name = search_one['series_group_name']
			# 车系
			series_name = search_one['series_name']
			request_series_id(series_id,series_group_name,series_name)


# id_dict = [1,2,3,536,587,5,7,15,172,144,6,9,12,8,499,10,115,156,17,14,167,573,13,11,20,16,19,18,21,23,22,24,497,25,34,639,142,26,30,170,33,28,32,27,29,31,574,36,35,39,545,40,162,37,42,38,543,41,44,45,636,46,47,586,48,50,56,51,54,57,52,173,146,560,147,160,53,618,55,495,145,59,58,63,143,62,65,60,66,542,68,61,64,634,67,69,71,70,572,752,817,825,73,157,74,75,158,562,77,546,76,819,79,90,78,80,84,85,83,619,81,87,89,815,561,682,86,88,82,661,588,712,750,92,93,94,96,97,95,641,98,558,99,100,713,101,102,103,635,637,503,716,104,105,106,107,624,632,108,109,110,631,570,112,113,498,111,116,114,117,169,149,501,118,120,166,119,150,816,121,163,122,544,123,124,617,571,616,125,126,127,155,130,638,148,151,128,717,564,751,132,159,131,615,135,133,134,565,568,547,136,563,824,138,137,139,140,152,154,168,569]
id_dict = [569]
for i in id_dict:
	request_id(i)