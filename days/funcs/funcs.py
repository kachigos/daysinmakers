'''
func -> map
func -> filter
func -> lambda
func -> enumerate
'''

#  lambda анонимные функции который выполняет только часть кусок функции например:

# def x(a,b):
#     return a + b
# print(x(12,12))

# p = lambda a,b: a+b,
# m = p(12,12)
# print(m)
#
print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))



# ls = ['qwe', 'reqw', 'asdf', ' ','   ']
# new = sorted(ls, key=len)
# print(new)

# ls = [11,12,14,124,542,356,345,234,3245,232,5]







# import random
# p=0
# m=0
# k=0
# l=0
# for i in range(0,1000):
#     choice= random.choice(i)
#     print(choice)
#     if choice.lower() == 'plov':
#         p= p+1#p+=1 инкремент
#     elif choice.lower() == 'manty':
#         m+=1
#     elif choice.lower() == 'kuurdak':
#         k+=1
#     elif choice.lower() == 'lagman':
#         l+=1
#
# print(f'Plov:{p},\nManty:{m},\nKuurdak:{k}.\nLagman:{l}')