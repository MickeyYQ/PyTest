#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist


# 可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;


# 调用printme函数
printme("好");
#必须传入一个参数
# 否则就会
# Traceback (most recent call last):
#   File "test.py", line 11, in <module>
#     printme();
# TypeError: printme() takes exactly 1 argument (0 given)