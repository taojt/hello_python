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