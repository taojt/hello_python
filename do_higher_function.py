# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/20
# 高阶函数式编程， 将函数名作为参数传入，这样的函数叫做高阶函数
# test， 定义两个数的绝对值和

f = abs


def add(a, b, f):
    return f(a) + f(b)


print('add(-5,6,f)=', add(-5, 6, f))


# python 中的map 和 reduce 函数
# map() 接收两个参数，一个是函数，一个是Iterable，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,但此时是map对象，需要list（）转换


# test 把函数f(x)=x^2 作用到list [1,2,3,4,5,6,7,8,9] 上，就可以用map来实现
def f(x):
    return x * x


r = map(f, range(10))
print(list(r))
# 将所有的数字转换为字符串
print(list(map(str, range(10))))

# reduce() 接收两个参数，把一个函数作用在序列上，把结果继续和序列的下一个元素做累积运算，效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# reduce zai functools m哦快中，需要导入使用

# test 用reduce 对序列求和
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


# map 和 reduce 一起使用，将数字字符串转化为整数，自己实现int()函数:
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(n):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[n]

    return reduce(fn, map(char2num, s))


m = str2int('12356')
print('type of m is ', type(m), '\nm=', m)


# test 规范用户的英文名字，变为首字母大写，其他小写的规范字
def normlize_name(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normlize_name, L1))
print(L2)


# test 写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def mul(x, y):
        return x * y

    return reduce(mul, L)


print(prod([1, 3, 5, 7, 9]))


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    m = s.find('.')
    if m > 0:
        n = len(s) - m - 1
    else:
        n = 0

    def fn(x, y):
        if y == -1:
            return x
        return x * 10 + y

    def char2num(n):
        if n is '.':
            return -1
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[n]

    return (reduce(fn, map(char2num, s))) / (10 ** n)


print(str2float('123.456'))
print(str2float('123456'))
print(str2float('0.123456'))
