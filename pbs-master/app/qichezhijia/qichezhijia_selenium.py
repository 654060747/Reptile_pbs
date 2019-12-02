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
	time.sleep(1.5)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data



def by_qichezhijia():
	driver = webdriver.Chrome()
	driver.get('https://car.autohome.com.cn/config/series/4350.html#pvareaid=102192')
	# 跳出选择车型界面
	data = data_(driver)
	css = '#config_nav > table > tbody > tr > td:nth-child(2) > div.carbox > div > a'
	name = select_css(2,data,css,'')
	print(name)



by_qichezhijia()

