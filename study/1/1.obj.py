# -*- coding: utf-8 -*-
from base_obj import Bird

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

summer = Chicken()
print(summer.have_feather)
print(summer.way_of_move)
print(summer.move(5,8))


class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print(self.gender)

li_lei = Human('male') # 这里，'male'作为参数传递给__init__()方法的input_gender变量。
print(li_lei.gender)
li_lei.printGender()


