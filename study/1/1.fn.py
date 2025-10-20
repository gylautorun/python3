# -*- coding: utf-8 -*-
a = 1

def change_integer(a):
    a = a + 1
    return a

print(change_integer(a))
print(a)

# ===Python中 "#" 后面跟的内容是注释，不执行

b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print(change_list(b))
print(b)


# 闰年判断
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2100))