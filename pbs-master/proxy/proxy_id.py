__author__ = 'llg.cc'
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import http.client
import threading
from random import choice


# 代理ip(使用代理配置)
# proxys = ["111.11.100.13:8060","45.221.77.82:8080","112.109.198.106:3128","60.9.1.80:80","47.106.216.42:8000","116.196.115.209:8080"]
# #1.使用python random模块的choice方法随机选择某个元素
# proxy = choice(proxys)

# proxy_d = "http://"+proxy

# proxies = {
#     "http":proxy_d
# }


inFile = open('proxy.txt')
outFile = open('verified.txt', 'w')
lock = threading.Lock()

def getProxyList(targeturl="http://www.xicidaili.com/nn/"):
    countNum = 0
    proxyFile = open('proxy.txt' , 'a')
    
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}

    for page in range(1, 10):
        url = targeturl + str(page)
        #print url
        # 使用代理
        # req = requests.get(url, proxies=proxies, headers=requestHeader)
        # 不使用代理
        req = requests.get(url, headers=requestHeader)
        html_doc = req.text
    
        soup = BeautifulSoup(html_doc, "html.parser")
        #print soup
        trs = soup.find('table', id='ip_list').find_all('tr')
        if trs != None:
            for tr in trs[1:]:
                tds = tr.find_all('td')
                #国家
                if tds[0].find('img') is None :
                    nation = '未知'
                    locate = '未知'
                else:
                    nation =   tds[0].find('img')['alt'].strip()
                    locate  =   tds[3].text.strip()
                ip      =   tds[1].text.strip()
                port    =   tds[2].text.strip()
                anony   =   tds[4].text.strip()
                protocol=   tds[5].text.strip()
                speed   =   tds[6].find('div')['title'].strip()
                time    =   tds[8].text.strip()
                
                proxyFile.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol,speed, time) )
                print ('%s=%s:%s' % (protocol, ip, port))
                countNum += 1
    
    proxyFile.close()
    return countNum
    
def verifyProxyList():
    '''
    验证代理的有效性
    '''
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    myurl = 'http://www.baidu.com/'

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0: break
        line = ll.split('|')
        protocol= line[5]
        ip      = line[1]
        port    = line[2]
        
        try:
            conn = http.client.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method = 'GET', url = myurl, headers = requestHeader )
            res = conn.getresponse()
            lock.acquire()
            print ("+++Success:" + ip + ":" + port)
            outFile.write(protocol+"://"+ip + ":" + port + "\n")
            lock.release()
        except:
            print ("---Failure:" + ip + ":" + port)
        
    
if __name__ == '__main__':
    tmp = open('proxy.txt' , 'w')
    tmp.write("")
    tmp.close()

    proxynum = getProxyList("http://www.xicidaili.com/nn/")
    print (u"国内高匿：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/nt/")
    print (u"国内透明：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wn/")
    print (u"国外高匿：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wt/")
    print (u"国外透明：" + str(proxynum))

    print (u"\n验证代理的有效性：")
    
    all_thread = []
    for i in range(50):
        t = threading.Thread(target=verifyProxyList)
        all_thread.append(t)
        t.start()
        
    for t in all_thread:
        t.join()
    
    inFile.close()
    outFile.close()
    print ("All Done.")