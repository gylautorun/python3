# -*- coding: utf-8 -*-

# f = open('./2.txt', 'r')
# content = f.read()           # 读取N bytes的数据
# print('content', content)
# line = f.readline()       # 读取一行
# print('line', line)
# readlines = f.readlines()      # 读取所有行，储存在列表中，每个元素是一行
# print('readlines', readlines)

fw = open('./2.txt', 'w')
readlines = fw.readlines()  
fw.write('I like apple')      # 将'I like apple'写入文件



