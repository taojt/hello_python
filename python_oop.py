# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/21
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if score >= 0 and score<= 100:
            self.__score = score
        else:
            raise ValueError('bad eeror.')


if __name__ == '__main__':
    bart = Student('Bart Simpson', 86)
    lisa = Student('Lisa Hellen', 100)
    bart.print_score()
    lisa.print_score()
    # 访问内部私有变量出错
    # print(bart.__score)

    # getter
    print(bart.get_name(), bart.get_score())

    # setter
    bart.set_name("Tom")
    bart.set_score(89)
    print(bart.get_name(), bart.get_score())


