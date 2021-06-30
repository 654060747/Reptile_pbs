# -*- coding: utf-8 -*-
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""ActionChains方法列表"""
# click(on_element=None) ——单击鼠标左键
# click_and_hold(on_element=None) ——点击鼠标左键，不松开
# context_click(on_element=None) ——点击鼠标右键
# double_click(on_element=None) ——双击鼠标左键
# drag_and_drop(source, target) ——拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开
# key_down(value, element=None) ——按下某个键盘上的键
# key_up(value, element=None) ——松开某个键
# move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
# move_to_element(to_element) ——鼠标移动到某个元素
# move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
# perform() ——执行链中的所有动作
# release(on_element=None) ——在某个元素位置松开鼠标左键
# send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
# send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素



driver = webdriver.Chrome()
login_url="https://sso.ahzwfw.gov.cn/uccp-user/resources/forgetPsd/forgetPsd-phone?callback="
driver.get(login_url)
# 最大界面显示
driver.maximize_window()

driver.find_element_by_xpath(r'//*[@id="forget-step1"]/div[1]/div/span[1]/span/input').send_keys('362427199010230317')
time.sleep(0.5)
driver.find_element_by_xpath(r'//*[@id="forget-step1"]/div[2]/button[1]').click()
time.sleep(1)

# 首先截取当前页面的全图
driver.save_screenshot('./01.png')
# 找到全图要截取的部分区域，得出各点坐标
div = driver.find_element_by_xpath(r'//*[@id="captcha"]/canvas[1]')
# 区域截取的起始点x、y坐标
location = div.location
# 区域截取的图片宽高
size = div.size
print(location)
print(size)
left = div.location['x']
top = div.location['y']
right = div.location['x'] + div.size['width']
bottom = div.location['y'] + div.size['height']
# 根据全图截取区域图片
im = Image.open('./01.png')
im = im.crop((left, top, right, bottom))
im.save('./02.png')

# 拖拽滑块拼图
time.sleep(2)
but = driver.find_element_by_xpath(r'//*[@id="captcha"]/div[2]/div/div')
# 拖拽不成功需要把window.navigator.webdriver置为false
ActionChains(driver).drag_and_drop_by_offset(but,75,0).perform()
time.sleep(4)
