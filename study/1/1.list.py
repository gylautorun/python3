for a in range(10):
    print(a**2)





my_list = ['apple', 'banana', 'orange', 'pear']

# for i in range(len(my_list)):
#     print('Index: {}, Value: {}'.format(my_list.index(i), my_list[i]))

print(enumerate(my_list))
for i, value in enumerate(my_list):
    print('Index: {}, Value: {}'.format(i, value))


