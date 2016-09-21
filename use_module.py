# -*-coding: utf-8 -*-
# Create by Jiang Tao on 2016/9/21

from PIL import Image
im = Image.open('image01.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200,100))
# 缩小图片尺寸
im.save('thumb.jpg', 'JPEG')