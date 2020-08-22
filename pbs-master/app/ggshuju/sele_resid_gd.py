# encoding='utf-8'
import time
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


def write_file(data_list):
	with open('./resId_bc.csv', 'a+', encoding='utf-8') as f:
		writer = f.write(data_list+'\n')


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


def data_(driver):
	time.sleep(1)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data




def get_csv_load_url(driver):

	
	data_all = data_(driver)
	css = '#dataSetContent_list > li'
	li_list = select_css(1,data_all,css,'')
	# print(len(li_list))
	for x in range(1,len(li_list)+1):
		#dataSetContent_list > li:nth-child(2) > div.title > a.tit_txt
		css = '#dataSetContent_list > li:nth-child('+str(x)+') > div.title > a.tit_txt'
		data = select_css(3,data_all,css,'href')
		print(data)
		write_file(data)


	css = 'body > div.container_wrap > div.t_main_wrap > div > div.sjkf_right_wrap.t4_fr > div:nth-child(2) > div.search_cont_wrap > div > a.next'

	driver.find_element_by_css_selector(css).click()
	get_csv_load_url(driver)

# 656
url = 'https://gddata.gd.gov.cn/data/dataSet/toDataSet'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(60)
get_csv_load_url(driver)