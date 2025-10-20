# -*- coding: utf-8 -*-

array = [1, 2, 3, 4, 5]
# print(dir(array))
print(array.__len__())
print(array.count(5))
print(array.index(5))
array.append(6)
print('append', array)
array.sort()
print('sort', array)
array.reverse()
print('reverse', array)
array.pop()
print('pop', array)
array.extend([7, 8])
print('extend', array)
array.insert(0, 9)
print('insert', array)

print([1,2,3] + [5,6,9])

# 报错
# print([1,2,3] - [3,4])

class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]        
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print(superList([1,2,3,4,5]) - superList([3,4]))
