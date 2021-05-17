# coding=utf-8
import time,os,re,json,math
import requests
from bs4 import BeautifulSoup
from contextlib import closing

# 1.安装python3  ==> https://pan.baidu.com/s/1RlH06qN9j4HTormagSmTqw  提取码zazz  下载3.7版本
# 2.安装bs4  ==> pip install bs4 -i http://pypi.douban.com/simple  --trusted-host pypi.douban.com


# 需要修改的位置
# 要搜索的关键字
keywords = ['camper pillow','sofa','dog']
# 第几页
page = 1
# 当前页的第几个
page_count = 1
# 可能会过期的cookie值
cookie_ = "us=274271EC-A3B4-42EE-8DFD-394ABB80191E; _gcl_au=1.1.1166412673.1620806103; _ga=GA1.2.16331678.1620806103; _gid=GA1.2.1812838852.1620806103; _scid=7ba45869-d2cf-49d2-92ba-4042be4876db; _pxhd=842a1d7c8d4104e793a9eaefac95f722ed878fb422b320fb4b5ecc1ba15d8d1f:5e703410-b2f7-11eb-a158-836446943baf; _pxvid=5e703410-b2f7-11eb-a158-836446943baf; __gads=ID=7148285d1067e17c:T=1620806456:S=ALNI_MYpMHTjBXbtyuLkEUijbStk51SVzw; general_maturity=1; zm=AQABAAAAchYAABRwmOI9YXDcU15WPQgos-XdLXvW-I6JmTYec9KxQTaiFx4zm_jIgcMQ4mONCNhBTRZDdAGy63vz4sF41zXUHAPJmtSkCGP4OBzEElvdMMveOejv6su6HXkvYsxo0nlUEpHMoRW6; zs=F592657C-DDBC-4AEE-A6C8-C76BEA622709%7c0%7c13265381920%7cAQABAAAAchYAABRFFlETYMV8AahITzBM4NMtcbRMo3qFUTlAlF9Vean0CdA9x-0Ir9oIPSZ-nuUEUi3aKtbA%7c; NSC_xxx01=28d4a3da20d4e0cbb74fdc9a6ab9936fef06d9a5f47ba533650667b054b957dde644bab7; bx=qs%3d%26qs_x%3d132653855335127665%26promoanim%3d1%26promoanim_x%3d132654107335752535; NSC_smw=2618a3ce6ac8f1327f9a397007acd623ccbd0e837ed27b04f4f280c13966309d75a668e8; _uetsid=5c1ae7f0b2f711eb8c99bb592a495ed0; _uetvid=5c1b41f0b2f711eba4d9f5185aa215f0; _px2=eyJ1IjoiOTk3NmJiMzAtYjNlNS0xMWViLWFhMzQtNWJjMzViZDE0MWJkIiwidiI6IjVlNzAzNDEwLWIyZjctMTFlYi1hMTU4LTgzNjQ0Njk0M2JhZiIsInQiOjE2MjA5MDg3MzU5MDMsImgiOiI5M2E4OWJlZTVmN2RiNzcxMzRhYmQzMGU4OGI0YWU4MjI5MjRlMGE0YzYzZjI2MGRiNWQ1YTQyNTNmYWVjM2E4In0=; bs=pis%3d9%26zshopurl%3dz%2fs%2fsofa"





headers = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"accept-encoding": "gzip, deflate, br",
	"accept-language": "zh-CN,zh;q=0.9",
	"cache-control": "max-age=0",
	"cookie": cookie_,
	"sec-ch-ua-mobile": "?0",
	"sec-fetch-dest": "document",
	"sec-fetch-mode": "navigate",
	"sec-fetch-site": "same-origin",
	"sec-fetch-user": "?1",
	"upgrade-insecure-requests": "1",
	"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
}


def select_css(count,data,css,title):
	if count == 1:
		return data.select(css)
	if count == 2:
		return data.select(css)[0].getText().strip()
	if count == 3:
		return data.select(css)[0].get(title)


# 创建目录
def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass


# 数据写入
def WriteInfo(folder_name, data):
    with open(folder_name, 'a+', encoding='utf-8') as f:
        writer = f.write(data+"\n")


#下载图片
def DownloadImg(img_url, dir_name, img_name, folder_name):
    try:
        with closing(requests.get(img_url, headers=headers, stream=True, timeout=10)) as r:
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
                WriteInfo(folder_name+'/'+'失败图片.csv',img_url)
    except:
        print('图片下载失败可能网络问题 \t%s' % img_url + '\n' + '失败图片已保存到"失败图片.csv"')
        WriteInfo(folder_name+'/'+'失败图片.csv',img_url)


