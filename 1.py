# """ """ a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
# for elem in a:
#     if elem < 15:
#         print(elem)

#  """

# """number = float(input("Введите число: "))
# if number > 0:
#     print("Число положительное")
# elif number < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")
# """


# """ def add(x, y):
#     return x + y
# def subsract(x,y):
#     return x - y
# def multiply(x,y):
#     return x * y
# def divide(x,y): 
#     return x / y

# num1 = float(input("Введите первое число"))
# num2 = float(input("Введите второе число"))

# operation = input("Выберите операцию (+, -, *, /): ")

# if operation == "+":
#     print(f"Результат: {add(num1,num2)}")
# elif operation == '-':
#     print(f"Результат: {subtract(num1, num2)}")
# elif operation == '*':
#     print(f"Результат: {multiply(num1, num2)}")
# elif operation == '/':
#     print(f"Результат: {divide(num1, num2)}")
# else:
#     print("Неверная операция") """


# """ for i in range(10, 0, -1):
#     print(i) """

# """ import math

# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))

# discriminant = b**2 - 4*a*c

# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2*a)
#     root2 = (-b - math.sqrt(discriminant)) / (2*a)
#     print(f"Два корня: {root1} и {root2}")
# elif discriminant == 0:
#     root = -b / (2*a)
#     print(f"Один корень: {root}")
# else:
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#     print(f"корни: {real_part} + {imaginary_part}i и {real_part} - {imaginary_part}i") """


# """ import random

# number = random.randint(1, 10)
# print("Загадано случайное число от 1 до 10. Попробуйте угадать его!")
# a = 0
# while True:
#     try:
#         a = int(input("Введите ваше предположение: "))
#         if a < number:
#             a+=1
#             print(f"Больше! попыток: {a}")
#         elif a > number:
#             a+=1
#             print(f"Меньше! попыток: {a}")
#         else:
#             print("Поздравляем! Вы угадали число.")
#             break
#     except ValueError:
#         print("Пожалуйста, введите целое число.")
#  """

# def group_identical_symbols(input_string):
#     symbols = input_string.split()
#     result = []
#     current_group = []
#     for symbol in symbols:
#         if current_group and current_group[-1] == symbol:
#             current_group.append(symbol)
#         else:
#             if current_group:
#                 result.append(current_group)
#             current_group = [symbol]
    
#     if current_group:
#         result.append(current_group)
    
#     return result

# input_string = "c c c o o o c c w w w w c k k k a a a a"
# grouped_data = group_identical_symbols(input_string)
# print(grouped_data)
#  """