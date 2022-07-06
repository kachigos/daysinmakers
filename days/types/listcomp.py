# ls = []
# for i in range(200):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# l = []
# for i in range(200):
#     if i % 2 == 0 and i % 3 == 0:
#         l.append(i)
# print(l)
#
# l = []
# for i in range(200):
#      if i % 2 ==0:
#          l.append(i**2)
#      else:
#          l.append(i)
# print(l)

# говно код
# res = []
# for i in range(1, 25, 2):
#     res.append(i)
# print(res)
#
# # так то лучше
# res = [i for i in range(1, 25, 2)]
# print(res)

# li = [[1,2,3],[4,5,6],[2,3,4]]
# ls = [i for x in li for i in x]
# print(ls)
# import datetime
# ls = []
# now = datetime.datetime.now()
# for i in range(10000000):
#     ls.append(i)
# finish = datetime.datetime.now()
# print(finish-now)
#
# ls = [x for x in range(10000000)]
# print(ls)


# ls = [x+10 if x == 8 else x+1 for x in range(0,10)]
# print(ls)

'''
8. Создайте список из 10 произвольных имён, затем пройдитесь
 по данному списку и  если имя состоит меньше чем из 4 букв
замените имя на 'shorter', а если больше на 'longer'. Нужно использовать comprehension.
'''


l = ['qwerty','katana','kumanjan','cat','lol','all']
# prices = [29, 10, 44, 5, 90]
ls = [l if len(l) < 5  else l for i in l]
print(ls)
