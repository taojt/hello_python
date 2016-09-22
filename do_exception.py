# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/22
try:
    print('try...')
    r = 10/0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:, ',e)
finally:
    print('finally...')
print('End. ')

try:
    print('try...')
    r = 10/int('2')
    print('result: ',r)
except ValueError as e:
    print('Value Error:', e)
except ZeroDivisionError as e:
    print('except:, ',e)
else:
    print('no error. ')
finally:
    print('finally...')
print('End. ')
print()


# reraise 异常，抛给上层函数处理
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value %s' %n)
    r = 10/n;
    print('result: ', r)

def bar():
    try:
        foo(0)
    except ValueError as e:
        print('error: ', e)

bar()
