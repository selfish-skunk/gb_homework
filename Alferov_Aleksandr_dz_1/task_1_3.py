# Задание 3.
# Реализовать склонение слова «процент» для чисел до 20.

# пользовательский ввод
number = int(input('введите число от 1 до 20: '))
# обработка
if number == 1:
    print(number, 'процент')
elif 2 <= number <= 4:
        print(number, 'процента')
elif 5 <= number <= 20:
        print(number, 'процентов')

# проверка циклом
print('вывод всех сколений при помощи цикла: ')
for number in range(1, 21):
    if number == 1:
        print(number, 'процент')
    elif 2 <= number <= 4:
        print(number, 'процента')
    elif 5 <= number <= 20:
        print(number, 'процентов')