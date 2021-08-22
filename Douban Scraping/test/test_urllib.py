import urllib.request
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode("utf-8"))

'''
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")  #把所有信息转化成二进制的数据包
也可以data={}，什么用户名密码什么的在这里输入（利用封装，模拟用户登录）
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))
'''

'''
try:
    response = urllib.request.urlopen("http://httpbin.org/get", data={},timeout=100) #设置时间，如果没响应就算了
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")
'''

'''
# 返回错误信息418：意味着别人已经意识到你是爬虫
response = urllib.request.urlopen("http://www.baidu.com")
# print(response.getheaders()  # 获取了所有头部信息，状态码
print(response.getheader('Connection').decode("utf-8"))  # 获取了所有头部信息，状态码
'''

'''
# url = "https://www.douban.com"
url = "http://httpbin.org/post"
# 一个完美的爬虫可以把网页里request header的数据完全放到headers里面
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

# 访问豆瓣！！返回的request放入txt，转换成html文件，再用bs4解码
def html():
    url = "https://www.douban.com"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))
    return response.read().decode("utf-8")

if __name__ == '__main__':
    html()


