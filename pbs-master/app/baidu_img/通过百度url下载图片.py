# coding=utf-8
import csv,requests
import time
import os
from contextlib import closing

# csv路径
file_list = "./img"

# 下载图片后保存的路径
dir_name = "./load_img"


def CheckDir(dir):
    if not os.path.exists(dir):
      os.makedirs(dir)
    pass

CheckDir(dir_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
 
#http请求超时设置
timeout = 10
#下载
def DownloadFile(img_url, dir_name, img_name):
    # check_download_dir(folder_name)
    try:
        with closing(requests.get(img_url, stream=True, headers=headers, timeout=timeout)) as r:
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
            except:
                # print('save fail \t%s' % img_url)
                print('save fail \t%s' % img_url)
    except:
        # print('requests fail \t%s' % img_url)

        print('requests fail \t%s' % img_url)




movie_name = os.listdir('./'+file_list)
# 循环文件
for csv_path in movie_name:
	print(csv_path)

	csv_file = csv.reader(open(file_list+"/"+csv_path,'r', encoding='utf8'))

	# 循环文件所有内容
	for line in csv_file:

		# 取图片url
		img_url_start = line[2]
		img_url_end = line[3]
		img_url = img_url_start+","+img_url_end
		print(img_url)

		# 图片名(可自由设置，这里是把已给的csv第一个字段作为图片名)
		img_name = line[0]
		print(img_name)
		DownloadFile(img_url,dir_name,img_name)
		time.sleep(1)
