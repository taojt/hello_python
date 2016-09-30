# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/29
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


if __name__ == '__main__':
    main()
