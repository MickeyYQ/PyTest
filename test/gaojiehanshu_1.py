#!/usr/bin/python
# -*- coding: UTF-8 -*-

def add(x, y, f):
    print "x:", x
    print "y:", y
    print "f:", f
    return f(x) + f(y)
    print "f:", f

#print "结果为：", (add(-5, 6, abs))
print "结果为：", add(-5, 6, abs)
