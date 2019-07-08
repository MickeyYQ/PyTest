#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 将当前目录改为"/home/newdir"
# os.chdir("C:\Users\Lenovo\Documents\zip") 可以用chdir()方法来改变当前的目录。
# path = os.chdir("C:\\Users\\Lenovo\\Documents\\zip")
# os.walk()
#os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
#os.chdir(path) 改变当前工作目录

path = "C:\Users\Lenovo\Documents\zip"
dirs = os.listdir(path)

# 输出所有文件和文件夹
fileadd = []
for file in dirs:
   print file
   filepath = path + "\\" + file
   print "文件路径：",filepath
   if os.path.isdir(filepath):
       print "it's a directory"
       #fileadd.remove(file)
       del fileadd[0]
   elif os.path.isfile(filepath):
       print "it's a normal file"
       fileadd.append(file)
   else:
       print "it's a special file(socket,FIFO,device file)"
       fileadd.remove(file)
   #fileadd.append(file)
print fileadd
print len(fileadd)
print fileadd[0]

