import time
import os
from bs4 import BeautifulSoup
import requests


headers = {

		"token": "13789:1568218817446:159tjC9M9qUMVnPjyqYiSw==",
		"api_version": "17",
		"Content-Type": "application/json; charset=UTF-8",
		"Content-Length": "95",
		"Host": "guatian.jy-tech.com.cn",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/2.5.0",


}


def get_haicj(url):

	data = {"mobile":"18321298725","sign":"eDhwsEUkRfTbRBKjA53LcCA29w8\u003d:1","timestamp":1568219002207}

	rs = requests.post(url, data = data, verify=False)
	rs.encoding = 'utf-8'
	print(rs.status_code)
	print("====请输入验证码:")
	a = input("")


url = "http://guatian.jy-tech.com.cn/rest/sms/verify"
get_haicj(url)
