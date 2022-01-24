# -*- coding: utf-8 -*-
from selenium import webdriver
import time,os
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup


# 1、安装python3
# 2、pip安装selenium,pyquery,bs4
# 3、安装Chrome,并下载对应版本驱动chromedriver
# 4、把驱动chromedriver放入Chrome目录==>...\Chrome\Application\,并把此目前添加环境变量(或者修改代码添加到代码)


# 数据存储本地
def WriteInfo(count,folder_name,data):
	if count == 1:
		with open(folder_name, 'a+', encoding='utf-8') as f:
			writer = f.write(data+"\n")
	if count == 2:
		with open(folder_name, 'w', encoding='utf-8') as f:
			writer = f.write(data+"\n")
	if count == 3:
		with open(folder_name,'r',encoding='utf-8') as f:
			return f.read() 



def is_folder(folder_quchong):
	if not os.path.exists(folder_quchong):
		WriteInfo(2,folder_quchong,'')
	quchong_data = WriteInfo(3,folder_quchong,'')
	return quchong_data



# 不断获取js加载的全部数据
def data_(driver):
	html = driver.page_source 
	data = str(pq(html))  
	data = BeautifulSoup(data,"lxml")
	data.encoding = 'utf-8'
	return data



# 点击邀请并发送邀请
def data_get(driver,i,j,data):
	xpaths = "//*[@id='tcm']/div[3]/div/div[1]/div[@style='transform: translateY("+str(i*scrollTo_len)+"px);']"
	WriteInfo(2,folder_jindu,"粉丝数"+str(j)+"-"+str(j+etc_space_count)+"滑动次数"+str(i)+",滑动距离"+str(i*scrollTo_len))
	css1 = "#tcm > div.creatorListContainer.relative > div > div.relative > div[style='transform: translateY("+str(i*scrollTo_len)+"px);']"
	if len(data.select(css1)) > 0:
		for x in range(1,5):
			css2 = css1+"> div:nth-child("+str(x)+")"
			if len(data.select(css2)) > 0:
				print("===========粉丝数"+str(j)+"-"+str(j+etc_space_count)+"第"+str(i)+"行,即"+str(i*scrollTo_len)+"px的第"+str(x)+"条============")
				name_1 = driver.find_element_by_xpath(xpaths+"/div["+str(x)+"]/div[2]/div[2]/div[1]/div[1]/div/div/div").text
				print("准备邀请："+name_1)
				etc_count = driver.find_element_by_xpath(xpaths+"/div["+str(x)+"]/div[2]/div[2]/div[3]/div[1]/span[2]").text
				if "K" in etc_count or "M" in etc_count:
					if "K" in etc_count:
						new_etc_count_ = etc_count.split("K")[0]+"000"
					if "M" in etc_count:
						new_etc_count_ = etc_count.split("M")[0]+"000000"
					if "." in new_etc_count_:
						new_etc_count = int(new_etc_count_.replace(".","")[:-1])
					else:
						new_etc_count = int(new_etc_count_)
				else:
					new_etc_count = int(etc_count)
				print("粉丝数："+str(new_etc_count))
				view_count = driver.find_element_by_xpath(xpaths+"/div["+str(x)+"]/div[2]/div[2]/div[3]/div[2]/span[2]").text
				if "K" in view_count or "M" in view_count:
					if "K" in view_count:
						new_view_count_ = view_count.split("K")[0]+"000"
					if "M" in view_count:
						new_view_count_ = view_count.split("M")[0]+"000000"
					if "." in new_view_count_:
						new_view_count = int(new_view_count_.replace(".","")[:-1])
					else:
						new_view_count = int(new_view_count_)
				else:
					new_view_count = int(view_count)
				print("平均观看数："+str(new_view_count))
				# 判断数据是否已发送过，已发送的不再发送
				quchong_data = is_folder(folder_quchong)
				if "_&_"+name_1+"_&_" not in quchong_data:
					# 点击邀请
					button_xpaths = xpaths+"/div["+str(x)+"]/div[2]/div[2]/span/button"
					driver.find_element_by_xpath(button_xpaths).click()
					driver.implicitly_wait(10)
					time.sleep(3)
					# 选择提成结佣
					driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[1]/span/div[2]").click()
					# 是否提供免费样品,粉丝＞200K,平均观看数＞50K,提供免费样品 
					if new_etc_count > etcCount and new_view_count > viewCount:
						driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[2]/div/span[2]/button").click()
					# 填写邀请信息
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/textarea').clear()
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/textarea').send_keys(content)
					# 填写联系方式
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[2]/div[1]/div/div/div[1]/span/span/span/div/div/span').click()
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[2]/div[1]/div/div/div[1]/span/span/span/div/div/input').send_keys(code)
					driver.find_element_by_xpath(r'/html/body/span/div/div/div/div/li[6]').click()
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[2]/div[1]/div/div/div[1]/span/span/input').send_keys(wtatsapp)
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div/input').clear()
					driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div/input').send_keys(email)
					
					# 如果需要发送邀请,注释掉以下代码
					driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/div[2]/button[1]").click()
					time.sleep(1)
					driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[3]/div[3]/button[2]").click()
					time.sleep(0.5)
					# 发送邀请,如果需要发送,放开注释
					# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[3]/div[2]/button[2]").click()
					# time.sleep(1)

					# 存储名字,做去重处理
					WriteInfo(1,folder_quchong,"_&_"+name_1+"_&_")
				else:
					print("*******数据已发送邀请********")
			else:
				break



