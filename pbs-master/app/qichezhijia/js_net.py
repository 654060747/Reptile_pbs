#coding=utf-8
import re
import requests
import execjs


def clscontent(alljs):
	try:
		print("=================")
		ctx = execjs.compile(alljs)
		return ctx.eval('rules')
	except:
		print('=========execjs解析失败')
		return None

def makejs(html):
	try:
		# alljs = ("""
		# 	var rules = '';
		# 	var document = {};
		# 	document.createElement = function() {      
		# 		return {              
		# 			sheet: {                      
		# 				insertRule: function(rule, i) {                             
		# 					if (rules.length == 0) {           
		# 						rules = rule;                              
		# 					} else {                    
		# 						rules = rules + '#' + rule;                              
		# 					}                    
		# 				}              
		# 			}      
		# 		}
		# 	};
		# 	document.querySelectorAll = function() {      
		# 		return {};};
		# 	document.head = {};
		# 	document.head.appendChild = function() {};
		# 	var window = {};window.decodeURIComponent = decodeURIComponent;
		# 	""")
		alljs = (
				"var rules = '';"
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
				 "window.decodeURIComponent = decodeURIComponent;"
			)
		js = re.findall('(\(function\([a-zA-Z]{2}.*?_\).*?\(document\);)', html)
		for item in js:
			alljs = alljs + item
		return alljs
	except:
		print('============js匹配不上')
		return None

def main(index):
	try:
		req = requests.get('https://car.autohome.com.cn/config/series/'+str(index)+'.html#pvareaid=102192')
		alljs = makejs(req.text)
		print(alljs)
		if(alljs == None):
			print('makejs error')
			return

		result = clscontent(alljs)
		if(result == None):
			print('clscontent error')
			return

		print(result)
		for item in result.split('#'):
			print(item)
	except:
		print('main function exception')

if __name__ == '__main__':
	main(4350)