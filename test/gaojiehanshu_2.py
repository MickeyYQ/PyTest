#!/usr/bin/python
# -*- coding: UTF-8 -*-
# main方法
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce

def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
x = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

list(r)
print "list",list(r)
print list(x)


def add(x,y):
    return x+y

a = reduce(add,[1,2,3,4,5])
b = reduce(add,[1,3,5,7,9])
print "a:",a ,"b:",b


def fn(i,j):
    return i+j