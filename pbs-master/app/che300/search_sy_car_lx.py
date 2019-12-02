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




def request_series_id(series_id,series_name):

	series_url = "https://open.che300.com/api/cv/model_list?series_id="+str(series_id)

	rs = requests.get(series_url, verify=False)
	rs.encoding = 'utf-8'
	# print(rs.status_code)
	if rs.status_code == 200:
		series_data = json.loads(rs.text)
		series_datas = series_data["data"]["list"]
		for series_one in series_datas:
			# url需要拼接的参数
			model_id = series_one['id']
			# print(model_id)
			# 车型
			model_name = series_one['name']
			# print(model_name)
			# 最小年份
			min_reg_year = series_one['min_year']
			# print(min_reg_year)
			# 最大年份
			max_reg_year = series_one['max_year']
			# print(max_reg_year)

			string_buffer = ''
			# 循环年份
			for j in range(int(min_reg_year),int(max_reg_year)+1):
				if j == 2019:
					# 月份
					for z in range(1,7):
						model_url = "https://www.che300.com/pinggu/v3c3b325s4073m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10?p=v3c3b325s4073m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10&business=1&click=homepage/&rt=1560424980934"
						string_buffer = string_buffer + model_url + ","

				else:
					for z in range(1,13):
						model_url = "https://www.che300.com/pinggu/v3c3b325s4073m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10?p=v3c3b325s4073m"+str(model_id)+"r"+str(j)+"-"+str(z)+"g10&business=1&click=homepage/&rt=1560424980934"
						string_buffer = string_buffer + model_url + ","

			print(series_name+","+model_name+","+string_buffer)

			# data_all = {'series_name': series_name, 'model_name': model_name, 'model_urls': string_buffer}
			# create_che300_url(data_all)
			# print('====================================上传成功==============================================')



def request_id(i):

	search_url = "https://open.che300.com/api/cv/series_list?brand_id="+str(i)


	rs = requests.get(search_url, verify=False)
	rs.encoding = 'utf-8'
	# print(rs.status_code)
	if rs.status_code == 200:
		search_data = json.loads(rs.text)
		sy_datas = search_data["data"]["list"]
		for sy_one in sy_datas:
			# 车系
			series_name = sy_one["name"]
			series_id = sy_one["id"]
			# print(series_name)
			request_series_id(series_id,series_name)

		


# id_dict = [436,391,294,325,341,268,566,309,761,301,335,395,270,344,249,250,718,394,327,493,282,308,286,567,298,296,274,397,259,541,303,333,293,263,399,559,307,738,349,431,790,401,351,252,727,277,554,313,759,276,283,758,606,350,556,555,271,320,404,326,353,448,771,697,405,359,358,299,450,356,453,407,451,702,357,454,557,686,362,762,723,265,410,782,254,248,289,314,273,411,272,329,625,365,260,257,267,280,414,332,373,322,492,323,284,266,275,304,797,462,288,608,421,821,319,537,418,422,251,464,318,539,491,383,300,465,311,471,472,255,765,728,474,331,253,822,475,315,385,428,427,324,478,477,337,626,261,305,287,302,292,269,295,737,430,429,540,389,328,708,435,823,281,483,312,317,256,297,316,321]
id_dict = [436]
for i in id_dict:
	request_id(i)