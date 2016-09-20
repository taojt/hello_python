# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/20

a = [1, 2, 3, 4, 5]

for i in a:
    print(i, end=" ")

print()

d = {'a': 1, 'b': 'boy', 'c': True}
for key in d:
    print(key, ':', d.get(key))

for ch in 'ABCdef':
    print(ch)

# use function enumerate to transfer list to pair with index and value
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)