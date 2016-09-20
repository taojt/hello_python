# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/20

# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
g = (x * x for x in range(10))
print(g)
# 访问生成器的元素
for n in g:
    print(n, end=" ")
print()


# 函数中含有yield关键字，那么这个函数就是一个生成器generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


# 函数中遇到yield 就中断，不会调用返回值
print(fib(6))


# test，不断输出杨辉三角
def triangle():
    ls = [1]
    while True:
        yield ls
        ls.append(0)
        ls = [ls[i - 1] + ls[i] for i in range(len(ls))]


n = 0
for lst in triangle():
    print(lst)
    n += 1
    if n == 20:
        break