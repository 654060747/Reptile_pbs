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
	time.sleep(5)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def tuhu_data_(string_buffer,driver,data,by_lx,by_son,by_name):
	# 得到产品列表
	css = "#changeProductList > div"
	div_list_ = select_css(1,data,css,'')
	# 右边列数
	for m in range(2,len(div_list_)+1):
		# print("xxxxxxxxxxxxxxxxxx"+str(m))
		css_ = "#changeProductList > div:nth-child("+str(m)+") >"
		css = "a.img"
		# 拿到产品链接
		product_url = select_css(3,data,css,'href')
		print("产品链接:::"+product_url)
		# 拿到产品图片
		css = css_+"a:nth-child(1) > img"
		product_pic = select_css(3,data,css,'src')
		print("产品图片:::"+product_pic)
		# 拿到列表内容
		css = css_+"a:nth-child(2) > span.productTitle"
		product_content = select_css(2,data,css,'')
		print("产品介绍:::"+product_content)
		# 拿到规格
		try:
			css = css_+"a:nth-child(2) > span.itemTag.qianscp"
			product_spec = select_css(2,data,css,'')
		except Exception:
			product_spec = " "
		print("产品规格:::"+product_spec)
		# 拿到列表价格
		css = css_+"div"
		product_price = select_css(2,data,css,'')
		print("产品价格:::"+product_price)

		string_buffer = string_buffer + product_url +","+ product_pic +","+ product_content +","+ product_spec + ","+ product_price + ";"
		# print(string_buffer)
		time.sleep(0.5)
		print("======"+by_name+","+product_url+","+product_pic+","+product_content+","+product_spec+","+product_price)
	# 查看有没有下一页数据
	css = "#changeList > div.tabcon.UnSelect > div:nth-child(2)"
	next_title = select_css(3,data,css,"class")
	print(next_title)
	if "active" in next_title:
		driver.find_element_by_css_selector("#changeList > div.tabcon.UnSelect > div.next.active").click()
		data = data_(driver)
		# 有下一页递归自己取数据
		tuhu_data_(string_buffer,driver,data,by_lx,by_son,by_name)
	# print(by_lx+","+by_son+","+by_name+","+string_buffer)


def find_result_data(driver,j,css_,data,by_lx,by_son,by_name):
	string_buffer = ''
	css = css_+"tr:nth-child("+str(j)+") > td:nth-child(2) > div"
	div_list = select_css(1,data,css,'')
	# 左边列数
	for z in range(1,len(div_list)+1):
		# 点击内容列
		css = css_+"tr:nth-child("+str(j)+") > td:nth-child(2) > div:nth-child("+str(z)+")"
		driver.find_element_by_css_selector(css).click()
		data = data_(driver)
		tuhu_data_(string_buffer,driver,data,by_lx,by_son,by_name)


def by_lx_open(driver,data,baoyang_dict):
	# 拿到子项点开的详细条数
	css = "#productList > div"
	div_list = select_css(1,data,css,'')
	for i in range(1,len(div_list)+1):
		css = "#productList > div:nth-child("+str(i)+") > div > span.name"
		by_son = select_css(2,data,css,'')
		# print(by_son)
		# 字典查找对应保养类型
		for by_son_one in baoyang_dict:
			if by_son_one in by_son:
				by_lx = baoyang_dict[by_son_one]
		# 拿到每个子项下的项目数量
		css_ = "#productList > div:nth-child("+str(i)+") > table > tbody >"
		css = css_+"tr"
		tr_list = select_css(1,data,css,'')
		for j in range(1,len(tr_list)+1):
			# 拿到项目名
			css = css_+"tr:nth-child("+str(j)+") > td:nth-child(1) > p"
			by_name = select_css(2,data,css,'')
			print(by_name)
			# 取数据
			if "火花塞" in by_name:
				find_result_data(driver,j,css_,data,by_lx,by_son,by_name)

			if "滤清器" in by_name:
				find_result_data(driver,j,css_,data,by_lx,by_son,by_name)
			

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
			if "大保养服务" in baoyang_text:
				driver.find_element_by_css_selector(css).click()
			if "空调滤清器" in baoyang_text:
				driver.find_element_by_css_selector(css).click()
			if "火花塞" in baoyang_text:
				driver.find_element_by_css_selector(css).click()

	# print(baoyang_dict)
	# 数据更新到最新
	data = data_(driver)
	by_lx_open(driver,data,baoyang_dict)


def by_tuhu_baoyang_data(url_one):
	driver = webdriver.Chrome()
	driver.get(url_one)
	data = data_(driver)
	# 得到保养类型
	by_list(data,driver,url_one)


url = ["https://by.tuhu.cn/baoyang/VE-HODO07AK/pl1.5T-n2018.html"]	

for url_one in url:
	by_tuhu_baoyang_data(url_one)

