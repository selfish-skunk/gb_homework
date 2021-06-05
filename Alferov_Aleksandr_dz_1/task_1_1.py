# Задание 1.
# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

# ввод пользователя
duration = int(input('Введите количество секунд: '))

# математика
days_count = duration // 86400
hours_count = (duration % 86400) // 3600
minutes_count = ((duration % 86400) % 3600) // 60
seconds_count = (((duration % 86400) % 3600) % 60)

# топорный вывод и гоблинские технологии
if days_count == 0 and hours_count == 0 and minutes_count == 0:
    print(seconds_count, 'сек')
elif days_count == 0 and hours_count == 0 and minutes_count != 0:
    print(minutes_count, 'мин', seconds_count, 'сек')
elif days_count == 0 and hours_count != 0 and minutes_count != 0:
    print(hours_count, 'час', minutes_count, 'мин', seconds_count, 'сек')
elif days_count != 0 and hours_count != 0 and minutes_count != 0:
    print(days_count, 'дн', hours_count, 'час', minutes_count, 'мин', seconds_count, 'сек')