# 不断向下滑动
def data_tiktok(driver,i,j):
	data = data_(driver)
	data_get(driver,i,j,data)
	i = i+1
	css_ = "#tcm > div.creatorListContainer.relative > div > div.relative > div[style='transform: translateY("+str(i*scrollTo_len)+"px);']"
	if len(data.select(css_)) > 0:
		driver.execute_script('window.scrollBy(0,'+str(scrollTo_len)+')')
		data_tiktok(driver,i,j)
	else:
		# 粉丝数目按钮消失,将其可见
		driver.find_element_by_xpath(r'//*[@id="root"]/div/div/section/section/aside/div/div/div/div/div[3]/div/div[2]/div[2]/div/span[2]/div').click()
		driver.implicitly_wait(10)
		time.sleep(2)
		driver.find_element_by_xpath(r'//*[@id="root"]/div/div/section/section/aside/div/div/div/div/div[3]/div/div[2]/div[1]/div/span[2]/div/span').click()
		driver.implicitly_wait(10)
		time.sleep(3)
			



# 登录成功后选择指定类别
def content_selection(driver):
	# 点击达人广场
	driver.find_element_by_xpath(r'//*[@id="root"]/div/div/section/section/aside/div/div/div/div/div[3]/div/div[2]/div[1]/div/span[2]/div/span').click()
	# 点击内容类别
	driver.find_element_by_xpath(r'//*[@id="tcm"]/div[2]/div/div/div[1]/div[2]/div[1]/button').click()
	time.sleep(1)
	# Comedy
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[1]').click()
	# DIY & Handicrafts
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[8]').click()
	# Family
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[11]').click()
	# Daily Life
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[16]').click()
	time.sleep(1)
	# Beauty & Care
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[25]').click()
	time.sleep(1)
	# Games
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[33]').click()
	# Technology & Photography
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[37]').click()
	time.sleep(1)
	# Sports
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[41]').click()
	# 点击达人区域
	driver.find_element_by_xpath(r'//*[@id="tcm"]/div[2]/div/div/div[1]/div[2]/div[5]/button').click()
	time.sleep(1)
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[2]/span[3]').click()
	# 粉丝每5万做一次搜索
	for j in range(etc_mix_count,etc_max_count,etc_space_count):
		# 点击粉丝数目
		driver.find_element_by_xpath(r'//*[@id="tcm"]/div[2]/div/div/div[1]/div[2]/div[2]/button').click()
		time.sleep(0.5)
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div').click()
		time.sleep(0.5)
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div[2]/div/input[1]').clear()
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div[2]/div/input[1]').send_keys(str(j))
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div[2]/div/input[2]').clear()
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div[2]/div/input[2]').send_keys(str(j+etc_space_count))
		driver.find_element_by_xpath(r'/html/body/span/div/div/div[5]/div[2]/button').click()
		driver.implicitly_wait(10)
		time.sleep(3)
		# 滑动计数使用
		i = 0
		if not os.path.exists(folder_jindu):
			data_tiktok(driver,i,j)
		else:
			txt_file = WriteInfo(3,folder_jindu,'')
			lenn = int(txt_file.split("滑动次数")[1].split(",")[0])
			etc_int = int(txt_file.split("粉丝数")[1].split("-")[0])
			if etc_int == j:
				for x in range(0,lenn):
					driver.execute_script('window.scrollBy(0,'+str(scrollTo_len)+')')
					time.sleep(1.5)
				data_tiktok(driver,lenn,j)
			else:
				data_tiktok(driver,i,j)



# 登录网页
def by_tiktok(url):
	# 启动浏览器打开网页
	driver = webdriver.Chrome()
	driver.get(url)
	driver.maximize_window()
	# 点击邮箱登录
	driver.implicitly_wait(10)
	driver.find_element_by_xpath(r'//*[@id="TikTok_Ads_SSO_Login_Email_Panel_Button"]').click()
	driver.find_element_by_xpath(r'//*[@id="TikTok_Ads_SSO_Login_Email_Input"]').send_keys(name)
	driver.find_element_by_xpath(r'//*[@id="TikTok_Ads_SSO_Login_Pwd_Input"]').send_keys(password)
	driver.find_element_by_xpath(r'//*[@id="TikTok_Ads_SSO_Login_Btn"]').click()
	# 登录成功点击开始及跳过
	driver.implicitly_wait(10)
	time.sleep(2)
	driver.find_element_by_xpath(r'/html/body/div[2]/div[2]/div/div[3]/div[2]/div/button/span').click()
	time.sleep(2)
	driver.find_element_by_xpath(r'//*[@id="___reactour"]/div[4]/div/div[2]/div/button[1]').click()
	content_selection(driver)



if __name__ == '__main__':
	# 登录邮箱、密码
	name = 'xxxxxxx'
	password = 'xxxxxx'

	# 粉丝数目最小值、最大值、搜索间隔值,每5万做一次搜索（5万这个数值后期可以修改）
	etc_mix_count = 200000
	etc_max_count = 1000000
	etc_space_count = 50000

	# 提供免费样品条件,粉丝数、平均观看数
	etcCount = 200000
	viewCount = 50000

	# 邀请信息内容
	content = "Up to 50% commission\nHi, I'm Savannah from @ttshopuk. We would like to invite you to be our affiliate and promote the products. And we can provide up to 50% commission on each sale. Please contact me if you are interested."

	# 邀请联系方式
	code = "44"
	wtatsapp = "xxxxxxxx"
	email = "xxxxxx"


	# 滑动距离(代码关联不修改)
	scrollTo_len = 396
	# 记录进度目录
	folder_jindu = ".\\已发送_进度.txt"
	# 去重使用
	folder_quchong = '.\\已发送_去重.txt'
	by_tiktok("https://affiliate.tiktokglobalshop.com/seller/dashboard/tcm/creator-marketplace")
