# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/21
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


if __name__ == '__main__':
    bart = Student('Bart Simpson', 86)
    lisa = Student('Lisa Hellen', 100)
    bart.print_score()
    lisa.print_score()
    # 访问内部私有变量出错
    print(bart.__score)
