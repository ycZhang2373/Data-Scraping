'''
BeautifulSoup4 将复杂的html文档转变成树形结构
'''
from bs4 import BeautifulSoup
import re

file = open("C:\\Users\\zhangxinyi\\OneDrive\\桌面\\vs_code\\vs1\\test\\douban.html","rb")   # rb: read bytes
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
soup = bs.find_all()
print(soup)
print(type(soup))

'''
1.Tag 标签及其内容：拿到它所找到的第一个内容
print(type(bs.head))

2. NavigableString：标签里的内容
print(bs.title)
print(bs.title.string)
print(type(bs.title.string))

3. a.attars：拿到a标签里所有的属性，返回一个字典
print(bs.a.attrs)

4. 表示整个文档；输出不包含注释符号
print(type(bs))
print(bs.name)
print(bs)

print(bs.a.string)
print(type(bs.a.string))
'''

#-------------------------------------
# 文档的遍历
# print(bs.head.contents)         #返回的是list
# print(bs.head.contents[2])  
# 更多content之外的内容，如父节点、子节点、兄弟节点之类，自己去查…… 

#########################################
################ 文档的搜索 ##############
#########################################

'''
#(1) 字符串过滤：查找与字符串完全匹配的内容。findall()，返回一个list
t_list = bs.find_all("a")
print(t_list)

#(2) 正则表达式方法：使用search()方法来匹配内容
t_list = bs.find_all(re.compile("a"))
print(t_list)


# (3) 传入一个函数，根据函数的要求来搜索
def name_is_exists(tag):
return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)
for item in t_list:
    print(item)
'''

#########################################
################ 参数的搜索 ##############
#########################################

# t_list = bs.find_all(id="anony-reg-new")
# for item in t_list:
#     print(item)

#3.text参数
# t_list= bs.find_all(text = ["豆瓣"])
# for item in t_list:
#     print(item)

#应用正则表达式来查找包含特定文本的内容
# t_list= bs.find_all(text = re.compile("\d"))   
# for item in t_list:
#     print(item)

#4. limit
# t_list= bs.find_all(text = "a",limit = 3)   
# for item in t_list:
#     print(item)

#5. 选择器
# print(bs.select('title'))   #通过标签查找
# t_list = bs.select(".mnav")  # 通过类名查找
# t_list = bs.select("#u1")   # id=u1来查找
# t_list= bs.select("a[bs.select()class='bri']")  # 属性查找：a这个标签的这个属性
# t_list= bs.select("div > ul > li")
# t_list = bs.select(".app-slogan ~ .app-title")
# for item in t_list:
#     print(item.get_text())