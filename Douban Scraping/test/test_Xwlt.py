# -*- encoding: utf-8 -*-
#@File    :   test_Xwlt.py
#@Time    :   2021/08/22 17:27:16
#@Author  :   Xinyi Zhang 
#@Version :   3.9.6 64-bit
#@Contact :   xzhang2373@wisc.edu
# pip install xxx -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

import xlwt
'''
workbook = xlwt.Workbook(encoding='utf-8')  #创建workbook对象
worksheet = workbook.add_sheet('sheet')  #创建工作表
worksheet.write(0,0,3*3) #写入数据，(row,collumn,content)
workbook.save('student.xls') #保存数据表
'''
workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
worksheet = workbook.add_sheet('sheet',cell_overwrite_ok=True)
for i in range (0,9):
    for j in range (0,i+1):
        worksheet.write(i,j,"%d * %d = %d" %(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls') #保存数据表