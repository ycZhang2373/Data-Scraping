# -*- encoding: utf-8 -*-
#@File    :   test_re.py
#@Time    :   2021/08/22 13:03:02
#@Author  :   Xinyi Zhang 
#@Version :   3.9.6 64-bit
#@Contact :   xzhang2373@wisc.edu
# pip install xxx -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re

# compile()
'''
pat = re.compile("AA")       #此处的AA是正则表达式，用来验证其他的字符串
m=pat.search("CDAAC")        #search字符串被校验的内容
print(m)
# <re.Match object; span=(2, 4), match='AA'>
m=pat.search("CDAACDDAA")    #search字符串被校验的内容
print(m)
# <re.Match object; span=(2, 4), match='AA'>
m = pat.research("asd",r"Aasd")  #前面"asd"是规则，后面"Aasd"是被匹配的
'''

# findall()
# 建议在被比较的字符串前面加上r，不用担心转义字符的问题
'''
print(re.findall("a",r"ASDaDFGAa"))   #前面字符串是正则表达式，后面字符串是被校验的字符串
# 得到['A', 'S', 'D', 'D', 'F', 'G', 'A']
print(re.findall("[A-Z]+",r"ASDaDFGAa"))
# 得到['ASD', 'DFGA']
'''

# sub()
print(re.sub("a","A",r"abcdcasd")) #找到a，用A来替换

a = r"\aabd-\'"
print(a)