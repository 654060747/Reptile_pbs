# coding=utf-8
import time,os
import requests
from selenium import webdriver
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

# 关键字
gjz = 'sofa'


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)

def data_(driver):
	time.sleep(2)
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data


headers = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "zh-CN,zh;q=0.9",
	"cache-control": "max-age=0",
	"cookie": "us=274271EC-A3B4-42EE-8DFD-394ABB80191E; _gcl_au=1.1.1166412673.1620806103; _ga=GA1.2.16331678.1620806103; _gid=GA1.2.1812838852.1620806103; _scid=7ba45869-d2cf-49d2-92ba-4042be4876db; _pxhd=842a1d7c8d4104e793a9eaefac95f722ed878fb422b320fb4b5ecc1ba15d8d1f:5e703410-b2f7-11eb-a158-836446943baf; _pxvid=5e703410-b2f7-11eb-a158-836446943baf; __gads=ID=7148285d1067e17c:T=1620806456:S=ALNI_MYpMHTjBXbtyuLkEUijbStk51SVzw; general_maturity=1; zm=AQABAAAAchYAABRwmOI9YXDcU15WPQgos-XdLXvW-I6JmTYec9KxQTaiFx4zm_jIgcMQ4mONCNhBTRZDdAGy63vz4sF41zXUHAPJmtSkCGP4OBzEElvdMMveOejv6su6HXkvYsxo0nlUEpHMoRW6; zs=F592657C-DDBC-4AEE-A6C8-C76BEA622709%7c0%7c13265381920%7cAQABAAAAchYAABRFFlETYMV8AahITzBM4NMtcbRMo3qFUTlAlF9Vean0CdA9x-0Ir9oIPSZ-nuUEUi3aKtbA%7c; NSC_xxx01=28d4a3da20d4e0cbb74fdc9a6ab9936fef06d9a5f47ba533650667b054b957dde644bab7; bx=qs%3d%26qs_x%3d132653855335127665%26promoanim%3d1%26promoanim_x%3d132654107335752535; NSC_smw=2618a3ce6ac8f1327f9a397007acd623ccbd0e837ed27b04f4f280c13966309d75a668e8; _uetsid=5c1ae7f0b2f711eb8c99bb592a495ed0; _uetvid=5c1b41f0b2f711eba4d9f5185aa215f0; _px2=eyJ1IjoiOTk3NmJiMzAtYjNlNS0xMWViLWFhMzQtNWJjMzViZDE0MWJkIiwidiI6IjVlNzAzNDEwLWIyZjctMTFlYi1hMTU4LTgzNjQ0Njk0M2JhZiIsInQiOjE2MjA5MDg3MzU5MDMsImgiOiI5M2E4OWJlZTVmN2RiNzcxMzRhYmQzMGU4OGI0YWU4MjI5MjRlMGE0YzYzZjI2MGRiNWQ1YTQyNTNmYWVjM2E4In0=; bs=pis%3d9%26zshopurl%3dz%2fs%2fsofa",
	"sec-ch-ua-mobile": "?0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "same-origin",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",

}


# 进入图片详情页
def by_img_details(url_id, url_img):
	print("原图链接…………"+url_img)
	# driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	driver = webdriver.Chrome()
	driver.get(url_id)
	time.sleep(1)
	js = "var q=document.documentElement.scrollTop=10000"
	driver.execute_script(js)
	data = data_(driver)
	public_css = '#main > div.WwwPage_root > div.WwwPage_headerAndContent > main > div > div > section.row.CmsSectionPdp > div > div'
	if len(select_css(1, data, public_css, '')) > 0:
		css = public_css+'> div.TopBar > div > div.TopBar-leftWrapper > div.TopBar-left > div.TopBar-titleRating > div.ProductTitle > div > h1'
		title_name = select_css(2, data, css, '')
		print("标题名称…………"+title_name)
		css = public_css+'> div:nth-child(1) > div.Tags'
		if len(select_css(1, data, css, '')) > 0:
			tags = select_css(2, data, css, '')
			print("Tags…………"+tags)
			css = public_css+'> div:nth-child(2) > div.OtherInfo > div:nth-child(1)'
			product_id = select_css(2, data, css, '')
			print("Product ID…………"+product_id)
			driver.close()
			driver.quit()
		else:
			str = input('等待刷新,刷新好请输入数字2\n')
			if '2' in str:
				by_img_details(url_id, url_img)
	else:
		str = input('等待刷新,刷新好请输入数字1\n')
		if '1' in str:
			by_img_details(url_id, url_img)


def by_to_zazzle(url_one,i):
	rs = requests.get(url_one, headers=headers, verify=False)
	data = BeautifulSoup(rs.text, "lxml")
	# css公共部分
	public_css = '#main > div.WwwPage_root > div.WwwPage_headerAndContent > main > div > div > div > div.SearchResults.SearchResults--ps60 > div >'
	css = public_css+'div.SearchResultsGridCell'
	div_list = select_css(1, data, css, '')
	# print(len(div_list))
	if len(div_list) > 0:
		for x in range(2,len(div_list)+2):
			css = public_css+'div:nth-child('+str(x)+') > div.SearchResultsGridCell-absolutePositionedContainer > div.SearchResultsGridCell-realviewContainer > a'
			url_id = select_css(3, data, css, 'href')
			print("正在爬取关键字"+gjz+"第"+str(i)+"页的"+"第"+str(x-1)+"个===="+url_id)
			css = public_css+'div:nth-child('+str(x)+') > div.SearchResultsGridCell-absolutePositionedContainer > div.SearchResultsGridCell-realviewContainer > a > div > img'
			# 图片链接
			net_pic = select_css(3, data, css, 'src')
			# 原图链接
			url_img = net_pic + '?rvtype=content'
			by_img_details(url_id, url_img)


url = 'https://www.zazzle.com/s/'+gjz+'?pg='
for i in range(1,17):
	start_url = url+str(i)
	by_to_zazzle(start_url,i)

