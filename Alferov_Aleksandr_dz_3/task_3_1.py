# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

# ヽ(ˇヘˇ)ノ

def num_translate(num, dict):
    print(dict.get(num))

word_book = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

digit = input('Ввод пользователя: ')
num_translate(digit, word_book)