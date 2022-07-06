# s = input('inter a word: ')
# if s == s[::-1]:
#     print ('yes')
# else:
#     print ('no')
#
# str = 'qwerty'[::-1]
# print(type(str))


# s = 'qwer qwet qwet'
# i = s.split(' ')
# l = len()
# print(l)

# import datetime
# n= int(input('enter num: '))
# time_format = str(datetime.timedelta(seconds = n))
# print("Time in preferred format :-",time_format)
#
# hour = n // 3600
# n = n % 60
# def convert_to_preferred_format(sec):
#     sec = sec % (24 * 3600)
#     hour = sec // 3600 sec %= 3600
#     min = sec // 60 sec %= 60
#     print("seconds value in hours:",hour)
#     print("seconds value in minutes:",min)
#     return "%02d:%02d:%02d" % (hour, min, sec)
#     n = 10000 print("Time in preferred format :-",convert(n))
# i = int(input('enter: '))
# day = i / 86400
# hours = i / 3600
# second = i / 60
# print(f'{}')

# n = int(input('enter: '))
# suma = 0
# while n > 0:
#     digit = n % 10
#     suma = suma + digit
#     n = n // 10
# print("Сумма:", suma)

#
# f1 = f2 = 1
# n = int(input())
# print(f1, f2, end=' ')
# for i in range(2, n):
#     f1, f2 = f2, f1 + f2
#     print(f2, end=' ')

# for i in range(1, 51):
#     if i % 3== 0:
#         print(f'{i} fizz')
#     elif i % 5 ==0:
#         print(f'{i} buzz')
#     elif i % 3 and 5 ==0:
#         print(f'{i} fizzbuzz')













# def proc(money:float,year:int) -> float:
#     if money < 30000:
#         raise Exception('vvedy horoshee chislo suchka')
#     if year < 3:
#         raise Exception('napishi horoshuyu stroku suchka min 3 god pishi')
#     i = 0
#     while i < year:
#         money = money + (money * 0.1)
#         i += 1
#         return money
#
# money = float(input("Введите кол-во money: "))
# year = int(input("Введите кол-во year: "))
# print(proc(money,year))




def re():
    s = 'Hello world, my name is suzi'
    p = s.split(' ')
    print(s)
    d = p[::-1]
    print(' '.join(d))
re()








