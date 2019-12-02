import codecs

# 写 csv
def write_csv(data):
	file = "a.csv"

	with codecs.open(file,'a',encoding='utf-8') as f:
		f.write(data+"\n")
		f.close()




string = "（大众 帕萨特 1.8T 手动 舒适版 2005款）"

data = string.split("（")[1].split("）")[0].split(" ")
print("品牌::"+data[0])
print("车系::"+data[1])
cx_all = ""
for x in range(2,len(data)):
	cx = data[x]
	cx_all = cx_all+cx+" "
print("型号::"+cx_all)
data = data[0]+","+data[1]+","+cx_all
