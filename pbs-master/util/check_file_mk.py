#coding=utf-8
# # # # # # # # BEGIN INIT INFO # # # # # # # # # # # # # #
#  copyright   : Copyright (c) 2019 emdata.
#  filename    : std.py
#  author      : emdata/data.dev
#  version     : 0.0.1
#  created     : 2019-08-17
#  description :  下载 ftp 链接文件
#
#  history     :
#
# # # # # # # # END INIT INFO # # # # # # # # # # # # # # #

import os

#  1.用于遍历文件夹下的所有指定后缀名的文件的具体路径
# 参数： 
#   path：需要遍历的目录， 
#   ext： 文件后缀名，默认为 .jpg  
# 返回值: 文件绝对路径
def list_file(path, ext='.jpg'):
    L=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            file_ext = file.endswith(ext)
            if file_ext:
                fpath = os.path.join(root, file)
                L.append(fpath)
    return L

def test_list_file():
    path = '/home'
    a = list_file(path)
    print(a)

if __name__ == "__main__":
    test_list_file()
