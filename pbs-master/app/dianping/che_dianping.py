# conding=utf-8
from fontTools.ttLib import TTFont

from PIL import Image, ImageDraw, ImageFont  #绘制图片
import pytesseract   #文字识别库,这个包的安装还需要安装tesseract.exe，可以网上搜教程
import numpy

# font = TTFont('./woff/fd8152c2.woff')    # 打开文件
# font.saveXML('./xml_woff/font.xml')     # 转换成 xml 文件并保存

def fontConvert(fontPath):     #将web下载的字体文件解析，返回其编码和汉字的对应关系
    font = TTFont(fontPath)  # 打开文件
    codeList = font.getGlyphOrder()[2:]
    im = Image.new("RGB", (1800, 1000), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(fontPath, 40)
    count = 15
    arrayList = numpy.array_split(codeList,count)   #将列表切分成15份，以便于在图片上分行显示
    for t in range(count):
        newList = [i.replace("uni", "\\u") for i in arrayList[t]]
        text = "".join(newList)
        text = text.encode('utf-8').decode('unicode_escape')
        dr.text((0, 50 * t), text, font=font, fill="#000000")
    # im.save("sss.jpg")
    # im = Image.open("sss.jpg")      #可以将图片保存到本地，以便于手动打开图片查看
    result = pytesseract.image_to_string(im, lang="chi_sim")
    result = result.replace(" ","").replace("\n","") #OCR识别出来的字符串有空格换行符
    codeList = [i.replace("uni","&#x")+";" for i in codeList]
    return dict(zip(codeList,list(result)))



print(fontConvert("./woff/hours.woff"))



