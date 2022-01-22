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


# 取各字段数据
def data_tiktok(driver,i):
	time.sleep(3)
	xpaths = "//*[@id='tcm']/div[3]/div/div[1]/div[@style='transform: translateY("+str(i*scrollTo_len)+"px);']"
	WriteInfo(2,folder_jindu,"滑动次数"+str(i)+",滑动距离"+str(i*scrollTo_len))
	data = data_(driver)
	css1 = "#tcm > div.creatorListContainer.relative > div > div.relative > div[style='transform: translateY("+str(i*scrollTo_len)+"px);']"
	if len(data.select(css1)) > 0:
		for x in range(1,5):
			print("===========第"+str(i)+"行,即"+str(i*scrollTo_len)+"px的第"+str(x)+"条============")
			name_1 = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[1]/div[1]/div/div/div').text
			name_2 = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[1]/div[2]/div/div/div').text
			print("名字1："+name_1)
			print("名字2："+name_2)
			etc_count = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[3]/div[1]/span[2]').text
			view_count = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[3]/div[2]/span[2]').text
			video_count = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[3]/div[3]/span[2]').text
			print("粉丝："+etc_count)
			print("平均观看数："+view_count)
			print("视频数："+video_count)
			gender_mix = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[4]/div[1]/span[1]').text
			gender = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[4]/div[1]/span[2]').text
			print("性别占比："+gender_mix)
			print("性别："+gender)
			age_mix = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[4]/div[2]/span[1]').text
			age = driver.find_element_by_xpath(xpaths+'/div['+str(x)+']/div[2]/div[2]/div[4]/div[2]/span[2]').text
			print("年龄占比："+age_mix)
			print("年龄："+age)
			# 判断是否有联系按钮及点击
			button_xpaths = xpaths + "/div["+str(x)+"]/div[2]/div[2]/button[@class='arco-btn arco-btn-primary arco-btn-size-default arco-btn-shape-square index__contactMeBtn--2-voa w-96 i18n-ecom-alliance-btn i18n-ecom-alliance-btn-type-primary']"
			button_css = css1 + "> div:nth-child("+str(x)+") > div.index__infoContainer--3fm-7.index__hasContact--aFEBd > div.index__infoContent--3IRt1 > button.arco-btn.arco-btn-primary.arco-btn-size-default.arco-btn-shape-square.index__contactMeBtn--2-voa.w-96.i18n-ecom-alliance-btn.i18n-ecom-alliance-btn-type-primary"
			if len(data.select(button_css)) > 0:
				driver.find_element_by_xpath(button_xpaths).click()
				time.sleep(2)
				# 判断是否有手机通讯邮箱地址
				Whatsapp_xpaths = "/html/body/div[3]/div[2]/div/div[3]/div[2]/div/div[3]/div[1]/div[1]"
				data = data_(driver)
				css2 = "body > div:nth-child(7) > div.arco-modal-wrapper.arco-modal-wrapper-align-center > div > div:nth-child(3) > div.arco-modal-content > div > div.flex.flex-col.mt-12.pt-6 > div:nth-child(1) > div.contact-info__itemText--VjqIi.flex"
				if len(data.select(css2)) > 0:
					news_name = driver.find_element_by_xpath(Whatsapp_xpaths+"/span[1]").text
					if 'Whatsapp' in news_name:
						Whatsapp = driver.find_element_by_xpath(Whatsapp_xpaths+"/span[2]").text
						print("手机通讯："+Whatsapp)
					else:
						Whatsapp = ''
						print("手机通讯："+Whatsapp)
					if '邮箱' in news_name:
						email_1 = driver.find_element_by_xpath(Whatsapp_xpaths+"/span[2]").text
						email_2 = driver.find_element_by_xpath(Whatsapp_xpaths+"/span[3]").text
						email = email_1+email_2
						print("邮箱地址："+email)
					else:
						email_xpaths = "/html/body/div[3]/div[2]/div/div[3]/div[2]/div/div[3]/div[2]/div[1]"
						css3 = "body > div:nth-child(7) > div.arco-modal-wrapper.arco-modal-wrapper-align-center > div > div:nth-child(3) > div.arco-modal-content > div > div.flex.flex-col.mt-12.pt-6 > div:nth-child(2) > div.contact-info__itemText--VjqIi.flex"
						if len(data.select(css3)) > 0:
							email_1 = driver.find_element_by_xpath(email_xpaths+"/span[2]").text
							email_2 = driver.find_element_by_xpath(email_xpaths+"/span[3]").text
							email = email_1+email_2
							print("邮箱地址："+email)
						else:
							email = ''
							print("邮箱地址："+email)
					quchong_data = is_folder(folder_quchong)
					if "_&_"+name_1+"_&_" not in quchong_data:
						data_all = name_1+","+name_2+","+etc_count+","+view_count+","+video_count+","+gender_mix+","+gender+","+age_mix+","+age+","+Whatsapp+","+email
						# 数据写入本地,如需存储别处自行更改
						WriteInfo(1,folder_data,data_all)

						WriteInfo(1,folder_quchong,"_&_"+name_1+"_&_")
					else:
						print("*******数据已存在********")
				driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/div[3]/button").click()
				time.sleep(1)
			else:
				Whatsapp = ''
				print("手机通讯："+Whatsapp)
				email = ''
				print("邮箱地址："+email)
				quchong_data = is_folder(folder_quchong)
				if "_&_"+name_1+"_&_" not in quchong_data:
					data_all = name_1+","+name_2+","+etc_count+","+view_count+","+video_count+","+gender_mix+","+gender+","+age_mix+","+age+","+Whatsapp+","+email
					# 数据写入本地,如需存储别处自行更改
					WriteInfo(1,folder_data,data_all)

					WriteInfo(1,folder_quchong,"_&_"+name_1+"_&_")
				else:
					print("*******数据已存在********")

		i = i+1
		driver.execute_script('window.scrollBy(0,'+str(scrollTo_len)+')')
		data_tiktok(driver,i)


# 进入网页前期准备工作
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
	# 登录成功点击达人及英国
	driver.find_element_by_xpath(r'//*[@id="root"]/div/div/section/section/aside/div/div/div/div/div[3]/div/div[2]/div[1]/div/span[2]/div/span').click()
	driver.find_element_by_xpath(r'//*[@id="tcm"]/div[2]/div/div/div[1]/div[2]/div[5]/button').click()
	time.sleep(1)
	driver.find_element_by_xpath(r'/html/body/span/div/div[2]/div[2]/span[3]').click()
	driver.find_element_by_xpath(r'//*[@id="tcm"]/div[2]/div/div/div[1]/div[2]/div[5]/button').click()

	if not os.path.exists(folder_jindu):
		data_tiktok(driver,i)
	else:
		txt_file = WriteInfo(3,folder_jindu,'')
		lenn = int(txt_file.split("滑动次数")[1].split(",")[0])
		for x in range(1,lenn+1):
			driver.execute_script('window.scrollBy(0,'+str(scrollTo_len)+')')
			time.sleep(1.5)
		data_tiktok(driver,lenn)



if __name__ == '__main__':
	# 登录邮箱
	name = 'bd@ucom18.com'
	# 登录密码
	password = 'sdskj123-'
	# 滑动计数使用
	i = 0
	# 滑动距离
	scrollTo_len = 396
	# 数据目录
	folder_data = ".\\tikTokDATA.csv"
	# 记录进度目录
	folder_jindu = ".\\进度.txt"
	# 去重使用
	folder_quchong = '.\\去重.txt'
	by_tiktok("https://affiliate.tiktokglobalshop.com/seller/dashboard/tcm/creator-marketplace")