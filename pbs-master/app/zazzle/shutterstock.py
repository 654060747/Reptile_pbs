# coding=utf-8
import time,os,re
import requests
from contextlib import closing
import threading

# 1.安装python3  ==> https://pan.baidu.com/s/1RlH06qN9j4HTormagSmTqw  提取码zazz  下载3.7版本
# 2.安装bs4  ==> pip install bs4 -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com


# 需要修改的位置
# 要搜索的关键字
keywords = ['dogs']
# 第几页
page = 1
# 可能会过期的cookie值
cookie_ = 'sb_slug-image-lohp_tBxD04db3efOtfqyvxXfu=true; _gcl_au=1.1.1812269219.1622815094; OptanonAlertBoxClosed=2021-06-04T13:58:14.721Z; __ssid=ed3d1a186a12e150c41b8834410e5cd; _ym_uid=1622815111732218185; _ym_d=1622815111; _cs_c=1; _ym_isad=1; visitor_id=65490781586; _actts=1622815086.1622815086.1622854023; _actvc=2; AMP_TOKEN=%24NOT_FOUND; _ce.s=v11.rlc~1622858097514; anonymousRendering=supported; did=J7JopOoYjGh1UYCNk1TFtT52NnCkHfRcajtZx7amhHw=; IR_gbd=shutterstock.com; IR_PI=1d688d20-c53d-11eb-bf70-42010a24662e%7C1622945493794; locale=en; search=%2Fsearch%2Fgame%3F; sstk_anonymous_id=%221c5d59f2-fb38-406f-9841-f99bfce7b920%22; ajs_anonymous_id=%221c5d59f2-fb38-406f-9841-f99bfce7b920%22; visit_id=71325944298; footage_search_tracking_id=674c7513-e952-450e-9df0-f60622e8554c; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jun+05+2021+10%3A20%3A23+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.10.0&hosts=&consentId=be796b1f-c2b6-46fd-b85e-b88403de8b5a&interactionCount=3&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0005%3A1%2CC0003%3A1%2CC0007%3A1&AwaitingReconsent=false&geolocation=DE%3BHE; _cs_mk=0.09851316059842286_1622854034639; _fbp=fb.1.1622815118671.1468909022; _uetsid=f0714b20c53c11ebb4a6b93e9caab8b3; _uetvid=f071fe90c53c11eb83e09fbf91cb34d9; IR_1305=1622859626812%7C0%7C1622859626812%7C%7C; stc114920=env:1622854037%7C20210706004717%7C20210605025027%7C22%7C1044418:20220605022027|uid:1622815113998.2046621652.6593451.114920.369201569.:20220605022027|srchist:1044418%3A1622854037%3A20210706004717:20220605022027|tsa:1622854037277.1851232566.0344825.8395015300585171.:20210605025027; _cs_ex=1596812801; _CEFT=Q%3D%3D%3D; extole_access_token=9CMOLAKJ66U69TBBIQOALIKC3B; fo=0; _ga=GA1.2.1161123811.1622815118; _gid=GA1.2.839296772.1622815118; ajs_anonymous_id=%221c5d59f2-fb38-406f-9841-f99bfce7b920%22; _actcc=81.25.89.30; _actmu=44562c28-2ff0-4f11-a5e4-68e3664a267d; _actms=90e95e22-1ec3-4556-a5fe-7ff6d6a41c74; _4c_=dVJNj9sgEP0rK84hMdhgyK3dStWe26rHyMAQW0lsC3DcdJX%2F3iFfK6WtDzbzZt543jzeydxCT9ZMcq6ErvFbyQXZwSmS9TuxY34f82sKe7ImbUpjXK9W8zwvYzulBCGmwe6WdjisIjTBtqttcwCyINAjj4zB4TnGtItdAgS6Q7PN6TiZaEM3pm7ov5%2FGnJp6B77rITOmCOFbatKEc5DtBDEhaIepT%2BGUSyOGTT%2F0p8MwxTeHELPCCe059aZUtCqkp1pVjHqtjbdQG82LSw%2BX%2F8X0krElRyD9xrBSOTeGwU02bdJ1nhnMS3Q7TDg4dhY2c%2BdSm8mllB9oC922TQjXUmV0DLkET3PXu2F%2BsMpSfIAPkiwzyYRhRsUYv7ZhOMCL0IgOWfzPCyHrDeAhhEtVXuB1n88u3DLo4FMy68uOsDz6frDNPtPRfCSAzTZg%2BJm%2FYvz10%2BbH25dcyyRjvFS4qssNYYIxRc4L8ut6ZXQlC651UeIaE94PJasiP1gROne7O8Ra4wreFNRztKcqFKNKCkO5K5jz2nAoPbn1LAtZikIoqRU2OXb3HnWjlKgsp%2BAN0EoDo0ZISxU6Jw1Yr7ghj7mUZBXXopa3uZi6jzXubx3ZR3FdVkLV%2FC6CVQ8R4%2FFeLZ80K63%2B1nx1keISKfT%2F5%2F5jX%2BfzHw%3D%3D'




headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	# 注意此处会把数据打包
	# 'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Cookie':cookie_,
	'Host':'www.shutterstock.com',
	'If-Modified-Since':'Sat, 05 Jun 2021 02:01:46 GMT',
	'If-None-Match':'W/"3a836-P0NamS9NuvL6z69RlATS32Wx3Ys"',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
}


# 使用多线程下载图片
class MyThread(threading.Thread):
    """docstring for MyThread"""
    def __init__(self,url_img,img_dir,img_name,folder_name):
        super(MyThread, self).__init__()
        self.url_img = url_img
        self.img_dir = img_dir
        self.img_name = img_name
        self.folder_name = folder_name      
    def run(self):
        DownloadImg(self.url_img,self.img_dir,self.img_name,self.folder_name)
        # time.sleep(1)
        print("线程："+threading.current_thread().getName()+"使用结束")


# 创建目录
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


# 数据写入
def WriteInfo(folder_name, data):
    with open(folder_name, 'a+', encoding='utf-8') as f:
        writer = f.write(data+"\n")


# 页码覆盖写入
def WritePage(folder_name, data):
    with open(folder_name, 'w', encoding='utf-8') as f:
        writer = f.write(data+"\n")


#下载图片
def DownloadImg(img_url, dir_name, img_name, folder_name):
	try:
		with closing(requests.get(img_url, stream=True, timeout=20)) as r:
			rc = r.status_code
			if 299 < rc or rc < 200:
				print('returnCode%s\t%s' % (rc, img_url))
				return
			content_length = int(r.headers.get('content-length', '0'))
			if content_length == 0:
			    print('size0\t%s' % img_url)
			    # return
			try:
			    with open(os.path.join(dir_name, img_name), 'wb') as f:
			        for data in r.iter_content(1024):
			            f.write(data)
			        print('==========图片下载成功=========')
			except:
			    print('保存失败可能含有特殊字符 \t%s' % img_url + '\n' + '失败图片已保存到"失败图片.csv"')
			    WriteInfo(folder_name+'/'+'失败图片.csv',img_url+","+img_name.split(".jpg")[0])
	except:
	    print('图片下载失败可能网络问题 \t%s' % img_url + '\n' + '失败图片已保存到"失败图片.csv"')
	    WriteInfo(folder_name+'/'+'失败图片.csv',img_url+","+img_name.split(".jpg")[0])


