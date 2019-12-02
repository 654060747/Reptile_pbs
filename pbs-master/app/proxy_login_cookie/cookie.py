#  coding= utf-8

from selenium.webdriver.common.keys import Keys
import random
import requests,json
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# proxy = "27.17.45.90:43411"
# ops = Options()

def dazhongdianping_login(phone):
   


   '''
   大众点评模拟登陆,随机睡眠
   :param phone: 手机号
   :return: 登陆的cookie
   '''
   # print('--proxy-server=http://%s' % proxy)
   # ops.add_argument('--user-agent=%s' % ua)
   # ops.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
   # ops.add_argument('--proxy-server=http://%s' % proxy)
   # driver = webdriver.Chrome(chrome_options=ops)
   driver = webdriver.Chrome()

   driver.delete_all_cookies()

   driver.get('https://account.dianping.com/login')
   # assert "Python" in driver.title
   # elem = driver.find_element_by_id('kw')
   # elem.send_keys("大众点评")
   # elem.send_keys(Keys.RETURN)
   # 自动点击登陆
   # sleep(random.uniform(1, 3))
   # elem = driver.find_element_by_xpath(r'//*[@id="top-nav"]/div/div[2]/span[2]/a[1]')
   # elem.click()
   # 切入网页框架
   driver.switch_to.frame(driver.find_element_by_xpath(r'//*[@id="J_login_container"]/div/iframe'))  # 切入
   # 点击账号登录
   driver.find_element_by_xpath(r"/html/body/div/div[2]/div[5]/span").click()

   # print(driver.page_source)
   # 输入验证码
   driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[:3])
   driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[3:7])
   driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[7:])

   # 点击获取验证码,等待输入
   driver.find_element_by_xpath(r'//*[@id="send-number-button"]').click()
   key = input('请输入验证码:')
   driver.find_element_by_xpath(r'//*[@id="number-textbox"]').send_keys(key)
   # 点击登陆
   driver.find_element_by_xpath(r'//*[@id="login-button-mobile"]').click()
   driver.switch_to.default_content() # 切出框架
   # 处理cookie
   cookie = driver.get_cookies()
   # result = {}
   # for each in cookie:

   #    result[each['name']] = each['value']
   return cookie



print(dazhongdianping_login('xxx'))
