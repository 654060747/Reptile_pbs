#!/usr/local/bin/python3.7
# PhantomJS一款无界面浏览器
# 下载PhantomJS路径：https://phantomjs.org/download.html
# selenium+PhantomJS无界面爬取动态页面；selenium+Chrome+webdriver谷歌有界面；Selenium+Headless+Chrome+webdriver谷歌无界面；Selenium+Headless+Firefox+geckodriver火狐无界面

# selenium+PhantomJS
from selenium import webdriver
import time
# phantomJS路径，没配置环境变量手动指定路径
path = 'E:\\selenium_PhantomJS\\phantomjs-2.1.1-windows\\bin'
# 创建浏览器对象
browser = webdriver.PhantomJS(path)
# 打开百度并操作
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)
# 截图
browser.save_screenshot('./baidu.png')
# 定位搜索框
search = browser.find_element_by_id('kw')
time.sleep(2)
# 在搜索框输入内容
search.send_keys('美女')
time.sleep(2)
# 截图
browser.save_screenshot('./meinv.png')
# 关闭浏览器
browser.quit()

1、selenium+PhantomJS动态抓取网页时，出现如下报错信息
UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
————————————————翻译：selenium已经放弃PhantomJS了，建议使用火狐或者谷歌无界面浏览器
解决方案
selenium版本太高需要降级
通过pip show selenium显示，默认安装版本为3.8.1。
将其卸载pip uninstall selenium，重新安装并指定版本号pip install selenium==2.48.0。

                                                                                                                                         
# Selenium+Headless+Chrome+webdriver 感觉此方式速度有点慢                                                                                                                                       
import requests,json,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# proxy = "183.195.106.118:8118"
# proxy = "118.190.95.43:9001"
ops = Options()
ops.add_argument('--headless')
ops.add_argument('--disable-gpu')
# print('--proxy-server=http://%s' % proxy)
# ops.add_argument('--proxy-server=http://%s' % proxy)
browser = webdriver.Chrome(chrome_options=ops)
# browser = webdriver.Chrome()
# driver.maximize_window()
login_url="https://www.baidu.com"
browser.get(login_url)
time.sleep(2)
# 截图
browser.save_screenshot('./baidu.png')
# 定位搜索框
search = browser.find_element_by_id('kw')
time.sleep(1)
# 在搜索框输入内容
search.send_keys('美女')
time.sleep(1)
# 截图
browser.save_screenshot('./meinv.png')
# 关闭浏览器
browser.quit()                                                                                                                                   
