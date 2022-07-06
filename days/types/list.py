# list -- тип данных изменяемый
# list_ = [1341,'1324',[1342],{2341},{12:'sfgfsd'}]
# print(type(list_))
#
# mylist = list('hi gues')
# print(mylist)

# tup = ('nana','koko', 'popa')
# print(type(tup))


# range() -- возврашает последовательность элементов
# a = list(range(0,100))
# print(a)


# list_ = []
# print(type(list_))
# print(list_.append('mam'))
# print(list_)

# i = [1,2,3]
# i.extend('hello')
# print(i)

# insert добавляет элемент по указанному index

# lsit = ['sdf', 123,'wer']
# lsit.insert(1,['wrt'])
# lsit.insert(2,3)
# print(lsit)
# print(lsit[-1])

# index (element, [start],[end])

# ls = [123,123,123,452,5,25,2,5]
# i = ls.index(5)
# print(i)


# remove(element) delete
# pop([index]) удаляет и возврашает
# element если не указать элемент удаляет последний element

# ls = [1,14,35,521,14,14]
# ls.remove(14)
# print(ls)
# deleted = ls.pop()
# print(deleted)

# sort([reverse=True/False],[key=<>])
# сортирует список for example :
# ls = [12,13,314,325,23425,25,235]
# ls.sort()
# print(ls)

# ls = ['hi', 'hello', 'python','d']
# ls.sort(key=len)
# print(ls)

# ls = [1,2,3]
# ls[0] = 5
# print(ls)

"""
7) Дан список в котором хранится строка.
Разрежьте его на две равные части (если длина строки нечетная,
то длина первой части должна быть на один символ больше).
Переставьте эти две части местами, при этом каждый символ должен
являться отдельной строкой, результат запишите в новый список и выведите на экран.
 """
import  string
newList = []
ls = ["mama papa kokakol lolopepa"]
# string.join(ls)
# i = len(ls[0])
# d = i.split()
# p = len(ls)/2
# for o in range(len(ls[0])):
#     print(newList.append(o))
# l = list(range(ls))




# tuple_ = ('a', 1, 'Hello', True, ['1', 'b'])
# tuple_.index('Hello')


# for st in range(tuple_):
#     print(st)

# for numFor in range(0, len(tuple)):
#         list = list + str(tuple[numFor])
