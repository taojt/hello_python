# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/30
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict's object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value