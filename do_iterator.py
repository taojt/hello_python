# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/20
from collections import Iterable

# list,set,dict 虽然都是Iterable，但是不是Iterator，所以不存在next() 方法，但是经过iter() 函数处理后就是Iterator
# 生成器generator 是Iterator 对象，可以调用 next() 方法
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
