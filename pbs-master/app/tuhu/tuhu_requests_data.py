# encoding='utf-8'
import time,os
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


def data_(driver):
	time.sleep(0.5)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def find_result_data(j,css_,data,by_lx,by_son):
	# 拿到项目名
	css = css_+"tr:nth-child("+str(j)+") > td:nth-child(1) > p"
	by_name = select_css(2,data,css,'')
	# print(by_name)
	# 拿到每个项目下的内容数
	string_buffer = ''
	css = css_+"tr:nth-child("+str(j)+") > td:nth-child(2) > div"
	div_list = select_css(1,data,css,'')
	for z in range(1,len(div_list)+1):
		# 拿到内容
		css = css_+"tr:nth-child("+str(j)+") > td:nth-child(2) > div:nth-child("+str(z)+") > div.pack_biaoti"
		by_content = select_css(2,data,css,'')
		# print(by_content)
		# 拿到价格
		css = css_+"tr:nth-child("+str(j)+") > td:nth-child(2) > div:nth-child("+str(z)+") > div.pck_price"
		by_price = select_css(2,data,css,'')
		# print(by_price)
		string_buffer = string_buffer + by_content +","+ by_price + ";"

	print(by_lx+","+by_son+","+by_name+","+string_buffer)


def by_lx_open(data,baoyang_dict):
	# 拿到子项点开的详细条数
	css = "#productList > div"
	div_list = select_css(1,data,css,'')
	for i in range(1,len(div_list)+1):
		css = "#productList > div:nth-child("+str(i)+") > div > span.name"
		by_son = select_css(2,data,css,'')
		# print(by_son)
		# 字典此项不对应,需要另外处理
		if "更换防冻冷却液" in by_son:
			by_lx = baoyang_dict["更换防冻液"]
		# 字典查找对应保养类型
		for by_son_one in baoyang_dict:
			if by_son_one in by_son:
				by_lx = baoyang_dict[by_son_one]
		# 拿到每个子项下的项目数量
		css_ = "#productList > div:nth-child("+str(i)+") > table > tbody >"
		css = css_+"tr"
		tr_list = select_css(1,data,css,'')
		for j in range(1,len(tr_list)+1):
			# 取数据
			find_result_data(j,css_,data,by_lx,by_son)
		# 大保养存在时取小保养数据
		if "大保养服务" in by_son:
			for j in range(1,3):
				find_result_data(j,css_,data,by_lx,"小保养服务")

			

def by_list(data,driver,url_one):
	dl_list = data.select("#package_baoyang > dl")
	if len(dl_list) == 0:
		print("网页没有数据==="+url_one)
	baoyang_dict = {}
	for i in range(1,len(dl_list)+1):
		# 拿到保养类型
		css = "#package_baoyang > dl:nth-child("+str(i)+") > dt > span"
		baoyang_list_text = select_css(2,data,css,'')
		# print(baoyang_list_text+":::")

		css = "#package_baoyang > dl:nth-child("+str(i)+") > dd"
		dd_list = select_css(1,data,css,'')
		for j in range(2,len(dd_list)+2):
			# 拿到保养的子项
			css = "#package_baoyang > dl:nth-child("+str(i)+") > dd:nth-child("+str(j)+") > div > span"
			baoyang_text = select_css(2,data,css,'')
			# print(baoyang_text)
			# 做成字典{"子项":"保养类型"}
			baoyang_dict[baoyang_text] = baoyang_list_text

			css = "#package_baoyang > dl:nth-child("+str(i)+") > dd:nth-child("+str(j)+")"
			dd_title = select_css(3,data,css,"class")
			print(dd_title)
			# 首次无需再更新数据
			if i > 1 or j > 2:
				data = data_(driver)
			# 查看有没有默认点击过,点击过不需要再点击
			if "checked" not in dd_title:
				driver.find_element_by_css_selector(css).click()

	# print(baoyang_dict)
	# 数据更新到最新
	data = data_(driver)
	by_lx_open(data,baoyang_dict)


def by_tuhu_baoyang_data(url_one):
	driver = webdriver.Chrome()
	driver.get(url_one)
	data = data_(driver)
	# 得到保养类型
	by_list(data,driver,url_one)


url = ["https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl4.0T-n2019.html","https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl2.0T-n2019.html","https://by.tuhu.cn/baoyang/VE-GM-S07BTHRV/pl1.6L-n2012.html","https://by.tuhu.cn/baoyang/VE-ZAR-Giulia/pl3.0T-n2019.html","https://by.tuhu.cn/baoyang/VE-McLaren540C/pl3.8T-n2019.html"]	

for url_one in url:
	by_tuhu_baoyang_data(url_one)

