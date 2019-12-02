# coding=utf-8
import requests
import random,math,time
from bs4 import BeautifulSoup
import pyquery
import re


def chinese_svg_dict(svg_kj_url,i):
	# ua = UserAgent()
	# User_Agent = ua.random

	# url = 'http://www.dianping.com/shop/27227334'

	# headers = {
	# 		'Referer':url,
	#         'Host':'www.dianping.com',
	#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
	#      }
	# resp = requests.get(url, headers=headers)
	# resp.encoding = 'utf-8'
	# html = resp.text

	# css_url_regex = re.compile(r'href="//(s3plus.meituan.net.*?)\"')
	# css_url = re.search(css_url_regex, html).group(1)
	# css_url = 'http://' + css_url
	css_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/5de9a9098d8d30d7d65f16ab93871bb4.css'

	# 获取css文件
	css_resp = requests.get(css_url)
	css_html = css_resp.content.decode('utf-8')

	# 提取svg图片的url
	# regex_kj_svg = re.compile(r'e\[class\^="tf"\][\s\S]*?url\((.*?)\)')
	# svg_kj_url = re.search(regex_kj_svg, css_html).group(1)
	# svg_kj_url = 'http:' + svg_kj_url
	# svg_kj_url = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/ef6ed4846e1531923f99d63a3d260216.svg'

	# 获取svg文件匹配的内容
	svg_kj_resp = requests.get(svg_kj_url)
	svg_kj_html = svg_kj_resp.text
	regex_svg_css = re.compile(r'<textPath xlink:href="#(.*?)" textLength=".*?">(.*?)</textPath>')
	svg_text = re.findall(regex_svg_css, svg_kj_html)
	# print(svg_text)

	# 存储('18', 'M0', '748', 'H600') eg:(x坐标，未知，y坐标，未知)
	svg_y_r = r'<path id="(.*?)" d="M0 (.*?) H600"/>'
	list_y = re.findall(svg_y_r, svg_kj_html)
	# print(list_y)

	# 生成svg加密字体库字典
	dict_avg = {}
	for data in svg_text:
	    dict_avg[data[0]] = list(data[1])
	# print(dict_avg)
	# print(list_y)
	# print(int(list_y[0][1]))

	# 匹配出以tf开头的class属性
	if i == 1:
		regex_kjs_css = re.compile(r'(cw\w{3})\{background:(\-\d+\.\d+)px (\-\d+\.\d+)px')
		kjs = re.findall(regex_kjs_css, css_html)
		# print(kjs)
		# 把tag值对应的x轴下标以及y轴坐标放入字典 #tag值=>tfsz1 tfxxx
		kjs_dict = []
		for one_kjs in kjs:
			# x轴下标
			x_kjs = math.floor(float(one_kjs[1].split('-')[1])/14)
			# y轴偏移量
			y_kjs = int(float(one_kjs[2].split('-')[1]))
			kjs_dict.append([one_kjs[0],x_kjs,y_kjs])
		# print(kjs_dict)
		
		tag_dict_one = {}
		for one_dict in kjs_dict:
			count = 0
			for y in list_y:
				if one_dict[2]/int(y[1]) <= 1:
					count = count + 1
					if count > 1:
						break
					# print(one_dict[2])
					# print(dict_avg.get(y[0])[one_dict[1]])
					# print(one_dict[1])
					# print(one_dict[0])
					tag_dict_one[one_dict[0]] = dict_avg.get(y[0])[one_dict[1]]
		return tag_dict_one
	elif i == 2:
		regex_kjs_css = re.compile(r'(vq\w{3})\{background:(\-\d+\.\d+)px (\-\d+\.\d+)px')
		kjs = re.findall(regex_kjs_css, css_html)
		# print(kjs)
		# 把tag值对应的x轴下标以及y轴坐标放入字典 #tag值=>tfsz1 tfxxx
		kjs_dict = []
		for one_kjs in kjs:
			# x轴下标
			x_kjs = math.floor(float(one_kjs[1].split('-')[1])/14)
			# y轴偏移量
			y_kjs = int(float(one_kjs[2].split('-')[1]))
			kjs_dict.append([one_kjs[0],x_kjs,y_kjs])
		# print(kjs_dict)
		
		tag_dict_two = {}
		for one_dict in kjs_dict:
			count = 0
			for y in list_y:
				if one_dict[2]/int(y[1]) <= 1:
					count = count + 1
					if count > 1:
						break
					# print(one_dict[2])
					# print(dict_avg.get(y[0])[one_dict[1]])
					# print(one_dict[1])
					# print(one_dict[0])
					tag_dict_two[one_dict[0]] = dict_avg.get(y[0])[one_dict[1]]
		return tag_dict_two

	elif i == 3:
		regex_kjs_css = re.compile(r'(ra\w{3})\{background:(\-\d+\.\d+)px (\-\d+\.\d+)px')
		kjs = re.findall(regex_kjs_css, css_html)
		# print(kjs)
		# 把tag值对应的x轴下标以及y轴坐标放入字典 #tag值=>tfsz1 tfxxx
		kjs_dict = []
		for one_kjs in kjs:
			# x轴下标
			x_kjs = math.floor(float(one_kjs[1].split('-')[1])/12)
			# y轴偏移量
			y_kjs = int(float(one_kjs[2].split('-')[1]))
			kjs_dict.append([one_kjs[0],x_kjs,y_kjs])
		# print(kjs_dict)
		
		tag_dict_three = {}
		for one_dict in kjs_dict:
			count = 0
			for y in list_y:
				if one_dict[2]/int(y[1]) <= 1:
					count = count + 1
					if count > 1:
						break
					# print(one_dict[2])
					# print(dict_avg.get(y[0])[one_dict[1]])
					# print(one_dict[1])
					# print(one_dict[0])
					tag_dict_three[one_dict[0]] = dict_avg.get(y[0])[one_dict[1]]
		return tag_dict_three

		
def chinese_dict():
	url_one = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/ef6ed4846e1531923f99d63a3d260216.svg'
	url_two = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/319c6f0b5ca12b8a36e2630cff47ad2b.svg'
	url_three = 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/99200ec2483ce4a9789ffecad45b017b.svg'
	i = 1
	j = 2
	z = 3
	dict1 = chinese_svg_dict(url_one,i)
	dict2 = chinese_svg_dict(url_two,j)
	dict3 = chinese_svg_dict(url_three,z)
	tag_dict = {**dict1, **dict2, **dict3}
	return tag_dict

