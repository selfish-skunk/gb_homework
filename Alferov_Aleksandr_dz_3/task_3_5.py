# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого)

# (╮°-°)╮┳━━┳ ( ╯°□°)╯ ┻━━┻

from random import randrange

def get_jokes(num):
    """
    Функция get_jokes принимает в качестве аргумента число и выдает аналогичное количество унылых сочетаний слов
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    while i < num:
        print(f'{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} '
              f'{adjectives[randrange(len(adjectives))]}')
        i += 1

jokes_number = input('Ввод пользователя: ')
get_jokes(int(jokes_number))
