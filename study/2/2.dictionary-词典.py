# -*- coding: utf-8 -*-

# 词典的元素没有顺序，key-value对组成
dic = {'tom':11, 'sam':57,'lily':100}
print(type(dic))
print(dic)
print("dic['tom']", dic['tom'])
dic['tom'] = 12
print(dic)
dic['new'] = 99
print(dic)

for key in dic:
    print(key, dic[key])



print('keys', dic.keys())
print('values', dic.values())
print('items', dic.items())
print('len', len(dic))
dic.clear()
print('dic', dic)
