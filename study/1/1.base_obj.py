class Bird(object):
    have_feet = 2
    have_feather = True
    way_of_reproduction = 'egg'

    def move(self, dx, dy):
        position = [0, 0]
        position[0] += dx
        position[1] += dy
        return position



# summer = Bird()
# print(summer.way_of_reproduction)
# print('after move:')
# print(summer.move(1, 2))
# print(summer.move(5,8))



