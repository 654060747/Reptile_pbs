# conding-utf-8
import requests,time
import json,csv
import codecs

# 响应状态码，大于等于200小于300表示成功；大于等于400小于500为客户端错误；大于500为服务端错误。
# csv路径
csv_path = "./bbb_no_data.csv"
# 读取csv文件
csv_file = csv.reader(open(csv_path,'r',encoding='UTF-8'))

# 写 csv
def write_csv(data):
	file = "liu.csv"

	with codecs.open(file,'a',encoding='utf-8') as f:
		f.write(data+"\n")
		f.close()

def get_cjh(url,cx,cjh):

	headers = {'Authorization':'APPCODE 159d3607c3554c16876be6231cf5935a'}
	rs = requests.get(url,headers=headers)
	rs.encoding = 'utf-8'
	print(rs)
	if rs.status_code == 200:
		data = json.loads(rs.text)
		car_pp = data['showapi_res_body']['brand_name']
		print(car_pp)
		car_cx = data['showapi_res_body']['model_name']
		print(car_cx)
		car_xh_name = data['showapi_res_body']['sale_name']
		print(car_xh_name)
		car_nf = data['showapi_res_body']['year']
		data = cx+","+cjh+","+car_pp+","+car_cx+","+car_xh_name+" "+car_nf+"款"

		write_csv(data)


for line in csv_file:
	cjh = line[1]
	url = "https://ali-vin.showapi.com/vin?vin="+cjh
	get_cjh(url,line[0],cjh)
	time.sleep(0.2)