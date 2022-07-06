# while True:
#     if input('enter: ') in 'fuck negr'.split():
#         print('block')
#         break


DB_EMAIL = []
while True:
    print(' 1) Input Email \n 2) Show email \n 3) delete \n 4) stop \n 5) update')
    choices = int(input('enter choice: '))
    if choices == 1:
        email = input('enter your email: ')
        if email.endswith('@gmail.com'):
            DB_EMAIL.append(email)
        else:
            print('your email kata')
    elif choices == 2:
        print(DB_EMAIL)
    elif choices == 3:
        email = input('enter email: ')
        if email in DB_EMAIL:
            DB_EMAIL.remove(email)
        else:
            print(f'{email} not in datebase')
    elif choices ==4:
        break
    elif choices ==5:
        oldemail = input('enter old email: ')
        if email in DB_EMAIL:
            newemail = input('enter new email: ')
            DB_EMAIL.remove\
                (oldemail)
            DB_EMAIL.append\
                (newemail)
        else:
            print('this email not in datebase')

    else:
        print('Error')

