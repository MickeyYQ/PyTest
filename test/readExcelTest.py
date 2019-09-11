#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd

filename = "c:\Users\Lenovo\Desktop\JYGZ.xlsx";
filename = filename.decode('GBK')
#filename = unicode(filename,'utf-8')
#打开文件
#file = open(filename ,'rb')
#book1=xlrd.open_workbook(filename,'rb')
book = xlrd.open_workbook(filename)
#获取所有sheet页的名字
print "sheet页名称：",book.sheet_names()
sheet = book.sheet_by_index(3)  #根据sheet编号来
# sheet=book.sheet_by_name('sheet1')   #根据 sheet名称来
print sheet.nrows  #excel里面有多少行
print sheet.ncols  #excel里面有多少列
print sheet.cell(0,0).value  #获取第0行第0列的值
print sheet.row_values(0)  #获取到整行的内容
print sheet.col_values(0) #获取到整列的内容

for i in range(sheet.nrows):  #循环获取每行的内容
    print(sheet.row_values(i))