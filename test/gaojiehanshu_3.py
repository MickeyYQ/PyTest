#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n % 2 == 1

x = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print "x:",x