# 进入id详情页
def by_img_details(url_id, key, title_name):
	rs = requests.get(url_id, headers=headers, verify=False)
	time.sleep(1)
	data = BeautifulSoup(rs.text, "lxml")
	data_ = rs.text
	if rs.status_code == 200:
		ID = url_id.split('-')[1]
		print("id…………"+ID)
		css = 'head > meta[property="og:image"]'
		pic_str = select_css(3, data, css, 'content')
		if '&' in pic_str:
			net_pic = pic_str.split('&')[0]
			url_img = re.sub(r'_\d+.jpg',r'_307.jpg',net_pic) + '&rvtype=content'
		else:
			net_pic = pic_str.split('?')[0]
			url_img = re.sub(r'_\d+.jpg',r'_307.jpg',net_pic) + '?rvtype=content'
		print("图片链接…………"+url_img)
		print("标题…………"+title_name)
		regex_json = re.compile(r'"tags":{"tags":\[.*?]}]}')
		json_data = regex_json.findall(data_)
		# 取Tags时会出现两种情况
		if len(json_data) > 0 and len(str(json_data)) < 6000:
			json_data = "{"+json_data[0]+"}"
			tags_data = json.loads(json_data)
			all_tags = tags_data['tags']['tags']
			tag_01 = all_tags[0]['displayName'] + ":" + '&'.join( text['text'] for text in all_tags[0]['tags'])
			print("tag 1…………"+tag_01)
			tag_02 = all_tags[1]['displayName'] + ":" + '&'.join( text['text'] for text in all_tags[1]['tags'])
			print("tag 2…………"+tag_02)
		else:
			css = 'div.ZazzleWwwProductPageTags > div:nth-child(1) > strong'
			if len(select_css(1, data, css, '')) > 0:
				tags_top_01 = select_css(2, data, css, '')
				css = 'div.ZazzleWwwProductPageTags > div:nth-child(1)'
				tags_contant_01 = select_css(2, data, css, '').replace('\r','').replace('\n','').replace('\t','').replace(', ',',').strip().split(tags_top_01)[1].replace(',','&')
				tag_01 = tags_top_01 + ":" + tags_contant_01
				print("tag 1…………"+tag_01)
				css = 'div.ZazzleWwwProductPageTags > div:nth-child(2) > strong'
				tags_top_02 = select_css(2, data, css, '')
				css = 'div.ZazzleWwwProductPageTags > div:nth-child(2)'
				tags_contant_02 = select_css(2, data, css, '').replace('\r','').replace('\n','').replace('\t','').replace(', ',',').strip().split(tags_top_02)[1].replace(',','&')
				tag_02 = tags_top_02 + ":" + tags_contant_02
				print("tag 2…………"+tag_02)
			else:				
				tag_01 = ''
				tag_02 = ''
		all_data = ID + "," + url_img + "," + title_name + "," + tag_01 + "," + tag_02
		txt_dir = './去重.txt'
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
			DownloadImg(url_img,img_dir,img_name,folder_name)
			WriteInfo(txt_dir,ID)
		else:
			print("数据已存在")


# 首页取图片链接与id详情页链接
def by_img_id(start_url,key,i):
	rs = requests.get(start_url, headers=headers, verify=False)
	time.sleep(1)
	data = BeautifulSoup(rs.text, "lxml")
	if rs.status_code == 200:
		# css公共部分
		public_css = '#main > div.WwwPage_root > div.WwwPage_headerAndContent > main > div > div:nth-child(3) > div > div.SearchResults.SearchResults--ps60 > div >'
		css = public_css+'div.SearchResultsGridCell'
		div_list = select_css(1, data, css, '')
		# print(len(div_list))
		for x in range(page_count+1,len(div_list)+2):
			css = public_css+'div:nth-child('+str(x)+') > div.SearchResultsGridCell-absolutePositionedContainer > div.SearchResultsGridCell-realviewContainer > a'
			url_id = select_css(3, data, css, 'href')
			print("\n\n\n已经爬到关键字"+key+"第"+str(i)+"页的"+"第"+str(x-1)+"个===="+url_id)
			css = 'div:nth-child('+str(x)+') > div.SearchResultsGridCell-absolutePositionedContainer > div.SearchResultsGridCell-info > a > span'
			title_name = select_css(2, data, css, '')
			by_img_details(url_id, key, title_name)


# 进入首页取页码
def by_to_zazzle(url_one,key):
	rs = requests.get(url_one, headers=headers, verify=False)
	time.sleep(0.5)
	data = BeautifulSoup(rs.text, "lxml")
	if rs.status_code == 200:
		css = '#main > div.WwwPage_root > div.WwwPage_headerAndContent > main > div > div > div > div.ActionBar > div > div > div > div.ActionBar-titleRow > div.ActionBar-numResults'
		# 有总个数result继续
		if len(select_css(1,data,css,'')) > 0:
			sum_result = int(select_css(2, data, css, '').split(' result')[0].replace(',',''))
			# print(sum_result)
			if sum_result > 900:
				for x in range(page,17):
					start_url = url_one + '?pg=' + str(x)
					by_img_id(start_url,key,x)
			else:
				for x in range(page,math.ceil(sum_result / 60)+1):
					start_url = url_one + '?pg=' + str(x)
					by_img_id(start_url,key,x)
		else:
			print("此关键字"+key+"没有数据")


for key in keywords:
	url = 'https://www.zazzle.com/s/'+key
	by_to_zazzle(url,key)