# 进入id详情页
def by_img_details(url_id, key, i):
	rs = requests.get(url_id, headers=headers, verify=False)
	# time.sleep(1)
	# data = BeautifulSoup(rs.text, "lxml")
	data = rs.text
	if rs.status_code == 200:
		ID = url_id.split('-')[-1]
		print("Id…………"+ID)
		# "description":"Pickle-ball word collage on blue background for sports, fitness, and recreation concepts. ",
		regex_json = re.compile(r'"description":"(.*?)",')
		json_data = regex_json.findall(data)
		if len(json_data) > 0:
			title_name = json_data[0]
			print("标题…………"+title_name)
		else:
			title_name = ''
		# "thumbnailUrl":"https://image.shutterstock.com/image-vector/pickleball-word-collage-on-blue-260nw-1903457593.jpg" 
		regex_json = re.compile(r'"thumbnailUrl":"(.*?)"')
		json_data = regex_json.findall(data)
		if len(json_data) > 0:
			url_img = json_data[0]
			print("图片链接…………"+url_img)
		else:
			url_img = ''
		# href="/search/word+collage">word collage</a>
		# href="/search/similar/1903457593">See all</a>
		regex_json = re.compile(r'href="/search/[^\d]+">(.*?)</a>')
		json_data = regex_json.findall(data)
		if len(json_data) > 0:
			tags = "&".join(tag for tag in json_data)
			print("Tags…………"+tags)
		else:
			tags = ''
		all_data = ID + "," + url_img + "," + title_name.replace(',','&') + "," + tags
		txt_dir = './shutterstock_去重.txt'
		if not os.path.exists(txt_dir):
			open(txt_dir,'w')
		f = open(txt_dir)
		txt_file = f.read()
		f.close()
		if ID not in txt_file:
			folder_name = "./" + key
			CheckDir(folder_name)
			file_dir = folder_name + "/" + "data.csv"
			WriteInfo(file_dir,all_data)
			img_dir =  folder_name + '/' + 'img'
			CheckDir(img_dir)
			img_name = ID + '.jpg'
			# DownloadImg(url_img,img_dir,img_name,folder_name)
			thread = MyThread(url_img,img_dir,img_name,folder_name)
			thread.start()
			# thread.join()
			if i%90 == 0:
				time.sleep(4)
			WriteInfo(txt_dir,ID)
		else:
			print("数据已存在")


# 首页取图片链接与id详情页链接
def by_img_id(start_url,key,strs):
	rs = requests.get(start_url, headers=headers, verify=False)
	# time.sleep(1)
	# data = BeautifulSoup(rs.text, "lxml")
	data = rs.text
	if rs.status_code == 200:
		# </button><a href="/image-vector/seamless-abstract-pattern-pixel-game-style-1435821359"
		regex_json = re.compile(r'</button><a href="(.*?)"')
		json_data = regex_json.findall(data) 
		if len(json_data) > 0:
			# 单个数据测试使用
			# by_img_details('https://www.shutterstock.com'+json_data[0], key)
			print("当前页有"+str(len(json_data))+"条数据")
			i = 0
			for url_xp in json_data:
				i=i+1
				print('\n\n\n'+strs+"的第"+str(i)+"个")
				url = 'https://www.shutterstock.com'+url_xp
				by_img_details(url, key, i)


# 进入首页取页码
def by_to_shutterstock(url_one,key):
	rs = requests.get(url_one, headers=headers, verify=False)
	# time.sleep(0.5)
	data = rs.text
	# data = BeautifulSoup(rs.text, "lxml")
	if rs.status_code == 200:
		regex_json = re.compile(r'min="1" step="1" max="(.*?)"')
		json_data = regex_json.findall(data)
		if len(json_data) > 0:
			print("关键字"+key+"共有"+json_data[0]+"页数据")
			for x in range(page,int(json_data[0])+1):
			# 单页测试使用
			# for x in range(page,2):
				start_url = url_one + '&page=' + str(x)
				strs = "已经爬到关键字"+key+"第"+str(x)+"页"
				WritePage('./shutterstock_进度.txt',strs)
				by_img_id(start_url,key,strs)
		else:
			print("此关键字"+key+"没有数据")


for key in keywords:
	url = 'https://www.shutterstock.com/search/'+key+'?mreleased=false'
	by_to_shutterstock(url,key)

