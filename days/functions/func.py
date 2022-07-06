# def popa(a,b):
#     return a + b
# p = popa(12,12)
# print(p)


# def i(a):
#     if a % 2 ==0:
#         return True
#     else:
#         return False
# k = int(input('enter'))
# print(i(k))

# def isEven(num: int) -> bool:
#     '''
#     проверка на четность
#     '''
#     if num % 2 == 0:
#         return True
#     return False
# print(isEven(122))


# def polindrom(words: list) -> list:
#     'palindrom'
#     ls = words[::-1]


# def check_palindrome(string):
#     reversed_string = string[::-1]
#     if string == reversed_string:
#         print(string, "is a palindrome")
#     else:
#         print(string, "is not a Palindrome")
# check_palindrome('aziza')


# def re(a,b,c,d):
#     return a+b+c+d
# re(1,2,3,4)  # позиционные аргументы
# re(a=1,b=2,c=3,d=4) # именованные аргументы (keyword arguments)

# a = [1,2,3,4]
# b = [5,6,7,8]
# c = [*a,*b]
# print(c)


# def te(s,*args):
#     print(s)
#     print(args)
#     print(type(args))
# te('mama',132,123,4132)

# def he(s,**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# he(12, dog=1234,cat='ewqr')




# def plus(a,b):
#     return a+b
# def minus(a,b):
#     return a-b
# def de(a,b):
#     return a/b
# def um(a,b):
#     return a*b
#
# def main():
#     a = int(input('enter first num: '))
#     b = int(input('enter second num: '))
#     print('команды введите так: ( + ) ( - ) ( / ) ( * )')
#     c = input('enter com: ')
#     if c == '+':
#         return plus(a,b)
#     elif c == '-':
#         return minus(a,b)
#     elif c == '/':
#         return de(a,b)
#     elif c == 'um':
#         return um(a,b)
#
# print(main())




"""
области видимости пространство имен

"""

# встроенные -> print, len, max
# global
# enclosed (не локальная)
# local локальная


# def l(ls):
#     for i in ls:
#         print(i)
# i = 'qwer'
# l([1,2,3,4,5,67,7])
# print(i)



a = 'qwr'
def i():
    print(a)
i()




