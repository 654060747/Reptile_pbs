#coding=UTF-8
# PyV8为js解析库
import re,os
import PyV8
import logging
import requests

root_path = ".\\down_car\\"

def CheckDir(dir):
	if not os.path.exists(dir):
	  os.makedirs(dir)
	pass

def write_file(key,value):
	CheckDir(root_path)
	file_name = root_path+"car.csv"
	with open(file_name,'a+') as f:
		writer = f.write(key+":"+value+"\n")

def analysis_js(alljs):
	try:
		ctx = PyV8.JSContext()
		ctx.enter()
		ctx.eval(alljs)
		return ctx.eval('rules')
	except:
		logging.exception('analysis_js === js解析出错')
		return None

def makejs(html):
	try:
		alljs = ("var rules = '';"
				 "var document = {};"
				 "document.createElement = function() {"
				 "      return {"
				 "              sheet: {"
				 "                      insertRule: function(rule, i) {"
				 "                              if (rules.length == 0) {"
				 "                                      rules = rule;"
				 "                              } else {"
				 "                                      rules = rules + '#' + rule;"
				 "                              }"
				 "                      }"
				 "              }"
				 "      }"
				 "};"
				 "document.querySelectorAll = function() {"
				 "      return {};"
				 "};"
				 "document.head = {};"
				 "document.head.appendChild = function() {};"

				 "var window = {};"
				 "window.decodeURIComponent = decodeURIComponent;")

		js = re.findall('(\(function\([a-zA-Z]{2}.*?_\).*?\(document\);)', html)
		for item in js:
			alljs = alljs + item
		return alljs
	except:
		logging.exception('makejs === js匹配出错')
		return None

def main(index):
	try:
		req = requests.get('https://car.autohome.com.cn/config/series/'+str(index)+'.html#pvareaid=102192')
		alljs = makejs(req.text)
		if(alljs == None):
			print('makejs === js匹配为空')
			return
		
		result = analysis_js(alljs)
		if(result == None):
			print('analysis_js === js解析数据为空')
			return

		data = {}
		for item in result.split('#'):
			key = item.split(".")[1].split("::before")[0]
			value = item.split('content:"')[1].split('" }')[0]
			data[key] = value
			print(key+":"+value)
			write_file(key,value)
			
		# print(data)    

	except:
		logging('requests === 请求网页数据失败')

if __name__ == '__main__':
	main(4350)