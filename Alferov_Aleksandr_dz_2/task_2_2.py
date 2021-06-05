# 2. Необходимо обработать список - обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов

# (∩ᄑ_ᄑ)⊃━☆ﾟ*･｡*
start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
end_list = []
counter = 0

# курусель ярости
for n in start_list:
    if n.isdigit():
        end_list.insert(counter, '"')
        counter += 1
        end_list.insert(counter, f'{int(n):02}')
        counter += 1
        end_list.insert(counter, '"')
        counter += 1
    elif (n.startswith('+') or n.startswith('-')) and n[1:].isdigit():
        end_list.insert(counter, '"')
        counter += 1
        end_list.insert(counter, n[0])
        counter += 1
        end_list.insert(counter, f'{int(n[1:]):02}')
        counter += 1
        end_list.insert(counter, '"')
        counter += 1
    else:
        end_list.insert(counter, n)
        counter += 1

result = ' '.join(end_list)
print(result)
