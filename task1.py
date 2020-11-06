# Task 1
# def last_one():
#     num =input("Enter any number:")
#     print(num[-1])

# last_one()


# Task 2
# def isdigit():
#     digit = input("Enter any number: ")
#     digit = int(digit)

#     if digit %2 ==0:
#         print("This number is even")
#     else:
#         print("This number is odd")

# isdigit()



# Task 4
# def palindrom():
#     word = input("Enter any word: ")
#     if word[::-1] == word:
#         print("This word is palindrom")
#     else:
#         print("This is not palindrom")

# palindrom()



# Task 6
# def sum_ofnumbers():
#     num = input ('Введите трехзначное число : ')

#     if len(num) < 3 or len(num) > 3 :
#         print('Введите трехзначное число!!!')
#     else: 
#        num = str(num)
#        print(int(num[0]) + int(num[1]) + int(num[2]))

# sum_ofnumbers()



#  Task 7
# def number_rank():
#     num = input("Enter any number: ")
#     print('Количество разрядов ' + str(len(num)))

# number_rank()



# Task 3
# def square () :

#     num = input ('Введите число : ')
#     squares = []

#     for number in range (int(num)):
#         number = number ** 2
#         squares.append(str(number))

#     print(','.join(squares))

# square()


# Task 5
# import datetime

# def check_date () :
#     day = int(input("Введите день : "))
#     month = int(input("Введите месяц : "))
#     year = int(input("Введите год : "))
#     try:
#         data = datetime.date(year, month, day)
#         print (data)
#         print (True) 

#     except:
#         print (False)

# check_date()


# Task 8
# def max_num () :
#     nums = []
#     bol = -1

#     while True:
#          try :
#             n = input('("exit" чтобы выйти) Введите число: ')

#             if n == 'exit':
#                 print('Максимальное число : ' + bol)
#                 break

#             nums.append(n)

#             for x in nums :
#                 if int(x) > int(bol) :
#                     bol = x
        
#         except ValueError :
#             raise TypeError ('Это программа принимает только числа!!')

# max_num()



# Task 9
def calculator () :
    try:
        operations = ['+', '-', '*', '/']
        operation = input ('| + | - | * | / | ')
    
        while operation not in operations :
            raise TypeError ('Выбрана неверная операция!!')
            operation = input ('| + | - | * | / | ')

        num1 = input ('Введите первое число : ')
        num2 = input ('Введите второе число : ')

        if operation == '+' :
            res = int(num1) + int(num2)
            print(f'Ответ : {res}')

        elif operation == '-' :
            res = int(num1) - int(num2)
            print(f'Ответ : {res}')

        elif operation == '*' :
            res = int(num1) * int(num2)
            print(f'Ответ : {res}')

        elif operation == '/' :
            res = int(num1) / int(num2)
            print(f'Ответ : {res}')  
    except ZeroDivisionError :
        raise TypeError ('На ноль делить нельзя !!!')   

    except ValueError :
        raise TypeError ('Это программа принимает только цифры !!!')   

    finally :
        print('Пока!')

calculator()
