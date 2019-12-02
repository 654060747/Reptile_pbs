# -*- coding: utf-8 -*-
# 调用浏览器自动登录获取Cookie
import requests,json,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

proxy = "27.17.45.90:43411"
# proxy = "118.190.95.43:9001"
# proxy = "58.52.50.246:9999"
ops = Options()
# ops.add_argument('--headless')
# ops.add_argument('--no-sandbox')
# ops.add_argument('--disable-dev-shm-usage')
# ops.add_argument('--disable-gpu')
def ElementProxyGetCookie():
	


	print('--proxy-server=http://%s' % proxy)
	# ops.add_argument('--user-agent=%s' % ua)
	# ops.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data')
	ops.add_argument('--proxy-server=http://%s' % proxy)
	driver = webdriver.Chrome( chrome_options=ops)
	# driver = webdriver.Chrome()


	# driver.maximize_window()

	login_url="https://account.dianping.com/login?redir=http://www.dianping.com"

	driver.get(login_url)
	driver.switch_to.frame(driver.find_element_by_xpath(r'//*[@id="J_login_container"]/div/iframe'))
	driver.find_element_by_class_name("bottom-password-login").click()#tab-account

	# 发送验证码方式
	# driver.find_element_by_id("mobile-number-textbox").send_keys('18321298725')
	# driver.find_element_by_xpath(r'//*[@id="send-number-button"]').click()
	# time.sleep(2)
	# boxStatic = driver.find_element_by_xpath(r'//*[@id="yodaBox"]')
	# # print(boxStatic)
	# driver.execute_script("arguments[0].style='left: 200px;';", boxStatic)
	# driver.switch_to.default_content()
	# time.sleep(5)
	# key = input('请输入验证码:')
	# driver.find_element_by_id("number-textbox").send_keys(key)

	# 密码方式
	driver.find_element_by_id("tab-account").click()
	driver.find_element_by_id("account-textbox").send_keys('xxx')
	driver.find_element_by_id("password-textbox").send_keys('xxx')

	driver.find_element_by_id("login-button-account").click()
	driver.switch_to.default_content()

	# 获取cookie信息
	cookies = driver.get_cookies()


	
	result = {}
	for each in cookies:

	   result[each['name']] = each['value']
	return result


	# jsonCookies = json.dumps(cookies)
	# with open('/tmp/jiayuan.json', 'w') as f:
	#     f.write(jsonCookies)

	# with open('/tmp/jiayuan.json','r',encoding='utf-8') as f:
	#     listCookies=json.loads(f.read())
	# cookie = [item["name"] + "=" + item["value"] for item in listCookies]
	# cookiestr = '; '.join(item for item in cookie)


	# driver.quit()

