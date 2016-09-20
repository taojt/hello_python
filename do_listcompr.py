# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/20
import os

print([x * x for x in range(1, 11)])

# 两层循环
print([m + n for m in 'ABCD' for n in 'xyz'])

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])

# for 循环对dict 的item() 可以同时迭代key 和 value
d = {'x': 1, 'y': 23, 'z': "hello"}
for k, v in d.items():
    print(k, '=', v)
