# encoding='utf-8'
import time,requests,re,json


def by_qczj(url):

	headers = {

		'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'accept-encoding':'gzip, deflate, br',
		'accept-language':'zh-CN,zh;q=0.9',
		'cache-control':'max-age=0',
		'cookie':'fvlid=1574941434679IH3XUlie44; sessionid=5719F0F6-EA7E-41E3-9B7C-E9846767E380%7C%7C2019-11-28+19%3A43%3A55.066%7C%7C0; autoid=e8fd6d70a08a60b4a8bd32d7eb94d1e0; ahpau=1; __ah_uuid_ng=c_5719F0F6-EA7E-41E3-9B7C-E9846767E380; sessionuid=5719F0F6-EA7E-41E3-9B7C-E9846767E380%7C%7C2019-11-28+19%3A43%3A55.066%7C%7C0; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1574941435,1574941492; JSESSIONID=DC51AB8D7A590730616D59D7171EFA92; __utma=1.808987616.1574942907.1574942907.1574942907.1; __utmc=1; __utmz=1.1574942907.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ahsids=2561_2968_4350_65_18_812; cookieCityId=110100; ahpvno=195; pvidchain=102192; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1574948484; sessionip=101.80.148.247; v_no=196; sessionvid=0EE0F4B0-B9D3-4765-9F9A-F5E755356EAD; area=310115; ref=www.baidu.com%7C0%7C0%7C0%7C2019-11-28+21%3A41%3A25.604%7C2019-11-28+19%3A44%3A25.045',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

	}

	rs = requests.get(url, headers=headers, verify=False)
	rs.encoding = 'utf-8'
	# data = BeautifulSoup(rs.text, "lxml")
	data = rs.text
	pattern  = re.compile(r'var config = (.*?);')
	# config_match = pattern.match(data)
	config_match = re.findall(pattern,data)
	if config_match:
		# print(config_match)
		config_json = json.loads(config_match[0])
		config_data = config_json['result']['paramtypeitems']
		for one_data in config_data:
			car_name = one_data['name']
			print(car_name)

	else:
		print("config匹配失败")



urls = ["https://car.autohome.com.cn/config/series/4350.html#pvareaid=102192"]	

for url in urls:
	by_qczj(url)

