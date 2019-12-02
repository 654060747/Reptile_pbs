# encoding='utf-8'
import time
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
	time.sleep(1)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


def by_che300(url):
	driver = webdriver.Chrome()
	driver.get(url)
	driver.find_element_by_css_selector("body > div.result > div > div.rh > div > a").click()
	time.sleep(1)

	# 移动句柄为当前页面
	# all_handles=driver.window_handles #显示当前页面一共有多少个句柄，结果是一个列['' ,'']
	# print(all_handles)
	# current_handle=driver.current_window_handle #当前页面的句柄即window_handles[0]
	# print(current_handle)
	driver.switch_to_window(driver.window_handles[1])#移动句柄定位到当前页面

	data = data_(driver)
	css = "body > div.main > div > dl:nth-child(2) > dt"
	data = select_css(2,data,css,'')
	print(data)

    #关闭当前句柄
    # driver.close()


urls = ["https://www.che300.com/pinggu/v3c3m1169042r2018-1g10?click=homepage&rt=1560258588319"]	

for url in urls:
	by_che300(url)

