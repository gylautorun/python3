# -*- coding: utf-8 -*-

# 位置传递
def f(a,b,c):
    return a+b+c
print(f(1,2,3))

# 关键字传递
def f(a,b,c):
    print(a,b,c) # 1,2,3
    return a+b+c
print(f(c=3,b=2,a=1))
print(f(1,c=3,b=2))

# 参数默认值
# 在定义函数的时候，使用形如a=19的方式，可以给参数赋予默认值(default)。
# 如果该参数最终没有被传递值，将使用该默认值。
def f(a,b,c=10):
    return a+b+c
print(f(3,2)) # 15
print(f(3,2,1)) # 6

# 包裹传递
# 在定义函数时，我们有时候并不知道调用的时候会传递多少个参数。
# 这时候，包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会非常有用
# 在func的参数表中，所有的参数被name收集，根据位置合并成一个元组(tuple)
# 提醒Python参数，name是包裹位置传递所用的元组名，在定义func时，在name前加*号
def func(*name):
    print(type(name)) # <type 'tuple'>
    print(name) # (1,2,3,....)
func(1,4,6)
func(5,6,7,1,2,3)
func(5)
## 包裹关键字传递
#  dict是一个字典，收集所有的关键字，传递给函数func。
#  为了提醒Python，参数dict是包裹关键字传递所用的字典，在dict前加**
def func(**dict):
    print(type(dict)) # <type 'dict'>
    print(dict) # {'x': x, 'y': y, ...}
func(a=1,b=9)
func(m=2,n=1,c=11)
# 包裹传递的关键在于定义函数时，在相应元组或字典前加*或**


# 解包裹
# *和**，也可以在调用的时候使用，即解包裹(unpacking)
# 所谓的解包裹，就是在传递tuple时，让tuple的每一个元素对应一个位置参数
# 在传递词典dict时，让词典的每个键值对作为一个关键字传递给func
def func(a,b,c):
    print(a,b,c)
args = (1,3,4)
func(*args)
dict = {'a':1,'b':2,'c':3}
func(**dict)

# 混合
# 在定义或者调用参数时，参数的几种传递方式可以混合。
# 前后顺序基本原则是: 
#   先位置，
#   再关键字，
#   再包裹位置，
#   再包裹关键字


