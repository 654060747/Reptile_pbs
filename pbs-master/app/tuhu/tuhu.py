# encoding='utf-8'
import time,os
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from tuhu_requests_data import by_tuhu_baoyang_data

root_path = "./down_car/"

def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


def write_file(car_pic,car,car_xh,url):
	CheckDir(root_path)
	file_name = root_path+"car.csv"
	# encoding='utf-8'
	with open(file_name, 'a+') as f:
		writer = f.write(car_pic+","+car+","+car_xh+","+url+'\n')


def data_(driver):
	time.sleep(1.5)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def car_nf(data,driver,car_lx_one,car_pl_one,car_pic,car,car_xh):
	car_nianfen_list = data.select("#div5 > ul > li")
	for x in car_nianfen_list:
		# 车年份
		car_nf_one = x.get("data-nian")
		# print(car_nf_one)
		# url
		url = "https://by.tuhu.cn/baoyang/"+car_lx_one+"/pl"+car_pl_one+"-n"+car_nf_one+".html"
		print(car_pic+","+car+","+car_xh+","+url)
		# write_file(car_pic,car,car_xh,url)
		# print("==========写入CSV成功===========")
		# 调用模块拿数据
		# by_tuhu_baoyang_data(url)


def car_pl(data,driver,car_lx_one,car_pic,car,car_xh):
	car_pailiang = data.select("#div5 > ul > li")
	i = 0
	for x in car_pailiang:
		# 车排量
		car_pl_one = x.get("data-pailiang")
		# print(car_pl_one)
		i = i+1
		driver.find_element_by_css_selector("#div5 > ul >li:nth-child("+str(i)+")").click()
		data = data_(driver)
		# 得到年份
		car_nf(data,driver,car_lx_one,car_pl_one,car_pic,car,car_xh)

		# 跳回点击排量
		driver.find_element_by_css_selector("#div40 > div:nth-child(4) > div.CarHistoryTitleDel").click()
		time.sleep(1)
			


def car_lx(char,count,data,driver,car_pic,car):
	car_leixing_list = data.select('#div5 > ul >li')
	# print(car_leixing_list)
	i = 0
	for x in car_leixing_list:
		i = i+1
		# if x.get("data-id") != None and i > 17:
		if x.get("data-id") != None:
			# url参数
			car_lx_one = x.get("data-id")
			# print(car_lx_one)
			# 车型号
			car_xh = x.getText()
			# print(car_xh)

			driver.find_element_by_css_selector("#div5 > ul >li:nth-child("+str(i)+")").click()
			data = data_(driver)

			car_pailiang = data.select("#div5 > ul > li")
			car_pl_one = car_pailiang[0].get("data-pailiang")
			# print(car_pl_one)
			if car_pl_one == None:
				data_(driver)
				driver.find_element_by_id("reSelectCar").click()
				time.sleep(2)
				driver.find_element_by_css_selector("#div2 > li:nth-child("+str(char)+")").click()
				time.sleep(2)
				driver.find_element_by_css_selector("#CarBrands > ul > li:nth-child("+str(count)+")").click()
				time.sleep(1)
				url = "https://by.tuhu.cn/baoyang/"+car_lx_one+"/pl-n.html"
				print(car_pic+","+car+","+car_xh+","+url)
				# by_tuhu_baoyang_data(url)


			if car_pl_one != None:
				# 得到排量
				car_pl(data,driver,car_lx_one,car_pic,car,car_xh)
				# 跳回点击品牌车型
				driver.find_element_by_css_selector("#div40 > div:nth-child(3) > div.CarHistoryTitleDel").click()
				time.sleep(1)
			

def car_baoyang(char,driver):
	# 点击字母
	driver.find_element_by_css_selector("#div2 > li:nth-child("+str(char)+")").click()
	data = data_(driver)
	# 得到每种字母下有多少品牌车
	car_list = data.select("#CarBrands > ul > li")
	lengh_car = len(car_list)
	letter = data.select("#div2 > li:nth-child("+str(char)+")")[0].getText()
	print(letter+"字母下车数量:::"+str(lengh_car))

	# for i in range(7,8):
	for i in range(7,lengh_car+1):
		# 车logo
		car_pic = data.select("#CarBrands > ul > li:nth-child("+str(i)+") > img")[0].get("src")
		# print(car_pic)
		# 车品牌
		car = data.select("#CarBrands > ul > li:nth-child("+str(i)+")")[0].getText()
		# print(car)
		# 点击各品牌车
		driver.find_element_by_css_selector("#CarBrands > ul > li:nth-child("+str(i)+")").click()
		data = data_(driver)
		# 获取品牌车型号
		car_lx(char,i,data,driver,car_pic,car)

		# 跳回点击各品牌车
		driver.find_element_by_css_selector("#div40 > div.CarHistoryTitlediv > div.CarHistoryTitleDel").click()
		time.sleep(1)


def by_tuhu_baoyang():
	driver = webdriver.Chrome()
	driver.get('https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl2.0T-n2019.html')
	# 跳出选择车型界面
	driver.find_element_by_id("reSelectCar").click()
	time.sleep(2)

	for char in range(3,4):
		car_baoyang(char,driver)


by_tuhu_baoyang()

