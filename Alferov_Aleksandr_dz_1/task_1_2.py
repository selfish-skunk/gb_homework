# Задание 2.
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000

# список для нечетных чисел, возведенных в куб
noteven_cubes = []
# заполняем список
for i in range(1001):
    if i % 2 != 0:
        i = i**3
        noteven_cubes.append(i)
print('список нечетных чисел, возведенных в куб:', noteven_cubes)

# a). Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

# список для сумм чисел, которые делятся на 7 (суммы, не сами числа)
devide_by7_list = []
# a_few_hours_later.jpg ( ╯°□°)╯ ┻━━┻
for num in noteven_cubes:
    num_helper = num
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    if sum % 7 == 0:
        devide_by7_list.append(num_helper)
print('список чисел, суммы цифр которых делятся на 7:', devide_by7_list)
# считаем финальную сумму чисел
sum_final = 0
for i in devide_by7_list:
    sum_final += i
print('сумма чисел, сумма цифр которых делится на 7:', sum_final)

# b). К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

# список для сумм чисел, которые делятся на 7 (суммы, не сами числа)
devide_by7_list_17plus = []
# считаем
for num1 in noteven_cubes:
    num1 += 17
    num_helper1 = num1
    sum1 = 0
    while (num1 != 0):
        sum1 = sum1 + num1 % 10
        num1 = num1 // 10
    if sum1 % 7 == 0:
        devide_by7_list_17plus.append(num_helper1)
print('список чисел + 17, суммы цифр которых делятся на 7:', devide_by7_list_17plus)
# считаем финальную сумму чисел еще раз
sum_final1 = 0
for i in devide_by7_list_17plus:
    sum_final1 += i
print('сумма чисел, сумма цифр которых делится на 7:', sum_final1)