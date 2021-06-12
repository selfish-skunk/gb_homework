# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def nums_gen(n):
    for num in range(1, n + 1):
        if num % 2 != 0:
            yield num


result = int(input('Введите число n: '))

print(list(nums_gen(result)))
