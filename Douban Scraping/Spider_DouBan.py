# -*- encoding: utf-8 -*-
# @File    :   douban.py
# @Time    :   2021/08/22 12:59:47
# @Author  :   Xinyi Zhang
# @Version :   3.9.6 64-bit
# @Contact :   xzhang2373@wisc.edu
# pip install googletrans -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

from bs4 import BeautifulSoup             # 网页解析，获取数据
import re                                 # 正则表达式，文字匹配
import urllib.request
import urllib.error       # 置顶url，获取网页数据
import xlwt                               # 进行excel操作
import sqlite3                            # 进行SQLite数据操作

##############################################
################# 1. 爬取网页 #################
##############################################
# 得到指定的一个url网页内容; User-Agent告诉豆瓣我们是什么类型的机器：浏览器
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "connection": "Keep-Alive",
        "Cookie": 'll="108288"; bid=rcVJJytKE8o; __utmc=30149280; __utmz=30149280.1629452843.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __gads=ID=51ed4a16a17716eb-2264c9640ccb0087:T=1629452773:RT=1629452773:S=ALNI_MZcAbr-bD0mdXNF2hXMkuWVppAhvQ; __utmc=223695111; __utmz=223695111.1629452985.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=30149280.2065318824.1629452843.1629476036.1629611169.4; __utma=223695111.896588906.1629452985.1629476945.1629611169.4; _pk_id.100001.4cf6=9c53f18909d60055.1629452985.4.1629611608.1629476951.'
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e, code)
        if hasattr(e, "reason"):
            print(e, reason)
    print("The Web-Connection is Done")
    return html

##############################################
################# 定义全局变量 ################
##############################################

#定义全局变量
# 注意到电影链接：<a href="https://movie.douban.com/subject/3319755/">
findLink = re.compile(r'<a href="(.*?)">')
# 图片行：<img alt="影名" class="" src="https://jpg链接" width="100"/> re.S考虑换行符
findImgSrc = re.compile(r'<img.*src="(.*?)".*/>', re.S)
# 影片片名：<span class="title">肖申克的救赎</span>
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分：<span class="rating_num" property="v:average">9.7</span>
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数：<span>2429742人评价</span>
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况：<span class="inq">希望让人自由。</span>
findInq = re.compile(r'<span class="inq">(.*?)</span>')
# 找到影片的相关内容，注意相关内容有换行，需要re.S
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

##############################################
############## 2. 逐一解析数据 ################
##############################################
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数，共10次
        url = baseurl + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 注意解析数据：html
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串，形成列表; class是类别，必须加下划线，和python内部class区分
        for item in soup.find_all('div', class_="item"):
            # print(item)  #测试：查看电影item信息
            data = []  # 保存一部电影的所有信息
            item = str(item)
            # re库通过正则表达式查找指定的字符串,[0]保证返回的是数组第一个
            link = re.findall(findLink, item)[0]
            data.append(link)
            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)
            title = re.findall(findTitle, item)  # 片名可能只有中文名，没有英文
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)  # 添加中文名
                otitle = title[1].replace("/", "")
                otitle = otitle.strip()
                data.append(otitle)  # 添加外国名
            else:
                data.append(title[0])
                data.append('')  # 外国名字留空
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append("")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)   #替换掉<\br>
            bd = re.sub('/',"",bd)
            data.append(bd.strip())       #去掉bd前后的空格
            datalist.append(data)  #把第一步电影信息放入datalist
    return datalist

##############################################
################# 3. 保存数据 #################
##############################################
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("豆瓣电影250",cell_overwrite_ok=True)
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)
    print("爬取完毕")


if __name__ == "__main__":  
    baseurl = "https://movie.douban.com/top250?start="
    savepath = r".\豆瓣电影Top250.xlsx"
    datalist = getData(baseurl)
    saveData(datalist,savepath)
