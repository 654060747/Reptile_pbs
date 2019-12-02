# # coding=utf-8
# # http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo?shopId=19658572
import requests,re,os
# import json
# from random import choice



# # 代理ip
# proxys = ["111.11.100.13:8060","45.221.77.82:8080","112.109.198.106:3128","60.9.1.80:80","47.106.216.42:8000","116.196.115.209:8080"]
# #1.使用python random模块的choice方法随机选择某个元素
# proxy = choice(proxys)

# proxy_d = "http://"+proxy

# proxies = {
# 	"http":proxy_d
# }

# headers = {
# 	"Accept": "application/json, text/javascript, */*; q=0.01",
# 	"Accept-Encoding": "gzip, deflate",
# 	"Accept-Language": "zh-CN,zh;q=0.9",
# 	"Connection": "keep-alive",
# 	"Cookie": "cy=1; cye=shanghai; _lxsdk_cuid=16c8b100f19c8-01cbe648f3d2a6-5f123917-1fa400-16c8b100f1ac8; _lxsdk=16c8b100f19c8-01cbe648f3d2a6-5f123917-1fa400-16c8b100f1ac8; _hc.v=ae79baa6-5372-4d49-e7e4-4f6b7f976e59.1565701181; s_ViewType=10; _dp.ac.v=27965664-c25d-4923-9e12-c959c90a9088; dper=b20ed38bbb26c76c38c315d5334fc1df1b5863b887494c52e605081861bece046904a5993165e68711f96f6820586e8688779401c12caffdc8e2a7147edc197783f9b2082d2044257b8763523091c1603c077cf6824e44ee58421a340cc18cab; ua=dpuser_4772089894; ctu=6ac4f4c6008f8ac7384c56fdb83150b3e832354ecc039485a11330efea317474; ll=7fd06e815b796be3df069dec7836c3df; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16c950a1014-669-878-ba2%7C%7C57",
# 	"Host": "www.dianping.com",
# 	"Referer": "http://www.dianping.com/shop/19658572",
# 	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
# 	"X-Requested-With": "XMLHttpRequest",
# }

# # headers = {
# # 	"Accept": "application/json, text/javascript, */*; q=0.01",
# # 	"Referer": "http://www.dianping.com/shop/19658572",
# # 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
# # 	"X-Requested-With": "XMLHttpRequest",
# # }

# url="http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo?shopId=19658572"
# rs = requests.get(url,headers=headers,proxies=proxies,verify=False)
# print(rs)
# rs.encoding = 'utf-8'
# data = json.loads(rs.text)
res = re.compile(r"<.*?>(.*?)<.*?>")
re = r"<.*?>"
# 地址
# data_address = data["msg"]["shopInfo"]["address"]
data_address = '1<d class="num">&#xf083;</d>11<d class="num">&#xe6c9;</d><d class="num">&#xe208;</d><d class="num">&#xf33b;</d><d class="num">&#xe6c9;</d><d class="num">&#xf0d2;</d><d class="num">&#xe6c9;</d><d class="num">&#xf33b;</d>'
i = 0
for x in data_address.split("<"):
	# print(x)
	for y in x.split(">"):
		if i == 0 or i%2 == 0:
			print(y)
		i = i+1
# list_y = re.findall(res, data_address)

# 电
# print(list_y)
# print(data_phone_one)
# print(data_phone_two)