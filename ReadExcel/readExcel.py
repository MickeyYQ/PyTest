#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlwt
import xlrd

class RFile:

    def readfile(self,file):
        print "file",file
        # 打开文件
        f = open(file, 'rb')
        xld = xlrd.open_workbook(file)
        sheet = xld.sheet_by_index(0)  # 根据sheet编号来
        print sheet.row_values(0)

        # 关闭文件
        f.close()

    def writefile(self,file):
        print "file", file

rf = RFile()
file = "‪c:\\Users\\Lenovo\\Desktop\\JYGZ.xlsx"
rf.readfile(file)